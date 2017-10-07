#https://stackoverflow.com/questions/38070373/how-to-send-and-receive-http-post-requests-in-python

from flask import Flask, request


app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    print(request.form['foo']) # should display 'bar'
    return 'Received !' # response to your request.