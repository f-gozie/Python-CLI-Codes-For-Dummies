import sqlite3

con = sqlite3.connect('Users.db')
cur = con.cursor()

# CREATE TABLE Users(UserName TEXT, Password TEXT, BankBalance INTEGER)
# cur.execute('CREATE TABLE Users(UserName TEXT, Password TEXT, BankBalance INTEGER)')
# cur.execute('INSERT INTO Users VALUES("Ose", "iyoke", 20000)')
# cur.execute('INSERT INTO Users VALUES("misi","wonder", 3546)')

con.commit()
cur.execute('SELECT * FROM Users')
# cur.execute('DROP TABLE Users')
content = cur.fetchall()
print(content)
