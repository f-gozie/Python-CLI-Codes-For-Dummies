import sqlite3

con = sqlite3.connect('population.db')
cur = con.cursor()

# CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)

# cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')
# cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
# cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
# cur.execute('INSERT INTO PopByRegion VALUES("Northern Africa", 1037463)')
# cur.execute('INSERT INTO PopByRegion VALUES("Southern Asia", 2051941)') 
# cur.execute('INSERT INTO PopByRegion VALUES("Asia Pacific", 785468)')
# cur.execute('INSERT INTO PopByRegion VALUES("Middle East", 687630)')
# cur.execute('INSERT INTO PopByRegion VALUES("Eastern Asia", 1362955)')
# cur.execute('INSERT INTO PopByRegion VALUES("South America", 593121)')
# cur.execute('INSERT INTO PopByRegion VALUES("Eastern Europe", 223427)')
# cur.execute('INSERT INTO PopByRegion VALUES("North America", 661157)')
# cur.execute('INSERT INTO PopByRegion VALUES("Western Europe", 387993)')
# cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')
# con.commit()
cur.execute('SELECT Region FROM PopByRegion WHERE Population > 1000000 AND Region > "L"')
# cur.execute('DROP TABLE PopByRegion')

content = cur.fetchall()
# print(content)
the_file = open("Databases.txt",'a')

for whatever in content:
# 	the_file.write(str(whatever[0] + "	  " + str(whatever[1])) + '\n')
	print(whatever)