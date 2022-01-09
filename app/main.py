import sys
import logging
import json
import urllib.request as requests
import urllib.parse
import os
from flask import Flask
from flask import request

app = Flask(__name__)

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info("SUCCESS Lambda Function Started")


def build_telegram_packet(message):
    telegram_bot_id = os.getenv("BOT_ID")
    chat_id = os.getenv("GROUP_ID")

    url = "https://api.telegram.org/bot" + telegram_bot_id + "/sendmessage"

    data = {"chat_id": chat_id, "text": message}

    return url, data


# executes upon API event
@app.route("/notify", methods=["POST"])
def recv():
    dl_name = request.form["name"]
    url, data = build_telegram_packet(dl_name)

    req = requests.Request(url)
    req.add_header("Content-Type", "application/json")
    response = requests.urlopen(req, json.dumps(data).encode("utf-8"))

    return {"statusCode": 200}
