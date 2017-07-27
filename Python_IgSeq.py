#! /usr/bin/env python

import os, sys, tarfile, re, glob, shutil, time

path = sys.argv[1]

high_folders = os.walk(sys.argv[1]).next()[1]
high_num_folders = len(high_folders)
high_num = 1
for high_num in range(high_num_folders):
    high_src = sys.argv[1]+"/"+high_folders[high_num-1]
    print high_src
    high_num = high_num + 1

    #Remove past data folder
    if os.path.exists("/Users/cmtipto/IgSeq/Data/"):
        shutil.rmtree('/Users/cmtipto/IgSeq/Data/')

    #make new data folder
    if not os.path.exists("/Users/cmtipto/IgSeq/Data/"):
        os.makedirs("/Users/cmtipto/IgSeq/Data/")

    #Find txz files in the folder
    txzs = []
    for root, dirs, files in os.walk(high_src):
        txzs += glob.glob(os.path.join(root, '*.txz'))

    #Determine and print the number of txz files in the folder
    num_files = len(txzs)
    print(num_files)

    #For each txz, make a folder of the same name and decompress into that folder
    num = 1
    for num in range(num_files):
        directory = os.path.splitext(txzs[num])
        print(directory[0])
        os.makedirs(directory[0])
        os.system("tar -xvzf"+txzs[num-1]+" -C "+directory[0])
        num = num + 1

    #Identify the folders made
    folders = os.walk(high_src).next()[1]
    num_folders = len(folders)

    #print folders and move folders to IgSeq folder
    num = 1
    for num in range(num_folders):
            src = high_src+"/"+folders[num-1]
            print src
            num = num + 1
            shutil.move(src, "/Users/cmtipto/IgSeq/Data/")

    time.sleep(5)
