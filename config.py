from os import environ 

class Config:
    API_ID = environ.get("API_ID", "8284356")
    API_HASH = environ.get("API_HASH", "b0f3696af7e07918d6b1852fdf726432")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7524230814:AAHbNRz-0trIiQ_giW_zKUf4HAHxgiPX9dk") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://WZMLX:WZMLX@cluster0.r9zqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1955934378').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
