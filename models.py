import sqlite3, json


def get_connection():
    return sqlite3.connect("data/madlibs.db")

#returns a dictionary of a random story {id,text,placeholders}
def get_random_story():
    connection=get_connection()
    cur=connection.cursor()

    query='''SELECT id, story_text, placeholders
            FROM madlib_stories 
            ORDER BY RANDOM()
            LIMIT 1'''
    
    cur.execute(query)
    result=cur.fetchone()
    cur.close()
    connection.close()

    return {
        "id":result[0],
        "text":result[1],
        "placeholders":json.loads(result[2])
    }

def get_story_by_id(id):

    connection=get_connection()
    cur=connection.cursor()

    query='''SELECT id,story_text, placeholders
            FROM madlib_stories 
            WHERE id=?'''
    
    cur.execute(query,(id,))
    result=cur.fetchone()
    cur.close()
    connection.close()

    return {
        "id":result[0],
        "text":result[1],
        "placeholders":json.loads(result[2])
    }



def fill_story(story:str,inputs:dict):
    for key,value in inputs.items():
        story=story.replace("{"+key+"}",value)
    
    return story

