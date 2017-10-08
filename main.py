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