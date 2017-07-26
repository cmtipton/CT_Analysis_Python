#! /usr/bin/env python

import os, sys

folders = os.walk(sys.argv[1]).next()[1]
num_folders = len(folders)
#print num_folders

num = 1
#num_folders = 3
for num in range(num_folders):
        print folders[num-1]
        num = num + 1
