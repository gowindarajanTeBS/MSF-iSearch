
import pyodbc
import json

# Connect to the database
cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                      "SERVER=192.168.1.151;"
                      "DATABASE=MSF_iSearch_DB;"
                      "UID=botadmin;"
                      "PWD=P@ssw0rd")

# Select all rows from a table
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM MSF_iSearchDB")

# Fetch the result
result = cursor.fetchall()

# Get the column names
columns = [column[0] for column in cursor.description]

# Build the JSON object
json_data = []
for row in result:
    json_data.append(dict((column, str(value)) for column, value in zip(columns, row)))

# Save the JSON object to a file
with open('your_table.json', 'w') as f:
    json.dump(json_data, f)

# Close the connection
cursor.close()
cnxn.close()
