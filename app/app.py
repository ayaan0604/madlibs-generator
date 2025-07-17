from flask import Flask,render_template,request
import models


app=Flask(__name__)
app.config['DATABASE']="data/madlibs.db"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fill",methods=["GET"])
def fill():
    if request.method=="GET":
        story=models.get_random_story()   
        id=story["id"]
        placeholders=story["placeholders"]
        placeholderNames=models.get_placeholder_names(placeholders)
        
        return render_template("fill.html",id=id,placeholderNames=placeholderNames)

   

@app.route("/result",methods=['GET',"POST"])
def result():
    if request.method=="POST":
        data=dict(request.form)
        id=data["id"]
        story=models.get_story_by_id(id)["text"]
        del data["id"]
        filledStory=models.fill_story(story=story,inputs=data)
        return render_template("result.html",story=filledStory)


if __name__=="__main__":
    app.run(debug=True)