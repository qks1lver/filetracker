#!/usr/bin/env python3

#
# Copyright (C) 2018 Jiun Y. Yen
#
# This is a free program. You can redistribute and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Fundation
#
# This is distributed with hope of being useful. No warranty of any kind what-so-ever.
#
# Have fun!
#
# Instruction:
#	1. Copy this to where ever you want
#	2. Enter $ python3 filetracker.py <path of directory containing files to track> <filename to keep track of files>
#	i.e.
#		$ python3 filetracker.py foo/ bar.txt
#



# Imports
import os
import sys


# Functions
def compile_files(p_dir):

	"""
	Compile unique file names and duplicated file names

	:param p_dir: String, path of directory containing new files
	:return: A list, dir_paths, of directory paths, and a list, file_names, of file names with matching indices to
			dir_paths
	"""
	
	dir_paths = []
	file_names = []
	for d,_,f in os.walk(p_dir):
		dir_paths += [d]*len(f)
		file_names += f
	
	return(dir_paths,file_names)

def show_duplicated_files(dir_paths, file_names, p_dir):

	"""
	Display duplicated files and return the unique ones

	:param dir_paths: List, paths of directories that contains the files
	:param file_names: List, file names
	:param p_dir: String, path of the directory currently investigating
	:return: A list, dir_paths, of directory paths, and a list, file_names, of file names with matching indices to
			dir_paths with no duplicated file names
	"""

	data = ['%s>>>%s'%(x,y) for x,y in zip(file_names,dir_paths)]
	data.sort()
	file_names = []
	dir_paths = []
	
	f0,d0 = data.pop(0).split('>>>')
	file_names.append(f0)
	dir_paths.append(d0)
	while data:
		f1,d1 = data.pop(0).split('>>>')
		if f0.upper() == f1.upper():
			print('Duplicated: %s @ %s'%(f0,p_dir))
		else:
			file_names.append(f1)
			dir_paths.append(d1)
			f0 = f1
	
	return(dir_paths,file_names)

def write_files(dir_paths, file_names, p_out):

	"""
	Append to the file tracking text file

	:param dir_paths: List, paths of directories that contains the files
	:param file_names: List, file names
	:param p_out: String, path of the text file to keep track of all the files
	:return: Nothing
	"""
	
	with open(p_out, 'w+') as fi:
		for d,f in zip(dir_paths,file_names):
			fi.write('%s\t%s\n'%(f,d))
	
	return()

def read_list(p_in):

	"""
	Read the file tracking text file

	:param p_in: String, path of the text file to keep track of all the files
	:return: A list, dir_paths, of directory paths, and a list, file_names, of file names with matching indices to
			dir_paths
	"""
	
	with open(p_in, 'r') as f:
		file_names = []
		dir_paths = []
		for l in f:
			tmp = l.strip().split('\t')
			file_names.append(tmp[0])
			dir_paths.append(tmp[1])
	
	return(dir_paths,file_names)


# Main
if __name__ == "__main__":
	p_source = sys.argv[1]
	p_list = sys.argv[2]
	ds,fs = compile_files(p_source)
	if os.path.isfile(p_list):
		ds0,fs0 = read_list(p_list)
		ds += ds0
		fs += fs0
		ds,fs = show_duplicated_files(ds,fs,p_source)
	write_files(ds,fs,p_list)
	print('File count: %d'%len(fs))
