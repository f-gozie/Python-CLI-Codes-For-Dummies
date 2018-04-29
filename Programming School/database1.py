import sqlite3

con = sqlite3.connect("census.db")
cur = con.cursor()

# CREATE TABLE Density(province TEXT, population INTEGER, land_area REAL)
# cur.execute('CREATE TABLE Density(province TEXT, population INTEGER, land_area REAL)')
# cur.execute('INSERT INTO Density VALUES("Newfoundland and Labrador", 512930, 370501.69)')
# cur.execute('INSERT INTO Density VALUES("Prince Edward Island", 135294, 5684.39)')
# cur.execute('INSERT INTO Density VALUES("Nova Scotia", 908007, 52917.43)')
# cur.execute('INSERT INTO Density VALUES("New Brunswick", 729498, 71355.67)')
# cur.execute('INSERT INTO Density VALUES("Quebec", 7237479, 1357743.08)')
# con.commit()
cur.execute('SELECT * FROM Density WHERE land_area > 200000')
contents = cur.fetchall()
print(contents)