from telethon import TelegramClient, events
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
import asyncio
import os
from dotenv import load_dotenv, set_key
from datetime import datetime, timedelta
import re


load_dotenv()

# Your API credentials
api_id = int(os.getenv('TELEGRAM_API_ID'))
api_hash = os.getenv("TELEGRAM_API_HASH")
phone_number = os.getenv("PHONE_NUMBER")
# Search parameters
SEARCH_TERM = 'python'  # Term to search for
NAME_PATTERN = r'^[A-Z][a-z]+\s[A-Z][a-z]+$'
LOG_FILE = "telegram_name_search_results.log"
async def list_chats():
    client = TelegramClient('session_name', api_id, api_hash)
    print("Connecting to Telegram...")
    await client.start()
    print("Listing all dialogs...")
    async for dialog in client.iter_dialogs():
        entity = dialog.entity
        if hasattr(entity, 'first_name'):
            username = f"@{entity.username}" if entity.username else "No Username"
            name = f"{entity.first_name} {getattr(entity, 'last_name', '')}"
            print(f"User: {name.strip()} ({username})")
        else:
            title = getattr(entity, 'title', 'Unknown')
            chat_id = entity.id
            print(f"Chat: {title} - ID: {chat_id}")
    
    count = 1
    await client.disconnect()
    is_connected = client.is_connected()
    print(f"{is_connected=}")
    while is_connected:
        print(f"attempting to disconnect. attempt {count}")
        await client.disconnect()
        count += 1
        await asyncio.sleep(1)
        is_connected = client.is_connected()
        print(f"{is_connected=}")
    print("Disconnected.")

def convert_to_datetime(offset):
    terms = offset.split('-')
    date_data = [int(term) for term in terms]
    return datetime(*date_data)

async def search(chat_id,pattern, size=1000, offset=None, batches=5):
    print("starting search function")
    # set offset
    last_offset = os.getenv("OFFSET")
    if not offset and last_offset:
        offset = convert_to_datetime(last_offset)
        
    # Create the client
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    print("client started")
    # Find the chat entity
    chat = await client.get_entity(chat_id)
    print("chat found")
    # Get Messages
    messages = await client.get_messages(
        chat,
        limit=size,
        offset_date=offset,
    )
    
    all_name_messages = []
    total_messages_checked = 0
    batch_number = 0
    
    with open(LOG_FILE, "a") as log:
        log.write(f"\n\n--- New Search: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        log.write(f"Starting point: {offset if offset else 'Most recent messages'}\n\n")
            
        # Loop to get messages in batches, going back in time
        while batch_number < batches:
            print(f"Fetching messages {total_messages_checked+1}-{total_messages_checked+size}" +
                (f" before {offset}" if offset else ""))
                
            # Get batch of messages using oldest_date as offset
            messages = await client.get_messages(
                chat,
                limit=size,
                offset_date=offset  # This gets messages before this date
                )
                
            if len(messages) < size or not messages:
                print("No more messages found or reached batch limit.")
                continue_search = False
                if not messages:
                    break
                
            total_messages_checked += len(messages)
                
                # Find name-only messages in this batch
            batch_name_messages = []
            for msg in messages:
                if msg.text and re.match(NAME_PATTERN, msg.text.strip()):
                    batch_name_messages.append(msg)
                    all_name_messages.append(msg)
                
                # Log the results from this batch
            log.write(f"Batch results (messages before {offset}):\n")
            for msg in batch_name_messages:
                date = msg.date.strftime('%Y-%m-%d %H:%M:%S')
                log.write(f"[{date}]: {msg.text.strip()}\n")
                
                # Update oldest_date to the timestamp of the oldest message in this batch
            offset = messages[-1].date
                
                # Update the .env file with the new offset date
                # Store as a string in format YYYY-MM-DD-HH-MM-SS
            offset_str = f"{offset.year}-{offset.month}-{offset.day}"
            set_key('.env', 'OFFSET', offset_str)
                
            print(f"Found {len(batch_name_messages)} name-only messages in this batch.")
            print(f"Total found so far: {len(all_name_messages)}")
            print(f"Oldest message checked: {offset.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Environment variable updated to continue from this point.")
            print("-" * 30)
                
            # Flush the log to disk
            log.flush()
                
                # Optional: add a small delay to avoid hitting rate limits
            await asyncio.sleep(1)
            batch_number +=1
            # Write summary to log
        log.write(f"\nSearch summary: Checked {total_messages_checked} messages total.\n")
        log.write(f"Total name-only messages found: {len(all_name_messages)}\n")
            
            # List unique names in the log
        unique_names = set(msg.text.strip() for msg in all_name_messages)
        log.write(f"\nUnique names found ({len(unique_names)}):\n")
        for name in sorted(unique_names):
            log.write(f"- {name}\n")
        
        # Display summary in console
    print(f"\nSearch complete! Checked {total_messages_checked} messages total.")
    print(f"Found {len(all_name_messages)} messages containing only a name.")
    print(f"Results have been saved to {LOG_FILE}")
    print(f"To continue the search later, run this script again.")
        
    print("messages retrieved")
    await client.disconnect()

if __name__ == '__main__':
    current_offset = datetime(2022,7,10)
    asyncio.run(search(chat_id=phone_number, pattern=NAME_PATTERN, size=500, batches=10))
    
