from flask import Flask, render_template, request, session, redirect, url_for
from chatbot import predict_class, get_response
import json, random, csv
# import request
from sentiment_analysis import get_emotion

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'Abhyoday'

intents = json.loads(open("intents.json", encoding="utf8").read())

chat_history = []
suggestion_list = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    global suggestion_list
    def random_songs(emotion):
        with open('../Spotify-Machine-Learning/data/data.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            json_list = []
            for row in reader:
                json_list.append(dict(row))
        classified_data = {
            'Calm': [],
            'Happy': [],
            'Sad': [],
            'Energetic': []
        }

        for obj in json_list:
            mood = obj['mood']
            classified_data[mood].append(obj)
        
        if emotion == "joy":
            suggestion_list = random.sample(classified_data['Energetic'], 10)
        elif emotion == "happy":
            suggestion_list = random.sample(classified_data['Happy'], 10)
        elif emotion == "sad":
            suggestion_list = random.sample(classified_data['Sad'], 10)
        elif emotion == "disgust":
            suggestion_list = random.sample(classified_data['Calm'], 10)
        elif emotion == "fear":
            suggestion_list = random.sample(classified_data['Calm'], 10)
        return suggestion_list
    if request.method == 'POST':
        message = request.form["message"]
        print(message)
        ints = predict_class(message)
        res = get_response(ints, intents)
        emotion = get_emotion(message)
        suggestion_list = random_songs(emotion)
        temp = {"res": res, "emotion": emotion}
        chat_history.append({"req": message, "res": res})
        return redirect(url_for('chatbot'))

    return render_template('chatbot_template.html', chat_history=chat_history, suggestion_list=suggestion_list)
#     # return json.dumps(temp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
