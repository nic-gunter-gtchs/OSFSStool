# a module for all of the major program processing, including all interactions with the DB
import sqlite3, json

letterlkup = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
con = sqlite3.connect("data/osfss.db")
cur = con.cursor()
qdb = cur.execute("SELECT name FROM sqlite_master WHERE name='acro'")
if qdb.fetchone() is None:
  cur.execute("CREATE TABLE acro(shd, extd, dfn, art)")
  for n, l in enumerate(letterlkup): #TODO: cleanup spaghetticode
    for u, e in enumerate(letterlkup):
      for m, t in enumerate(letterlkup):
        cur.execute("INSERT INTO acro VALUES ("+str(l)+str(e)+str(t)+",'','','')")

#TODO: write function for reading sqlite db and returning the data efficiently
def grabDB(include_short=False, subject=None):
  form = {}
  if include_short:
    form["short"] = []
  form["names"] = []
  form["defs"] = []
  form["links"] = []
  for row in cur.execute("SELECT shd, extd, dfn, art FROM acro"):
    if include_short:
      form["short"].append(row[0])
    form["names"].append(row[1])
    form["defs"].append(row[2])
    form["links"].append(row[3])
  if subject is not None and include_short:
    locs = [i for i, data in enumerate(form["short"]) if data == subject]
    form["names"] = [form["names"][i] for i in locs]
    form["defs"] = [form["defs"][i] for i in locs]
    form["links"] = [form["links"][i] for i in locs]
  return form
    
#TODO: write function for updating sqlite db (check for malicious or incorrect requests)

#TODO: write function for reading/writing favorites json
