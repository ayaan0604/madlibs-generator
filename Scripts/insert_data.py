from extract_story_data import *
import sqlite3
import json

db=sqlite3.connect("data/madlibs.db")


#function to get all the stories as a list of strings
def get_all_stories():
    storyNames=getFileNames(path="stories")
    stories=[]
    for story in storyNames:
        storyPath="stories/"+story
        with open(storyPath,"r",encoding="utf-8") as f:
            text=f.read()
            stories.append(text)
        
    return stories

#returns data as a list of dictionaries as {storyText:string,placeholders:list,wordCount:int}
def get_all_story_data():
    storiesRawText=get_all_stories()

    data=[]
    
    for rawText in storiesRawText:
        data.append(getStoryData(rawText))

    return data


def insert_story_data_to_database(storyData:dict):
    query='''INSERT INTO madlib_stories(story_text,placeholders,word_count)
            VALUES(?,?,?)'''

    text=storyData["storyText"]
    placeholders=json.dumps(storyData["placeholders"])
    words=storyData["wordCount"]
    cur=db.cursor()
    cur.execute(query,(text,placeholders,words))
    db.commit()
    cur.close()
    


if __name__=="__main__":
    for data in get_all_story_data():
        insert_story_data_to_database(data)
    