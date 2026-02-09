import mysql.connector
import pandas as pd
import numpy as np

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="7984455774sak"
)
cursor =conn.cursor()
# step-6: fetch employee details
cursor.execute("""use employee""")
cursor.execute("""
SELECT EMP_ID,FIRST_NAME,LAST_NAME,GENDER,DEPT FROM emp_record_table;
""")
rows=cursor.fetchall()

#step-7: Display data into table form 
df=pd.DataFrame(rows,columns=["EMP_ID", "FIRST_NAME", "LAST_NAME",
"GENDER", "DEPARTMENT"])
print("\nemplyopee details:\n",df)

# step_8: Close MYsql connection
cursor.close()
conn.close()
print("All tasks completed")