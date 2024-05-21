import os
import sys
import requests
import json
import uuid

def download_image(url, folder):
    # Generate a unique filename
    filename = str(uuid.uuid4()) + ".jpg"
    filepath = os.path.join(folder, filename)
    
    # Download the image
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
        sys.exit(1)
    
    return filename

def update_skeets_json(skeet:str, image_filename:str=''):
    # Define the path to the JSON file
    json_file = 'skeets.json'
    
    # Load existing data
    if os.path.exists(json_file):
        with open(json_file, 'r',encoding="utf-8") as file:
            skeets = json.load(file)
    else:
        skeets = []

    # Add new skeet
    new_skeet = {
        "skeet": skeet
    }

    if(image_filename != ''):
        new_skeet["image"] = image_filename

    skeets.append(new_skeet)
    
    # Save updated data
    with open(json_file, 'w',encoding="utf-8") as file:
        json.dump(skeets, file, ensure_ascii=False, indent=4)

def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: python add.py <skeet> [<url>]")
        sys.exit(1)
    
    skeet = sys.argv[1]

    if(len(sys.argv) == 2):
        url = ''
    else:
       url = sys.argv[2]

    if(url != ''):
        # Ensure the images directory exists
        images_folder = 'images'
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
        
        print("Image is downloading...") 
        # Download the image and get the filename
        image_filename = download_image(url, images_folder)
        
        # Update the JSON file
        update_skeets_json(skeet, image_filename)
    else:
        update_skeets_json(skeet)
    
    print("skeet and image saved successfully.")

if __name__ == "__main__":
    main()

