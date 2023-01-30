import pyodbc
import csv

cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                      "SERVER=192.168.1.151;"
                      "DATABASE=MSF_iSearch_DB;"
                      "UID=botadmin;"
                      "PWD=P@ssw0rd")


cursor = cnxn.cursor()
cursor.execute("SELECT * FROM MSF_iSearchDB")

# Save the result to a CSV file
with open('your_table.csv', 'w', newline='') as f:
    writer = csv.writer(f,delimiter=';',
      lineterminator='\n',
      quotechar='|',
      quoting=csv.QUOTE_MINIMAL)
    writer.writerow([i[0] for i in cursor.description])
    writer.writerows(cursor)

# Close the connection
cursor.close()
cnxn.close()
