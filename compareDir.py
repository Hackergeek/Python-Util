#! /usr/bin/python
# 缺点： 一次只能同步一级目录

import os,sys
import filecmp
import re
import shutil
holderlist = []
temp = []


def comparedir(dir1, dir2):
    dircomp = filecmp.dircmp(dir1, dir2, ignore=temp)
    only_in_one = dircomp.left_only
    diff_in_one = dircomp.diff_files
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in diff_in_one]
    if len(dircomp.common_dirs) > 0:
        for item in dircomp.common_dirs:
            comparedir(os.path.abspath(os.path.join(dir1, item)), os.path.abspath(os.path.join(dir2, item)))
        return holderlist
    else:
        return holderlist


def main():
    dir2 = 'E:\\SystemUI'
    dir1 = 'D:\\android-4.4.4_r1\\frameworks\\base\\packages\\SystemUI'
    # dir1 = 'C:\\Users\\12240\\PycharmProjects\\autoMake'
    # dir2 = 'E:\\autoMake'

    # if len(sys.argv) > 2:
    #     dir1 = sys.argv[1]
    #     dir2 = sys.argv[2]
    #     temp = sys.argv[3:]
    # else:
    #     print('Usage: ', sys.argv[0], " datadir backupdir ignorelist")
    #     sys.exit(1)
    if not (os.path.exists(dir1) and os.path.exists(dir2)):
        print('Please make sure the path is correct and exist')
        return
    source_files = comparedir(dir1, dir2)
    dir1 = os.path.abspath(dir1)
    dir2 = os.path.abspath(dir2)
    destination_files = []
    createdir_bool = False

    if os.sep == '\\':
        dir1 = dir1.replace('\\', '\\\\')
        dir2 = dir2.replace('\\', '\\\\')

    print(dir1)
    print(dir2)

    for item in source_files:
        destination_dir = re.sub(dir1, dir2, item)
        destination_files.append(destination_dir)
        if os.path.isdir(item):
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool = True
    if createdir_bool:
        destination_files = []
        source_files = comparedir(dir1, dir2)
        for item in source_files:
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)

    print('update item:', source_files)
    print('total count:', len(source_files))
    print('destination_files', destination_files)
    copy_pair = zip(source_files, destination_files)
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])


if __name__ == '__main__':
    main()
