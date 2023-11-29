from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    return render_template('index.html', dog_image=data['message'])

if __name__ == '__main__':
    app.run(debug=True)
