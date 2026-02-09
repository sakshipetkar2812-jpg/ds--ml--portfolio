import mysql.connector
import pandas as pd
import numpy as np

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="7984455774sak",
    database="employee"
)
cursor=conn.cursor()
print("connected to database")

# step_9: Fetch employee details based on emp_rating

queries={
    "Less than 2":"SELECT EMP_ID,FIRST_NAME, DEPT, EMP_RATING FROM emp_record_table Where EMP_RATING<2;",

    "Greater than 5":"SELECT EMP_ID, FIRST_NAME,DEPT, EMP_RATING FROM emp_record_table Where EMP_RATING>4;",

    "between 2 and 4": "SELECT EMP_ID,FIRST_NAME, DEPT, EMP_RATING FROM emp_record_table Where EMP_RATING BETWEEN 2 AND 4;",
} 

for condition,query in queries.items():
    cursor.execute(query)
    rows=cursor.fetchall()
    print(f"\nEmployees with EMP_RATING {condition}:")
    print("EMP_ID,FIRST_NAME, DEPT, EMP_RATING FROM")
    print("-"*60)
    for row in rows:
        print("|".join(map(str,row)))


# step_10: Fetch and concate FIRST_NAME and MIDDLE_NAME as NAme
cursor.execute(""" SELECT CONCAT(FIRST_NAME," ",LAST_NAME) AS NAME FROM emp_record_table WHERE DEPT='Finance';
""")
rows=cursor.fetchall()
print("\n Employess in Finance deparment")
print("NAME")
print("-"*60)
for row in rows:
    print(row[0])

# step_11: Close MYsql connection
cursor.close()
conn.close()
print("All tasks completed")