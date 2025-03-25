from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
import requests

def send_telegram_notification(message: str):
    """Mengirim notifikasi ke Telegram (placeholder)."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    body = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, body)
    print(message)

def log(message: str):
    print(message)
    # Simpan data ke file (opsional)
    with open("webhook_logs.txt", "a") as file:
        file.write(message + "\n")