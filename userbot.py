from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel
import config

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

if __name__ == '__main__':
    client.loop.run_until_complete(main())