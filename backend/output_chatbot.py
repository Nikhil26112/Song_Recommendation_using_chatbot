from flask import Flask, render_template, request, session, redirect, url_for
from chatbot import predict_class, get_response
import json
# import request
from sentiment_analysis import get_emotion

app = Flask(__name__)
app.secret_key = 'Abhyoday'

intents = json.loads(open("intents.json",encoding="utf8").read())

chat_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['GET','POST'])
def chatbot():
    if request.method == 'POST':
        message = request.form["message"]
        print(message)
        ints = predict_class(message)
        res = get_response(ints, intents)
        emotion = get_emotion(message)
        temp = {"res":res, "emotion":emotion}
        chat_history.append({"req":message,"res" : res})
        return redirect(url_for('chatbot'))
    return render_template('chatbot_template.html', chat_history=chat_history)
#     # return json.dumps(temp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
