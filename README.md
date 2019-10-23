# filetracker.py

Remember that time when you have a bunch of files in a folder that you forgot, and now you see a file in a new location that might actually be the same file in that folder that you forgot...
Worry not! Because this silly little program will help you keep track of the files you already have and where they were.

So easy:
1. Copy filetracker.py to where ever you want it
2. Enter $ python3 filetracker.py \<directory-with-new-files\> \<tracker-file\>

```
$ python3 filetracker.py foo/ bar.txt
```

If all filenames are new, then it just shows how many files you are keeping track.

```
$ python3 filetracker.py ../tmp/ inventory
File count: 3
```

If there are files with names that already exist, they won't be added to the tracker-file. Instead, their filename and previous location will be shown

```
$ python3 filetracker.py ../tmp/ inventory
Duplicated: file1.jpg @ ../tmp/
Duplicated: file2.txt @ ../tmp/
Duplicated: file3.csv @ ../tmp/
File count: 3
```

The tracker-file is just a tab-delimited file containing a list of the filenames and their directory path

```
$ more inventory
file1.jpg	../tmp/
file2.txt	../tmp/
file3.csv	../tmp/
```
