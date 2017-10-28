#!/usr/bin/env python

from PyPDF2 import PdfFileMerger, PdfFileReader
import os
import argparse

def valid_filenames (filenames):
	for filename in filenames:
		if not os.path.isfile(filename):
			print (filename)
			return False

	return True

def valid_output (output):
	return True

def merge_pdf (filenames, output):

	if (not (valid_filenames(filenames) and valid_output(output))):
		print(filenames)
		print(output)
		exit(1)
	

	merger = PdfFileMerger()
	for filename in filenames:
		merger.append(PdfFileReader(file(filename, 'rb')))

	print ("Writing to %s" % os.path.abspath(output))
	merger.write(output)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("filenames", nargs="+", help="List of paths to pdf files.")
	parser.add_argument("-o", "--output", help="Output filename", default="output.pdf")
	args = parser.parse_args()
	merge_pdf(args.filenames, args.output);