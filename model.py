from sqlite3 import Error

def createTables(conn):
  sql = """CREATE TABLE IF NOT EXISTS jobs(
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nombre VARCHAR(255) NOT NULL,
  fecha_orden DATE,
  fecha_prevista DATE,
  fecha_entrega DATE NOT NULL
  );
  """

  try:
    c = conn.cursor()
    c.execute(sql)
    c.close()
  except Error as e:
    print(e)

    
