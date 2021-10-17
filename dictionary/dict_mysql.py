

import sys
import mysql.connector

conn = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = conn.cursor()
user_input = input("Enter a word: ")
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % user_input )
results = cursor.fetchall()
#print(results)
#print(type(results))

if results:
    for result in results:
        print(result[1])
else:
    print("No word found")

# query = cursor.execute("SELECT * FROM Dictionary")