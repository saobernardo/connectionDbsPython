import connection
import model

conn = connection.createConnection("db.sqlite")

model.createTables(conn)