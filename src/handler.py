# a module for all of the major program processing, including all interactions with the DB
import sqlite3, json
con = sqlite3.connect("data/osfss.db")
cur = con.cursor()
#TODO: write function for reading sqlite db and returning the data efficiently

#TODO: write function for updating sqlite db (check for malicious or incorrect requests)

#TODO: write function for reading/writing favorites json
