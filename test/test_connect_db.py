import sqlite3

db = sqlite3.connect('../DB/TEST.db')
cursor = db.cursor()
print('Connect ok')

cursor.execute(
'''CREATE TABLE KCM
(ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
KEY TEXT NOT NULL,
VALUE TEXT NOT NULL);''')

#
# print('Table created.')
# db.commit()

# Insert
# cursor.execute('''INSERT INTO HUMAN (ID,NAME,AGE) VALUES (1, 'Clay', 25)''')
# cursor.execute('''INSERT INTO HUMAN (ID,NAME,AGE) VALUES (2, 'Wendy', 16)''')
# cursor.execute('''INSERT INTO KCM2 (KEY,VALUE) VALUES ('Clay', "25")''')
# cursor.execute('''INSERT INTO KCM (NAME,AGE) VALUES ('Wendy', 16)''')

#
# db.commit()
# print('Insert ok')

# Select
# results = cursor.execute('''SELECT * FROM KCM1 where key="Clay"''')
# for item in results:
#     print(item)

db.close()
