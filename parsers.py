"""Util functions for parsing files
"""
import numpy as np
def parse_soft(fn):
	# A function to parse soft files
	# fn: string, path/filename of the soft file
	dataset = open(fn, 'r')
	lines = []
	# Iterate over every line in the file, storing it in the list.
	for line in dataset:
		lines.append(line)
	# Remove metadata
	idx = lines.index('!dataset_table_begin\n')
	lines = lines[idx+1:]
	# Remove the newline character and split on the tab.
	lines = [line[:-1].split('\t') for line in lines]
	# Remove the first element from every list.
	header = lines[0] # [ID_REF,IDENTIFIER, sample, ...]
	samples = header[2:]
	lines = lines[1:] # skip header
	genes = [] # to store genes 
	mat = [] # to store the gene expression values a list of lists [[val1, val2, ...], [], ...]
	for line in lines:
		if 'null' in line or '--Control' in line:
			continue
		if len(line) != len(header):
			continue
		gene = line[1].upper() # convert gene to uppercase
		# Convert each expression value from string to float
		values = map(float, line[2:]) # expression values of a gene across samples
		# values = [float(value) for value in line[1:]] # equivalent list comprehension
		genes.append(gene)
		mat.append(values)
	# Close the files.
	dataset.close()
	# convert the list of list to a numpy 2d-array for each data manipulations
	mat = np.array(mat)
	return mat, genes, samples

