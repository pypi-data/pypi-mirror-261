"""Read/Write image files in S3/Minio storage.
"""
# Copyright (c) 2024 Erling Andersen, Haukeland University Hospital, Bergen, Norway

from typing import List, Optional
import os.path
import io
from minio import Minio
import minio.error
import minio.datatypes
import urllib
import logging
import tempfile
import shutil
from imagedata.transports.abstracttransport import AbstractTransport

logger = logging.getLogger(__name__)


class S3Transport(AbstractTransport):
    """Read/write from S3/Minio storage.
    """

    name: str = "s3"
    description: str = "Read and write from S3/Minio storage."
    authors: str = "Erling Andersen"
    version: str = "1.0.0"
    url: str = "www.helse-bergen.no"
    schemes: List[str] = ["s3"]
    mimetype: str = "application/zip"  # Determines archive plugin

    def __init__(self,
                 netloc: Optional[str] = None,
                 root: Optional[str] = None,
                 mode: Optional[str] = 'r',
                 read_directory_only: Optional[bool] = False,
                 opts: Optional[dict] = None):
        super(S3Transport, self).__init__(self.name, self.description,
                                          self.authors, self.version, self.url, self.schemes)
        # self.client = Minio(
        #     "play.min.io",
        #     access_key="Q3AM3UQ867SPQQA43P2F",
        #     secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
        #     cert_check=False
        # )
        # if self.client.bucket_exists("imagedata_transport_s3"):
        #     logger.debug('Bucket exists')
        # else:
        #     logger.debug('Bucket do not exist')
        if opts is None:
            opts = {}
        self.read_directory_only = read_directory_only
        self.opts = {}
        for attr in ['username', 'password']:
            try:
                self.opts[attr] = opts[attr]
            except KeyError:
                self.opts[attr] = None
        # Does netloc include username and password?
        if '@' in netloc:
            # Add fake scheme to satisfy urlsplit()
            url_tuple = urllib.parse.urlsplit('s3://' + netloc)
            self.netloc = url_tuple.hostname
            try:
                self.opts['username'] = url_tuple.username
            except AttributeError:
                pass
            try:
                self.opts['password'] = url_tuple.password
            except AttributeError:
                pass
        else:
            self.netloc = netloc
        logger.debug("S3Transport __init__ root: {}".format(root))
        root_split = root.split('/')
        try:
            bucket = root_split[1]
        except IndexError:
            raise ValueError('No bucket given in URL {}'.format(root))
        self.destination = "/".join(root_split[2:]) \
            if len(root_split) > 2 and len(root_split[2]) \
            else None
        self.__mode = mode
        self.__local = False
        self.__must_upload = False
        self.__tmpdir = None
        self.__zipfile = None

        self.client = Minio(
            self.netloc,
            access_key=self.opts['username'],
            secret_key=self.opts['password'],
            cert_check=True
        )
        self.bucket = bucket
        try:
            if not self.client.bucket_exists(bucket):
                if mode[0] == 'r':
                    raise FileNotFoundError("Bucket ({}) does not exist".format(bucket))
                else:
                    self.client.make_bucket(bucket)
                logger.debug('Bucket "{}" is created'.format(bucket))
        except minio.error.S3Error:
            logger.debug('After except minio.error.S3Error:')
            if mode[0] == 'r':
                raise FileNotFoundError("Bucket ({}) does not exist".format(bucket))
            else:
                self.client.make_bucket(bucket)
            logger.debug('Bucket "{}" is created'.format(bucket))

    def walk(self, top):
        """Generate the file names in a directory tree by walking the tree.
        Input:
        - top: starting point for walk (str)
        Return:
        - tuples of (root, dirs, files)
        """
        def _yield_dir(parent_dir, root):
            logger.debug('_yield_dir: {}'.format(parent_dir))
            logger.debug('_yield_dir: yield {} {} {}'.format(
                root, [*parent_dir['dirs']], parent_dir['files']
            ))
            yield root, [*parent_dir['dirs']], parent_dir['files']
            logger.debug('_yield_dir: yield done')
            for d in parent_dir['dirs'].keys():
                logger.debug('_yield_dir: key {}'.format(d))
                child_root = '/{}'.format(d) if root == '/' else '{}/{}'.format(root, d)
                yield from _yield_dir(parent_dir['dirs'][d], child_root)

        logger.debug('S3Transport.walk:')
        bucket, prefix = self._get_bucket_and_object(top)
        logger.debug('S3Transport.walk: bucket: {}, prefix: {}'.format(bucket, prefix))
        objects = self.client.list_objects(
            self.bucket, prefix=prefix, recursive=True,
        )
        logger.debug('S3Transport.walk: calling _sort_objects')
        dirs = _sort_objects(prefix, objects)
        logger.debug('S3Transport.walk: returned _sort_objects:\ndirs: {}'.format(
            dirs)
        )

        for root, dirs, files in _yield_dir(dirs['/'], '/'):
            logger.debug('S3Transport.walk: yield {} {} {}'.format(root, dirs, files))
            yield root, dirs, files

    def isfile(self, path):
        """Return True if path is an existing regular file.
        """
        bucket, obj = self._get_bucket_and_object(path)
        try:
            result: minio.datatypes.Object = self.client.stat_object(bucket, obj)
            return not result.is_dir
        except minio.error.S3Error:
            return False

    def exists(self, path):
        """Return True if the named path exists.
        """
        bucket, obj = self._get_bucket_and_object(path)
        try:
            self.client.stat_object(bucket, obj)
            return True
        except minio.error.S3Error:
            return False

    def _get_bucket_and_object(self, path):
        path_split = path.split('/')
        try:
            bucket = path_split[1]
            obj = '/'.join(path_split[2:])
        except IndexError:
            raise ValueError('No bucket given in URL {}'.format(path))
        if self.bucket != bucket:
            raise FileNotFoundError('Bucket {} is not open'.format(bucket))
        logger.debug('S3Transport.open: bucket: "{}", object ({}): "{}"'.format(
            bucket, type(obj), obj))
        return bucket, obj

    def open(self, path, mode='r'):
        """Extract a member from the archive as a file-like object.
        """
        bucket, obj = self._get_bucket_and_object(path)

        if mode[0] == 'r' and not self.__local:
            if len(obj) == 0:
                raise FileNotFoundError('Empty filename "{}" not found.'.format(obj))
            self.__tmpdir = tempfile.mkdtemp()
            self.__zipfile = os.path.join(self.__tmpdir, obj)
            self.client.fget_object(
                bucket_name=self.bucket,
                object_name=obj,
                file_path=self.__zipfile
            )
            self.__local = True

        elif mode[0] == 'w' and not self.__local:
            logger.debug('Open "w" path: {}'.format(obj))
            self.__tmpdir = tempfile.mkdtemp()
            self.__zipfile = os.path.join(self.__tmpdir, 'upload.zip')
            self.__path = obj
            self.__local = True
            self.__must_upload = True
            logger.debug('Write {}'.format(self.__zipfile))
        if self.__local:
            return io.FileIO(self.__zipfile, mode)
        else:
            raise IOError('Could not download bucket "{}"'.format(self.bucket))

    def close(self):
        """Close the transport
        """
        if self.__must_upload:
            # Upload zip file to S3 server
            logger.debug('Upload to bucket "{}"'.format(self.bucket))
            try:
                result = self.client.fput_object(bucket_name=self.bucket,
                                                 object_name=self.__path,
                                                 file_path=self.__zipfile,
                                                 content_type="application/zip"
                                                 )
                logger.debug('Upload created {}; etag: {}, version-id: {}'.format(
                    result.object_name, result.etag, result.version_id
                ))
            except Exception as e:
                logger.debug('Upload exception: {}'.format(e))
                raise
        if self.__tmpdir is not None:
            shutil.rmtree(self.__tmpdir)

    def info(self, path) -> str:
        """Return info describing the object

        Args:
            path (str): object path

        Returns:
            description (str): Preferably a one-line string describing the object
        """
        bucket, obj = self._get_bucket_and_object(path)
        try:
            result: minio.datatypes.Object = self.client.stat_object(bucket, obj)
            return '{} {} {} {}'.format(
                result.object_name, result.content_type, result.size, result.last_modified
            )
        except minio.error.S3Error:
            raise FileNotFoundError('File not found: {}'.format(path))


