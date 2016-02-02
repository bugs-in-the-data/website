##
# Install numpy and pandas!!
#
# 
##
import numpy as np
import pandas as pd


def load_data_from_csv(filename):
	table = pd.read_table(filename, sep='\t')
	return table.to_records()


def main():
	# Load data into memory
	och = load_data_from_csv('../data/och.csv')
	habitat = load_data_from_csv('../data/habitat.csv')
	# Example usage of numpy arrays:
	for row in och:
		print row['Order'], row['Family']

if __name__ == '__main__':
	main()
