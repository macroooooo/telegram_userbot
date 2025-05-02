from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel
import config
import threading
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define a simple route for Koyeb's health checks
@app.route('/')
def health_check():
    return "Userbot is running!"

# Initialize the Telegram client
client = TelegramClient('userbot_session', config.api_id, config.api_hash)

@client.on(events.NewMessage(chats=config.source_chat_id))
async def handler(event):
    # Copy the message to the destination group
    await client.send_message(config.destination_chat_id, event.message)

async def main():
    # Start the client
    await client.start(phone=config.phone_number)
    print("Userbot is running. Listening for messages...")
    # Keep the client running
    await client.run_until_disconnected()

# Function to run the Flask app
def run_flask():
    app.run(host='0.0.0.0', port=8000)

# Start Flask in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# Run the Telegram client
if __name__ == '__main__':
    client.loop.run_until_complete(main())