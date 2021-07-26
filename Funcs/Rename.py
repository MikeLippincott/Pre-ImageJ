#!/usr/bin/env python
# coding: utf-8
import os
from tkinter.filedialog import askdirectory


# Function sorts files in directory then adds an index to the name for sorting


def rename():
    path = askdirectory()
    for root, dirs, files in os.walk(path):
        files.sort()
        templst = []
        for f in files:
            if not f.startswith('.'):  # ignores the .DS_Store file
                templst.append(f)
    for i in templst:
        filepath = (os.path.join(root, i))
        if filepath.endswith(".dv"):
            newname = root + str(templst.index(i)) + "_" + i
            os.rename(filepath, newname)


def main():
    return


if __name__ == "main":
    main()
