from flask import Flask, request, jsonify
from helper import send_telegram_notification

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json  # Mengambil data JSON dari request
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400
        
        # Log data yang diterima
        print("Received webhook:", data)
        
        # Simpan data ke file (opsional)
        with open("webhook_logs.txt", "a") as file:
            file.write(str(data) + "\n")
        
        # Tambahkan logika pemrosesan di sini jika diperlukan
        send_telegram_notification(str(data))
        return jsonify({"status": "success", "message": "Webhook received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
