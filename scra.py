#!/usr/bin/python3
import glob, os, shutil, sys

#scra.py - A File Scraping Python Script by colonEndBracket

if len(sys.argv) == 1:
    print("[About>] Recursive File Scraping from specified folder of specified file types into a folder labeled 'dump-scrapy'")
    print("[Usage>] ./scra.py <target_directory> <file_types>")
    print("[e.g. >] ./scra.py .. png jpg mp4")
    exit()
elif len(sys.argv) == 2:
    print("[ERROR>] File types not listed")
    print("[Usage>] ./scra.py <target_directory> <file_types>")
    print("[e.g. >] ./scra.py .. png jpg mp4")
    exit()

#Prepare dump-scrapy folder
os.system("rm -rf ./dump-scrapy")
os.system("mkdir ./dump-scrapy")

#Directories
source_dir = sys.argv[1]
dest_dir = "./dump-scrapy"

filetypes = []
showtypes = "[scra.py>] Scraping for"
for spectyp in sys.argv[2:]:
    filetypes += spectyp
    showtypes += " "+spectyp
showtypes += " files..."

print(showtypes)

f_found = 0
for i in filetypes:
    itech="**/*."+i
    files = glob.glob(itech, recursive=True)
    for file in files:
        if os.path.isfile(file):
            print("# "+file)
            shutil.copy(file, dest_dir)
            f_found += 1

if f_found == 0:
    print("[scra.py>] No files were scraped!")