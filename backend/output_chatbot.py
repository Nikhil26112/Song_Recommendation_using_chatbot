from flask import Flask, render_template, request
from chatbot import predict_class, get_response
import json
# import request
from sentiment_analysis import get_emotion

app = Flask(__name__)

intents = json.loads(open("intents.json",encoding="utf8").read())
chat_history = []

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
    temp = {"res":res, "emotion":emotion}
    chat_history.append({"req":message,"res" : res})
    return json.dumps(temp)

@app.route('/chatbot', methods=['GET','POST'])
def loadChatbot():
    return render_template("chatbot_template.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
