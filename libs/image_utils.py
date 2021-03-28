from os.path import splitext, join
from uuid import uuid4


def update_file_path(instance, filename, path, file_type):
    _, extension = splitext(filename)
    filename_format = "%s_%s%s" % (uuid4(), file_type, extension)
    return join(path, filename_format)
