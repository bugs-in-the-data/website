##
# Install numpy and pandas!!
#
#
##
import numpy as np
import pandas as pd
import MySQLdb


def load_data_from_csv(filename):
	table = pd.read_table(filename, sep='\t')
	return table.to_records()


def main():
	conn = MySQLdb.connect(
				host = "localhost",
				user = "root",
				passwd = "Temp123",
				db="bugdata"
			)
	x = conn.cursor()

	# Load data into memory
	och = load_data_from_csv('../data/och.csv')
	habitat = load_data_from_csv('../data/habitat.csv')
	# Example usage of numpy arrays:
	# for row in och:
	# 	print row['Order'], row['Family']
	for row in habitat:
		# x.execute("""INSERT INTO app_sitemodel VALUES ())
		print "State: " + row['State:Installation'].split(':')[0].strip()
		print "Installation: " + row['State:Installation'].split(':')[1].strip()
		print "Drainage: " + str(row['Drainage']).strip()
		print "Mountain Range: " + row['MtnRange'].strip()
		print " "

if __name__ == '__main__':
	main()
