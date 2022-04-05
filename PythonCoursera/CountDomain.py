
#count the number of email messanger per organization(i.e domain name of email addfress)

import sqlite3
conn = sqlite3.connect('count.sqlite')
cur = conn.cursor()

cur.execute('drop table if exists Counts')
cur.execute('create table counts(org text, count integer)')
fname = input('Enter file name: ')
if len(fname)< 1:
    fname = 'mbox.txt'
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    else:
        word = line.split()
        word1 = word[1].split('@')
        domain = word1[1]
        cur.execute('select * from counts where org = ?', (domain, ))
        row = cur.fetchone()
        if row is None:
            cur.execute('insert into counts values(?, 1)', (domain, ))
        else:
            cur.execute('Update counts set count = count + 1 where org = ? ', (domain, ))
    conn.commit()