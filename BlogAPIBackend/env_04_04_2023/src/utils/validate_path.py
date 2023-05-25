import os.path


def create_path_if_not_exist(path):
    """ Create the folder path if not exist"""
    os.makedirs(path, exist_ok=True)
    return "Folder Created"
