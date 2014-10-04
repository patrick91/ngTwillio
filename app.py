from __future__ import unicode_literals

import twilio.twiml

from flask import Flask, request

import yo

from api import convert_text


app = Flask(__name__)

yo_client = yo.Yo('asdasdas')


@app.route("/", methods=['GET'])
def hello():
    return str('ngHello ngWorld')


@app.route("/sms", methods=['POST'])
def hello_ng():
    body = request.form.get('Body', 'no body').encode('utf-8').decode('utf-8', 'ignore')

    resp = twilio.twiml.Response()
    resp.message(convert_text(body))

    yo_client.yo()

    return str(resp)


@app.route("/yo", methods=['POST'])
def yo():

    return str('')

if __name__ == "__main__":
    app.run(debug=True)
