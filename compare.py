#!/usr/bin/env python
# 比较两个文件夹，并将其差异文件，以相同的目录结构拷贝到指定位置中
import os
import sys
import filecmp
import re
import shutil

holderlist = []


def compareme(dir1, dir2):
    dircomp = filecmp.dircmp(dir1, dir2)
    only_in_one = dircomp.left_only
    diff_in_one = dircomp.diff_files
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in diff_in_one]
    if len(dircomp.common_dirs) > 0:
        for item in dircomp.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1, item)), os.path.abspath(os.path.join(dir2, item)))
        return holderlist


def main():
    # if len(sys.argv) > 3:
    #     dir1 = sys.argv[1]
    #     dir2 = sys.argv[2]
    #     dir3 = sys.argv[3]
    # else:
    #     print("Usage: ", sys.argv[0], "current_dir old_dir target_dir")
    #     sys.exit(1)
    dir1 = r'Z:\works\sc01\android\frameworks\base\packages\SystemUI'
    dir2 = r'Y:\sg00\mydroid\vendor\desaysv\g5\packages\apps\privileges\SystemUI'
    dir3 = r'D:\data\diff'
    if not (os.path.exists(dir1) and os.path.exists(dir2)):
        print('Please make sure the path is correct and exist')
        sys.exit(1)
    if not os.path.exists(dir3):
        os.makedirs(dir3)
    if not (os.path.isdir(dir1) and os.path.isdir(dir2) and os.path.isdir(dir3)):
        print('Please make sure the path is a directory')
        sys.exit(1)
    temp = dir1.split(os.path.sep)
    length = len(temp)
    if not dir3.endswith(os.sep):
        dir3 = dir3 + os.sep
    dir3 = dir3 + temp[length - 1]
    print(dir3)
    if not os.path.exists(dir3):
        os.makedirs(os.path.abspath(dir3))
    if not dir3.endswith(os.sep):
        dir3 = dir3 + os.sep
    source_files = compareme(dir1, dir2)
    dir1 = os.path.abspath(dir1)
    dir3 = os.path.abspath(dir3)
    if os.sep == '\\':
        dir1 = dir1.replace('\\', '\\\\')
        dir3 = dir3.replace('\\', '\\\\')
    destination_files = []
    new_dirs_create = []
    for item in source_files:
        destination_files.append(re.sub(dir1, dir3, item))
    print(destination_files)
    for item in destination_files:
        new_dirs_create.append(os.path.split(item)[0])
    for mydir in set(new_dirs_create):
        if not os.path.exists(mydir):
            os.makedirs(mydir)
    # copy pair
    copy_pair = zip(source_files, destination_files)
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])


if __name__ == '__main__':
    main()
