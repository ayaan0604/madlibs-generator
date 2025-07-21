import sqlite3, json
import random


def get_connection():
    return sqlite3.connect("data/madlibs.db")

#returns a dictionary of a random story {id,text,placeholders}
def get_random_story():
    connection=get_connection()
    cur=connection.cursor()
    randomId=random.randint(1,28)

    query='''SELECT id, story_text, placeholders
            FROM madlib_stories 
            WHERE id=?
            LIMIT 1'''
    
    cur.execute(query,(randomId,))
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
        story=story.replace("_"," ")
        story=story.replace("{"+key+"}",value)
    
    return story

def get_placeholder_names(placeholders:list):
    names=[]
    for placeholder in placeholders:
        current=placeholder["placeholder"].replace("_"," ")
        names.append(current)
    #removing duplicates
    names=list(set(names))
    
    return names

