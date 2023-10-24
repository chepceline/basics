import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(1, 'Damaris', 25, 'Juja', 50000.00)")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(2, 'Karani', 26, 'Thika', 55000.00)")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(3, 'Lopez', 27, 'Nairobi', 60000.00)")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(4, 'Brendah', 30, 'Mombasa', 65000.00)")

conn.commit()
print("Records created successfully")
conn.close

