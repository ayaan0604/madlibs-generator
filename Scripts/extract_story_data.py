import os


def getFileNames(path):
    try:

        file_names=os.listdir(path)
        return file_names
    except Exception as e:
        print("File name not correct")

def getAStory():
    with open("stories/story_1.txt") as f:
        story=f.read()
        return story


#funtion to return the placeholders as list of dictionaris as {"placeholder":name, "start":startIndex, "end":endIndex}
def extract_placeholders(story):
    #list for all placeholders
    placeholders=[]

    #markers for start and end index of placeholder
    start=0
    end=0
    
    for currentidx in range(len(story)):
        if story[currentidx]=="{":
            start=currentidx
        
        if story[currentidx]=="}":
            end=currentidx
            placeholderData={"placeholder":story[start+1:end],
                             "start":start,
                             "end":end}
            placeholders.append(placeholderData)

    return placeholders


def getStoryWordCount(story):
    return len(story.split(" "))



#function for story metadata as a dictionary {storyText:string,placeholders:list,wordCount:int}
def getStoryData(story):
    storyData={}
    
    storyData["storyText"]=story
    storyData["placeholders"]=extract_placeholders(story=story)
    storyData["wordCount"]=getStoryWordCount(story)

    return storyData
