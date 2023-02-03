
import pandas as pd
import json
import sqlite3

con = sqlite3.connect("database.db")
df = pd.read_sql_query("SELECT * from table_name", con)

json_data = df.to_json()
print(json_data)

con.close()

def get_db(table_name):
    # filter table content
    return  df