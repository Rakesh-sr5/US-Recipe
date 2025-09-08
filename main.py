# -*- coding: utf-8 -*-
"""securin assessment

Original file is located at
    https://colab.research.google.com/drive/1LtGEAlDXJPklmDC3pbWflHWWOpGh_zsA
"""

# Parsing the file
import json
import numpy
import pandas
File = open('US_recipes_null.Pdf.json')

recipes = json.load(File)
df = pandas.DataFrame(recipes)
df.head()

df = df.transpose()
df.head()

#finding Nan values
df.isna().sum()

#Replacing Nan values with NULL
df.replace(numpy.nan,'NULL',inplace=True)
df.isna().sum()

#creating a database
import sqlite3
c = sqlite3.connect('s.db')
cursor = c.cursor()
q1 = '''CREATE TABLE recipes(
  cuisine TEXT,
  title VARCHAR,
  rating FLOAT,
   prep_time INT,
   cook_time INT,
    total_time INT,
     description TEXT,
serves VARCHAR);
'''

cursor.execute(q1)
print("THE DATABASE IS SUCCESSFULLY CREATED")

new_df = df[['cuisine','title','rating','prep_time','cook_time','total_time','description','serves']]
new_df

for row in new_df.values:
  cursor.execute("INSERT INTO recipes VALUES(?,?,?,?,?,?,?,?)", row)

cursor.execute("SELECT * FROM recipes")
#retriving 10 recipes
cursor.fetchmany(10)

