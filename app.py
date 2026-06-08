from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hellow guys,i am learing flask!"
app.run(debug=True)