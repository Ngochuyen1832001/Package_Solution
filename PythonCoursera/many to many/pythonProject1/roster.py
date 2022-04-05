import json
import sqlite3

conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member
''')

cur.executescript('''
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
) ;

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
) ;

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
) 
''')
fname = input("Enter file name: ")
if (len(fname)<1):
    fname = 'roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)
for entry in json_data:
    name = entry[0];
    title = entry[1];
    role = entry[2]
    print(name, title, role)
    cur.execute('''
        Insert or Ignore into User(name) values(?)
    ''', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]
    cur.execute('''
            Insert or Ignore into Course(title) values(?)
        ''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''
        Insert or replace into Member(user_id, course_id, role) values(?, ?, ?)
    ''',(user_id, course_id, role))
    conn.commit()
