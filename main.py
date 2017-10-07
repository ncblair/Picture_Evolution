from flask import Flask, render_template, request

app = Flask(__name__)

from helpers import *

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/newImg', methods=['POST'])
def newImgReq():
    ###CALL MAIN.PY ON DEFAULT PARAMS###
    imageReturned = main()
    return render_template('newImg.html', image = imageReturned)