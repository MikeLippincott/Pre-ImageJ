#!/usr/bin/env python
# coding: utf-8
import os
import shutil
from tkinter.filedialog import askdirectory


# Function moves all files in a directory to new folder
# Args: Path = input folder, destination = new folder


def filemove():
    path = askdirectory()
    destination = askdirectory()
    templst = []
    for root, dirs, files in os.walk(path):
        files.sort()
        for f in files:
            if not f.startswith('.'):  # ignores the .DS_Store file
                templst.append(f)
    for i in templst:
        filepath = (os.path.join(root, i))
        dest = os.path.join(destination, i)
        if filepath.endswith(".dv"):
            shutil.move(f'{filepath}', dest)


def main():
    return


if __name__ == "main":
    main()
