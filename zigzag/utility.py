# -*- coding: utf-8 -*-
import codecs
import os
import errno
from types import MethodType, ModuleType


def from_pyfile(self, filename, silent=False):
    """Override existing from_pyfile method to read py file in
    encoding 'UTF-8'.
    See: http://www.sdg32.com/flask-instance-folders/
         https://www.ianlewis.org/en/dynamically-adding-method-classes-or-class-instanc

    :param filename: the filename of the config.  This can either be an
                     absolute filename or a filename relative to the
                     root path.
    :param silent: set to ``True`` if you want silent failure for missing
                   files.

    .. versionadded:: 0.7
       `silent` parameter.
    """
    filename = os.path.join(self.root_path, filename)
    d = ModuleType('config')
    d.__file__ = filename
    try:
        with codecs.open(filename, encoding='utf-8') as config_file:
            exec(compile(config_file.read(), filename, 'exec'), d.__dict__)
    except IOError as e:
        if silent and e.errno in (errno.ENOENT, errno.EISDIR):
            return False
        e.strerror = 'Unable to load configuration file (%s)' % e.strerror
        raise
    self.from_object(d)
    return True


class Zigzag:

    def __init__(self, flask_obj):
        flask_obj.config.from_pyfile = MethodType(
            from_pyfile, flask_obj.config)