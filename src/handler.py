# a module for all of the major program processing, including all interactions with the DB
import sqlite3, json

letterlkup = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
con = sqlite3.connect("data/osfss.db")
cur = con.cursor()
qdb = cur.execute("SELECT name FROM sqlite_master WHERE name='acro'")
if qdb.fetchone() is None:
  cur.execute("CREATE TABLE acro(shd, extd, dfn, art)
#TODO: write function for reading sqlite db and returning the data efficiently

#TODO: write function for updating sqlite db (check for malicious or incorrect requests)

#TODO: write function for reading/writing favorites json
