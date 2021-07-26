#!/usr/bin/env python
# coding: utf-8
import os
import shutil
from tkinter.filedialog import askdirectory


def filesort(searchstring):
    path = askdirectory()
    destination = askdirectory()
    for root, dirs, files in os.walk(path):
        files.sort()
        templst = []
        for f in files:
            if not f.startswith('.'):  # ignores the .DS_Store file
                templst.append(f)
    for i in templst:
        print(i)
        filepath = (os.path.join(root, i))
        dest = os.path.join(destination, i)
        if filepath.endswith(".dv"):
            if f'{searchstring}' in filepath:
                shutil.move(f'{filepath}', dest)


def main():
    return


if __name__ == "main":
    main()
