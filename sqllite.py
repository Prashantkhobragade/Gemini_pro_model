import sqlite3 

#connect to SQlite

connection = sqlite3.connect('student.db')

#create cursor object to insert record, create table
cursor = connection.cursor()

#create the table
table_info = """
CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25));
"""
cursor.execute(table_info)

##Insert some record

cursor.execute('''Insert Into STUDENT values('John', 'Data Science', 'A')''')
cursor.execute('''Insert Into STUDENT values('Abram', 'Data Science', 'B')''')
cursor.execute('''Insert Into STUDENT values('Neha', 'Data Analyst', 'A')''')
cursor.execute('''Insert Into STUDENT values('Kabir', 'MLOps', 'A')''')
cursor.execute('''Insert Into STUDENT values('Rana', 'Data Analyst', 'B')''')
cursor.execute('''Insert Into STUDENT values('Katil', 'MLOps', 'B')''')

##Display all records
print("The inserted records are: ")
data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)
    
    
connection.commit()
connection.close()