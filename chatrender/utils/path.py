import re


def relativize_path(path):
    return re.sub('^/', '', path)
