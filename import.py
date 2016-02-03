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
				passwd = "Temp123",
				db="bugdata"
			)
	x = conn.cursor()

	# Load data into memory
	och = load_data_from_csv('../data/och.csv')
	habitat = load_data_from_csv('../data/habitat.csv')

	# NOTE: inserting into site table
	for row in habitat:
		state 		 = row['State:Installation'].split(':')[0].strip()
		installation = row['State:Installation'].split(':')[1].strip()
		drainage 	 = str(row['Drainage']).strip()
		mtnRange 	 = row['MtnRange'].strip()
		name 		 = str(row['Site']).strip()

		x.execute("SELECT * FROM app_sitemodel WHERE name =\""+name+"\"")
		existing = x.fetchall()
		if not existing:
			try:
				x.execute("""INSERT INTO app_sitemodel (state, installation, drainage, mountain_range, name) VALUES (%s, %s, %s, %s, %s)""", (state, installation, drainage, mtnRange, name))
				conn.commit()
			except:
				conn.rollback()
		else:
			print str(existing[0][0])

	## NOTE: inserting into sample table
	for row in habitat:
		site			= "NULL" if str(row['Site']).strip() == 'nan' else str(row['Site']).strip()
		sample_name		= "NULL" if str(row['Sample Code with Date']).strip() == 'nan' else str(row['Sample Code with Date']).strip()
		date			= "NULL" if str(row['Years'])+'-01-01' == 'nan' else str(row['Years'])+'-01-01'
		subsite			= "NULL" if str(row['Subsite']).strip() == 'nan' else str(row['Subsite']).strip()
		microhabitat	= "NULL" if str(row['Microhabitat']).strip() == 'nan' else str(row['Microhabitat']).strip()
		sample_hydro	= "NULL" if str(row['SampleHydro']).strip() == 'nan' else str(row['SampleHydro']).strip()
		habitat_size	= "NULL" if str(row['Habitat Size']).strip() == 'nan' else str(row['Habitat Size']).strip()
		zone			= "NULL" if str(row['Zone']).strip() == 'nan' else str(row['Zone']).strip()
		utm_easting		= "NULL" if str(row['UTM Easting']).strip() == 'nan' else str(row['UTM Easting']).strip()
		utm_northing	= "NULL" if str(row['UTM Northing']).strip() == 'nan' else str(row['UTM Northing']).strip()

		x.execute("SELECT * FROM app_sitemodel WHERE name =\""+site+"\"")
		existing = x.fetchall()
		if existing:
			site_key = int(existing[0][0])
			try:
				x.execute("""INSERT INTO app_samplemodel (date, subsite, microhabitat, sample_hydro, habitat_size, zone, utm_easting, utm_northing, site_id, sample_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (date, subsite, microhabitat, sample_hydro, habitat_size, zone, utm_easting, utm_northing, site_key, sample_name))
				conn.commit()
			except:
				conn.rollback()
		else:
			print "could not find site named: " + site

	## NOTE: inserting into subsample table
	for row in och:
		sample_id 		= "NULL" if str(row['Sample ID']).strip() == 'nan' else str(row['Sample ID']).strip()
		order			= "NULL" if str(row['Order']).strip() == 'nan' else str(row['Order']).strip()
		family			= "NULL" if str(row['Family']).strip() == 'nan' else str(row['Family']).strip()
		genus			= "NULL" if str(row['Genus/sub-genus']).strip() == 'nan' else str(row['Genus/sub-genus']).strip()
		sub_genus       = "NULL"
		species			= "NULL" if str(row['Species']).strip() == 'nan' else str(row['Species']).strip()
		taxa			= "NULL" if str(row['Taxa']).strip() == 'nan' else str(row['Taxa']).strip()
		total_count		= "NULL" if str(row['Total Counts']).strip() == 'nan' else str(row['Total Counts']).strip()

		x.execute("SELECT * FROM app_samplemodel WHERE sample_name =\""+sample_id+"\"")
		existing = x.fetchall()

		if existing and taxa != 'NO OCH PRESENT':
			sample_id = int(existing[0][0])
			try:
				x.execute("""INSERT INTO app_subsamplemodel(order_name, family, genus, sub_genus, species, taxa, total_count, sample_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", (order, family, genus, sub_genus, species, taxa, total_count, sample_id))
				# x.execute("INSERT INTO app_subsamplemodel (order, family, genus, sub_genus, species, taxa, total_count, sample_id) VALUES (\""+order+"\", \""+family+"\", \""+genus+"\", \""+sub_genus+"\", \""+species+"\", \""+taxa+"\", "+str(total_count)+", "+str(sample_id)+")")
				conn.commit()
			except MySQLdb.Error, e:
				print e
				conn.rollback()
		else:
			print "count not find: " + sample_id

if __name__ == '__main__':
	main()
