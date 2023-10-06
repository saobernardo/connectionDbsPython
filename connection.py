import sqlite3
from sqlite3 import Error

def createConnection(dbFile):
  conn = None
  try:
    conn = sqlite3.connect(dbFile)
  except Error as e:
    print(e)

  return conn