# Bsky Autoshare with images
This is a simple script to share images to Bsky from a folder. It will automatically share the images to Bsky. 
It will share skeets in order of skeets in json file. If all is done, then it will pick random skeet from list and share it.You can add main.py to crontab to run it every hour with `python3 main.py` command. An example crontab entry is `0 * * * * python3 /path/to/main.py` which will run the script every hour. 

Also there is a tool named add.py which will take skeet and image url as argument and it will download image and give it a unique name, then it will add skeet and image to json file. 

You can also add manual records to json file.

## Requirements
- Python 3
- Pipenv 

## Installation
- Clone the repository
- Copy .env.dist to .env and add your Bsky username and password
- Run `pipenv install` to install dependencies
- Run `pipenv shell` to activate virtual environment
- Run `python3 add.py "skeet" "image_url"` to add skeet and image to json file
- Run `python3 main.py` to share your first skeet

