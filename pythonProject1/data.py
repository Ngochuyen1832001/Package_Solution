#Write a program in the python programming language using data from the datafile.txt.
#The result is saved to the database file dbFU.sqlite. Create the table with information:
#CREATE TABLE ProStatus (ProCode INTEGER, Deleted TEXT)
#The program prints the number of processed records, the first 5 rows of the table when sorted in descending order by ProjectCode.

import sqlite3

conn = sqlite3.connect('dbFU.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS ProStatus;
CREATE TABLE ProStatus(
    ProCode INTEGER, 
    Deleted TEXT
)
''')


fileX = open('datafile.txt')
count = 0

for line in fileX:
    line = line.rstrip()
    if count > 0:
        pro = line.strip(' ')[0]
        if 'Undelete' in line:
            status = 'N'
        else:
            status = 'Y'
        cur.execute('INSERT INTO ProStatus VALUES(?, ?)', (pro, status))
    count += 1
conn.commit()
fileX.close()

print(count - 1)
sqlstr = 'SELECT ProCode, Deleted FROM ProStatus ORDER BY ProCode DESC LIMIT 5'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
