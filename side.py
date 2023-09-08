import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()
create = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY autoincrement, name VARCHAR(50), pass VARCHAR(50));'
cursor.execute(create)
conn.commit()

insert = 'INSERT INTO users (name, pass) VALUES (?, ?);'
values = [('name-1', 'pass-1'), ('name-2', 'pass-2'), ('name-3', 'pass-3')]

cursor.executemany(insert, values)
conn.commit()

select = 'SELECT * FROM users;'
cursor.execute(select)
results = cursor.fetchall()

print(results)
