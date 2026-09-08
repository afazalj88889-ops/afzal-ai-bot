"""
Render.com free tier par bot ko chalane ke liye chhota wrapper.
Render sirf "web service" free mein deta hai, isliye hum ek chhota
web page bana rahe hain jo bot ko background mein chalata hai, aur
koi bahar wali service (UptimeRobot) isay har 5 min mein "ping"
karti rahegi taake ye kabhi so na jaye.
"""

import threading
from flask import Flask
from afzal_ai_bot import run_forever, CONFIG

app = Flask(__name__)


@app.route("/")
def home():
    return "Afzal AI Bot is running! 🤖"


def start_bot_in_background():
    thread = threading.Thread(target=run_forever, args=(CONFIG,), daemon=True)
    thread.start()


start_bot_in_background()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
