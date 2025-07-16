
"""
Notes:
placeholders are in json format. Formatting is required while retrieving

"""


import sqlite3

db=sqlite3.connect("data/madlibs.db")
dbCursor=db.cursor()

query="""CREATE TABLE IF NOT EXISTS madlib_stories(
    id INTEGER PRIMARY KEY,
    story_text TEXT,
    placeholders TEXT,
    word_count INTEGER)"""

if __name__=="__main__":
    dbCursor.execute(query)