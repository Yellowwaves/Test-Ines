import os
import random
import requests

MESSAGES = [
    "You make every day brighter ❤️",
    "I hope you have an amazing day my love ❤️",
    "Thinking about you always makes me smile ❤️",
    "You are my favorite person in the world ❤️",
    "I can't wait to see you again ❤️",
    "I'm lucky to have you ❤️",
    "You make everything better ❤️",
    "Just a reminder that I love you ❤️",
    "You mean everything to me ❤️",
    "I hope today brings you happiness ❤️"
]

SIGN = "aries"  # modifier selon son signe

try:
    horoscope = requests.get(
        f"https://ohmanda.com/api/horoscope/{SIGN}/",
        timeout=10
    ).json()["horoscope"]
except Exception:
    horoscope = "Today is full of possibilities."

message = random.choice(MESSAGES)

notification = (
    f"{message}\n\n"
    f"✨ Horoscope:\n"
    f"{horoscope}"
)

payload = {
    "app_id": os.environ["ONESIGNAL_APP_ID"],
    "included_segments": ["Subscribed Users"],
    "headings": {
        "en": "❤️ Good Morning ❤️"
    },
    "contents": {
        "en": notification
    }
}
print(payload)
response = requests.post(
    "https://api.onesignal.com/notifications",
    headers={
        "Authorization": f"Key {os.environ['ONESIGNAL_API_KEY']}",
        "Content-Type": "application/json"
    },
    json=payload
)

print(response.status_code)
print(response.text)