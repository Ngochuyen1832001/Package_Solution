import sqlite3

fu_db=sqlite3.connect("dbFPT.sqlite")
cur = fu_db.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Counts;
CREATE TABLE Counts(
    count INTEGER, 
    org TEXT
)
''')
fh = open("mbox.txt")
lt = list()
counts = dict()

for line in fh:
    if line.startswith("From") and len(line.split())>2
        mes=0
        temp=line.split()
        newtup=(temp[1], )
