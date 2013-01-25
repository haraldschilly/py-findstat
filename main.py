#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/calc/<n>")
def calc(n):
    try:
        n = int(n)
        return "Thanks Harald " + str(4 * n)
    except:
        return 'error', 300


@app.route("/findstat/<n>/<k>")
def findstat_main(n, k):
    from sage.all_cmdline import Integer, factor
    n = factor(Integer(n) ** Integer(k))
    txt = "The result is: '%s'" % str(n)
    return render_template("home.html", text=txt)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug", help="enables flask's debug mode", action="store_true")
    args = parser.parse_args()

    options = {}
    options.update({'debug': args.debug})
    app.run(**options)
