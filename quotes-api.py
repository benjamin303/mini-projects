import requests
import mysql.connector
from datetime import datetime
import time

mydb = mysql.connector.connect(
    host='192.168.1.103',
    user='benjamin',
    password='benjamin',
    database='learning'
)
cursor = mydb.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS quotes (
    quote_id VARCHAR(50) PRIMARY KEY,
    content TEXT,
    author VARCHAR(100),
    tags TEXT,
    author_slug VARCHAR(100),
    length INT,
    date_added DATE,
    date_modified DATE
)
"""
cursor.execute(create_table_query)

for i in range(10):

    response = requests.get('https://api.quotable.io/random')
    data = response.json()

    quote_id = data['_id']
    content = data['content']
    author = data['author']
    tags = data['tags']
    author_slug = data['authorSlug']
    length = data['length']
    date_added = data['dateAdded']
    date_modified = data['dateModified']

    insert_query = """
    INSERT INTO quotes (quote_id, content, author, tags, author_slug, length, date_added, date_modified)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    quote_data = (quote_id, content, author, str(tags), author_slug, length, date_added, date_modified)
    cursor.execute(insert_query, quote_data)
    mydb.commit()

cursor.close()
mydb.close()






