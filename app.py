from flask import Flask,render_template
import requests
import json
app = Flask(__name__)



@app.route('/')
def hello_world():
    r1 = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text&text=?")
    text_data = r1.text
    r2 = requests.get("https://official-joke-api.appspot.com/random_joke")
    json_data = json.loads(r2.text)
    joke = json_data.get('setup')
    punchline = json_data.get('punchline')
    return render_template("index.html", text_data=text_data, joke=joke, punchline=punchline)



if __name__ == '__main__':
    app.run(debug=True)
