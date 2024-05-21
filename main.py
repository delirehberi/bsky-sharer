import json
import random
import os
from atprototools import Session
from dotenv import load_dotenv

load_dotenv()

# Bluesky API credentials
USERNAME = os.getenv('BSKY_USERNAME')
PASSWORD = os.getenv('BSKY_PASSWORD')

# Path to JSON file
SKEETS_FILE = 'skeets.json'
INDEX_FILE = 'index.json'

# Authenticate to Bluesky
session = Session(USERNAME, PASSWORD)

def load_skeets():
    with open(SKEETS_FILE, 'r') as file:
        return json.load(file)

def save_index(index):
    with open(INDEX_FILE, 'w') as file:
        json.dump(index, file)

def load_index():
    if not os.path.exists(INDEX_FILE):
        return {'current_index': 0, 'shared': []}
    with open(INDEX_FILE, 'r') as file:
        return json.load(file)

def share_skeet(skeet:dict):
    try:
        #print all keys for skeet dict 
        if(skeet['image']): 
            session.postBloot(postcontent=skeet['skeet'],image_path=skeet['image'])
        else: 
            session.postBloot(postcontent=skeet['skeet'])

        print(f"Posted to Bluesky: {skeet['skeet']}")
    except Exception as e:
        print(f"Error posting to Bluesky: {e}")

def main():
    skeets = load_skeets()
    
    index_data = load_index()

    current_index = index_data['current_index']
    shared = index_data['shared']

    if current_index < len(skeets):
        skeet = skeets[current_index]
        index_data['current_index'] += 1
    else:
        skeet = random.choice(skeets)
        while skeet in shared:
            skeet = random.choice(skeets)
        index_data['shared'].append(skeet)

        if len(index_data['shared']) == len(skeets):
            index_data['shared'] = []
    print(skeet)
    share_skeet(skeet)
    save_index(index_data)

if __name__ == "__main__":
    main()

