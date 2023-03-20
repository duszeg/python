#That's exeptional code which I'll fill with real db data
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="Database"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM yourtable")
result = mycursor.fetchall()
import subprocess

# Specify the path where you want to save the exported database file
output_path = 'F:/DataBaseExport'

# Construct the mysqldump command
command = f"mysqldump -u {root} -p{1234} {Database} > {output_path}"

# Execute the command
subprocess.call(command, shell=True)

mydb.close()


