import sqlite3
conn = sqlite3.connect('email.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts') # Xoa bang Counts neu da co san tron database
cur.execute('CREATE TABLE Counts(email TEXT, count INTEGER)') # Tao bang Counts

fname = input("Enter file name: ")
if len(fname)<1:
    fname = 'mbox-short.txt'

fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    else:
        word = line.split()
        email = word[1]
        cur.execute('SELECT count from counts where email = ?', (email, ))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT into counts(email, count) values(?, 1)', (email, ))
        else:
            cur.execute('Update counts set count = count+1 where email = ?', (email, ))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
