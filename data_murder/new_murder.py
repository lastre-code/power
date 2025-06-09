import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Conexión a SQLite
sqlite_conn = sqlite3.connect("sql-murder-mystery.db")

# Conexión a MySQL
password = quote_plus("Grace07431*")
mysql_engine = create_engine(f"mysql+pymysql://root:{password}@localhost/murder")

# Obtener las tablas de SQLite
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", sqlite_conn)

# Transferir cada tabla a MySQL
for table_name in tables["name"]:
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", sqlite_conn)
    df.to_sql(table_name, mysql_engine, if_exists='replace', index=False)
    print(f"Tabla '{table_name}' exportada a MySQL correctamente.")

sqlite_conn.close()

