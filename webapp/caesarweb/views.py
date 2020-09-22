from flask import render_template
from caesarweb import app, cache, socketio
import sys
import os
sys.path.append(os.path.abspath("../"))
import caesar

@app.route('/')
@cache.cached()
def main():
    return render_template("main.html")

@socketio.on('new input')
def new_input(input_body):
    try:
        e = caesar.encrypt(input_body)
        emit('new encrypt', {'encrypt': e})
        d = caesar.decrypt(input_body)
        emit('new decrypt', {'decrypt': d})
    except:
        pass
