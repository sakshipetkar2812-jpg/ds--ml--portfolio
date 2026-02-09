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

#step-28: Find Employees with More Than 10 Years of Experience Using Nested Query 
cursor.execute(""" 
SELECT EMP_ID, FIRST_NAME, LAST_NAME, ROLE, EXP 
FROM emp_record_table 
WHERE EXP > (SELECT MIN(EXP) FROM emp_record_table WHERE EXP > 10); 
""") 
rows = cursor.fetchall() 

#step-29: : Display Results 
print("\nEmployees with More Than 10 Years of Experience:") 
print("EMP_ID | FIRST_NAME | LAST_NAME | ROLE | EXPERIENCE") 
print("-" * 60) 
for row in rows: 
    print(" | ".join(map(str, row))) 

# Step 30: Close MySQL Connection 
cursor.close() 
conn.close()