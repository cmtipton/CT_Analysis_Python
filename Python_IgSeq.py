#! /usr/bin/env python

import os, sys, zipfile

path = sys.argv[1]

files = os.listdir(path)
num_files = len(files)
#print num_folders

num = 1
#num_folders = 3
for num in range(num_files):
        print files[num-1]
        num = num + 1

#zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
#zip_ref.extractall(directory_to_extract_to)
#zip_ref.close()
