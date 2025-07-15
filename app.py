from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api.fast-creat.ir/sms"
API_KEY = "1807093505:gKP98hHmnoGXTx0@SenatorApiBot"
TEMPLATE_ID = "1610182413"

@app.route("/send-otp", methods=["POST"])
def send_otp():
    data = request.json
    phone = data.get("phone")
    code = data.get("code")

    if not phone or not code:
        return jsonify({"success": False, "message": "Phone or code missing"}), 400

    params = {
        "apikey": API_KEY,
        "type": "private",
        "code": code,
        "phone": phone,
        "template": TEMPLATE_ID
    }

    response = requests.get(API_URL, params=params)

    try:
        result = response.json()
    except:
        result = response.text

    return jsonify({"success": True, "api_response": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
