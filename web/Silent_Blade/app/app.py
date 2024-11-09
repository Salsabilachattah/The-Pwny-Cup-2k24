#!/usr/bin/env python2

from flask import Flask
from flask import render_template, render_template_string
from flask import request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["GET"])
def submit():
    try:
        template = """ <html>
             <h1> Ah yes, you qualified to PwnyCup Finals! I remember you! Hello {}   </h1>     
        </html>
        """.format(request.args.get('value'))

    except KeyError:
        return "Hey! Stop fooling around!"
 
    filter_regex = r"_|config|os|RUNCMD|base|import"


    if re.search(filter_regex, template):
        return "Trying to be a hacker? We don't do that here, you are not allowed to use :- _ ,base,config ,RUNCMD, os"


    return render_template_string(template)