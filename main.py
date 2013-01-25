#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/calc/<n>")
def calc(n):
    try:
        n = int(n)
        return "Thanks Harald "+str(4 * n)
    except:
        return 'error', 300

@app.route("/findstat/<n>/<k>")
def findstat_main(n,k):
    from sage.all_cmdline import sage_eval
    try:
        n = sage_eval("factor(Integer(%s)**%s)"%(n,k))
        return "How do I start Sage computations here?%s"%str(n)
    except:
        return 'error', 300

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="enables flask's debug mode", action = "store_true")
    args = parser.parse_args()

    options = {}
    options.update({'debug' : args.debug})
    app.run(**options)
