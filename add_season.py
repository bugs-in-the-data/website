# Install numpy and pandas!!
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
				passwd = "",
				db="bugdata"
			)
	x = conn.cursor()

	# Load data into memory
	och = load_data_from_csv('../data/och.csv')
	habitat = load_data_from_csv('../data/habitat.csv')

	## NOTE: inserting into sample table
	for row in habitat:
		sample_name		= "NULL" if str(row['Sample Code with Date']).strip() == 'nan' else str(row['Sample Code with Date']).strip()
		season			= "NULL" if str(row['Season']).strip() == 'nan' else str(row['Season']).strip()

		try:
			query = "UPDATE app_samplemodel SET season = \"" + str(season) + "\" WHERE sample_name = \"" + str(sample_name) + "\""
			print query
			x.execute(query)
			conn.commit()
		except MySQLdb.Error, e:
			print e
			conn.rollback()


if __name__ == '__main__':
	main()
