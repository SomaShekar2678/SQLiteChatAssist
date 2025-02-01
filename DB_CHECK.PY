import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Check the Departments table data
cursor.execute("SELECT * FROM Departments")
rows = cursor.fetchall()

print("📌 Data in Departments Table:")
for row in rows:
    print(row)

conn.close()
