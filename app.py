from flask import Flask, request, jsonify import requests import os
app = Flask(name)
BOT_TOKEN = os.environ.get("BOT_TOKEN") CHAT_ID = os.environ.get("CHAT_ID")
@app.route("/location", methods=["POST"]) def receive_location(): data = request.json
Python
latitude = data.get("latitude")
longitude = data.get("longitude")
accuracy = data.get("accuracy")

message = (
    "📍 New Location\n\n"
    f"Latitude: {latitude}\n"
    f"Longitude: {longitude}\n"
    f"Accuracy: {accuracy} meters\n\n"
    f"https://www.google.com/maps?q={latitude},{longitude}"
)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "text": message
    }
)

return jsonify({"success": True})
if name == "main": app.run(host="0.0.0.0", port=10000
