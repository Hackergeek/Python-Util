import os
import shutil


def change_dir(absolute_path):
    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)
    os.chdir(absolute_path)


def copy_file(source_path, destination_path, cover=True):
    if os.path.exists(destination_path):
        if cover:
            os.remove(destination_path)
        else:
            print('file existed!!!')
            return
    shutil.copy(source_path, destination_path)


def copy_tree(source_path, destination_path, cover=True):
    if os.path.exists(destination_path):
        if cover:
            shutil.rmtree(destination_path)
        else:
            print('directory existed!!!')
            return
    shutil.copytree(source_path, destination_path)


def copy(source_path, destination_path, cover=True):
    if os.path.isdir(source_path):
        copy_tree(source_path, destination_path, cover)
    else:
        copy_file(source_path, destination_path, cover)


if __name__ == '__main__':
    pass
