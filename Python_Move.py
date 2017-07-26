#! /usr/bin/env python

import shutil, os, sys, re

#Finds arguments from command line
src = sys.argv[1]
dest_part = sys.argv[2]

#Finds substring of folder to be moved
fold = re.search(r'(.*)/(.*)', src)
fold2 = fold.group(2)

#Assembles full path for destination
dest = dest_part+"/"+fold2

#Confirms Source and Destination
print "Source: ", src
print "Destination: ", dest

#Copies folder to new location
shutil.copytree(src, dest)
print os.listdir(dest)

#Removes source folder
shutil.rmtree(src)

print "Done"