def _sort_objects(prefix, objects):
    # logger.debug('S3Transport._sort_objects: prefix: ' + prefix)
    dirs = {'/': {'dirs': {}, 'files': []}}
    try:
        for obj in objects:
            # logger.debug('S3Transport._sort_objects: object: {}: {}'.format(
            #     obj.object_name, obj.is_dir)
            # )
            _add_object(dirs, obj)
    except Exception as e:
        logger.error('S3Transport._sort_objects: exception:\n  {}'.format(e))
    return dirs


def _add_object(dirs, object):
    filename = object.object_name
    logger.debug('_add_object: filename: {}'.format(filename))
    path = filename.split('/')
    parent_dir = dirs['/']
    try:
        for component in path[1:-1]:
            # logger.debug('_add_object: component :  {}'.format(component))
            # logger.debug('_add_object: dirs      : {} ({})'.format(dirs, type(dirs)))
            # logger.debug('_add_object: parent_dir: {} ({})'.format(parent_dir, type(parent_dir)))
            if component not in parent_dir['dirs']:
                parent_dir['dirs'][component] = {'dirs': {}, 'files': []}
            parent_dir = parent_dir['dirs'][component]
        # logger.debug('_add_object: dirs       before insert into files: {}'.format(dirs))
        # logger.debug('_add_object: parent_dir before insert into files: {}'.format(parent_dir))
        if object.is_dir:
            parent_dir['dirs'].append(path[-1])
        else:
            parent_dir['files'].append(path[-1])
    except Exception as e:
        logger.error('_add_object: exception: {}'.format(e))
    # logger.debug('_add_object: dirs: {}'.format(dirs))
