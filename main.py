from flask import Flask, render_template, request

from helpers import *

app = Flask(__name__)



@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/newImg', methods=['POST'])
def newImgReq():
    ###CALL MAIN.PY ON DEFAULT PARAMS###
    engine()
    return render_template('newImg.html')


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
