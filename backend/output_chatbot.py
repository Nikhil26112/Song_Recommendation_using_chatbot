from flask import Flask, render_template, request
from chatbot import predict_class, get_response
import json
# import request
from sentiment_analysis import get_emotion

app = Flask(__name__)

intents = json.loads(open("intents.json",encoding="utf8").read())


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/output', methods=['GET'])
def chatbot():
    message = request.args["message"]
    print(message)
    ints = predict_class(message)
    res = get_response(ints, intents)
    emotion = get_emotion(message)

    # return render_template("index.html", result=res, emotion=emotion)
    temp = {"res":res, "emotion":emotion}
    return json.dumps(temp)

@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":"28-04-2023", 
        "programming":"python"
        }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
