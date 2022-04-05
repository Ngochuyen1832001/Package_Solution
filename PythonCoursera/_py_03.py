import sqlite3

conn = sqlite3.connect("dbFPT.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS InFos;
''')

cur.execute('''
CREATE TABLE InFos(
    ProCode Integer PRIMARY KEY, 
    Deleted text)
''')

data_raw = open('datafile.txt')
line = 0
for i in data_raw:
    line = line + 1
    if line==1:
        continue
    i = i.rstrip()
    word = i.split()
    preCode = word[0]
    delete = word[3]
    cur.execute('''
        INSERT INTO InFos VALUES(?, ?)
    ''', (preCode, delete))

conn.commit()

# cur.execute('''
#     SELECT COUNT(*) FROM InFos
# ''')
# row = cur.fetchone()[0]
print("Number of processed records: ", line)
cur.execute('''
    SELECT * FROM InFos
    ORDER BY ProCode
    LIMIT 3
''')
A = cur.fetchall()
print("PreCode\tDelete")
for i in A:
    print(i[0], i[1], sep = '\t\t')

conn.close()