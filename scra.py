#!/usr/bin/env python3
import glob, os, shutil, sys

#scra.py - A File Scraping Python Script by colonEndBracket

#If user only runs 'scra.py'
if len(sys.argv) == 1:
    print("[About>] Recursive File Scraping from specified folder of specified file types into a folder labeled 'dump-scrapy'")
    print("[Usage>] ./scra.py <target_directory> <file_types>")
    print("[e.g. >] ./scra.py .. png jpg mp4")
    exit()
#If user supplies directory but not file types
elif len(sys.argv) == 2:
    print("[ERROR>] File types not listed")
    print("[Usage>] ./scra.py <target_directory> <file_types>")
    print("[e.g. >] ./scra.py .. png jpg mp4")
    exit()

#Prepare dump-scrapy folder
os.system("rm -rf ./dump-scrapy")
os.system("mkdir ./dump-scrapy")

#Define directories
user_home = os.path.expanduser("~")
source_dir = sys.argv[1]
if source_dir == user_home:
    source_dir += "/"
dest_dir = "./dump-scrapy"

#Process the file types
filetypes = []
typeprinted = "[scra.py>] Scraping for"
for spectyp in sys.argv[2:]:
    filetypes.append(spectyp)
    typeprinted += " "+spectyp
typeprinted += " files in "+source_dir
print(typeprinted)

#Find and copy files
f_found = 0
for i in filetypes:
    itech=source_dir+"**/*."+i
    files = glob.glob(itech, recursive=True)
    for file in files:
        if os.path.isfile(file):
            print("# "+file)
            shutil.copy(file, dest_dir)
            f_found += 1

#Print results
if f_found == 0:
    print("[scra.py>] No files were scraped!")
else:
    print("[scra.py>] %s files were scraped and placed in dump-scrapy/!" % f_found)
