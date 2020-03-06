import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS database (recipient_id, status) ")
c.execute("commit")
conn.close()

# Testing on terminal
user_id = input("what's your id?")
status = "2"
#status = random.choice(["1", "2", "3"])
table = (user_id,status)
conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS database (recipient_id, status) ")
c.execute("DELETE FROM database WHERE recipient_id = ? ", (user_id,))
a = c.execute("SELECT recipient_id, status from database")
print(a.fetchall())

c.execute("INSERT INTO database(recipient_id, status) VALUES (?, ?)",table)
c.execute("commit")

a = c.execute("SELECT recipient_id, status from database")
print(a.fetchall())





