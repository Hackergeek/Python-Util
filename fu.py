import os
import shutil


def change_dir(absolute_path):
    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)
    os.chdir(absolute_path)


def copy(source_path, destination_path):
    if os.path.isdir(source_path):
        copy_tree(source_path, destination_path)
    else:
        copy_file(source_path, destination_path)


def copy_file(source_path, destination_path):
    if os.path.exists(destination_path):
        os.remove(destination_path)
    shutil.copy(source_path, destination_path)


def copy_tree(source_path, destination_path):
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    shutil.copytree(source_path, destination_path)


if __name__ == '__main__':
    pass
