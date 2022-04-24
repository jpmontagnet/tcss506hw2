# TCSS 506 Spring 2022 - homework 2
# Student: JP Montagnet (jpmont)

from flask import Flask
from time import ctime

app = Flask(__name__)

@app.route("/")
def f_root():
    return "TCSS 506 - 2022 Springt - jpmont\n"

@app.route("/owner")
def f_owner():
    return "Hello world from JP Montagnet (jpmont)\n"

@app.route("/datetime")
def f_datetime():
    return f"{ctime()}\n"

app.run(host='0.0.0.0', debug=True)

# END
# vim: set ts=4 sw=4 expandtab :
