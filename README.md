# discord_CTF_archiver
This is a discord bot that archives a given channel category. Built for the messy discord of CTF teams.
Use with command : ```~archive <category_name>```
what it does basicaly : 
### Before: 
![image](https://user-images.githubusercontent.com/45575007/112208344-8b5a8080-8c18-11eb-8f70-03dbf606af1c.png)

### After: 
![image](https://user-images.githubusercontent.com/45575007/112208490-b0e78a00-8c18-11eb-835b-d4b77bb6fb71.png)


## pre-configuration :
Create a new file called ".env" looking like this :

    DISCORD_TOKEN=<the_bot_secret_token>
    DISCORD_GUILD=<guild/server name>
    ARCHIVE_CATEGORY_NAME=ARCHIVES

## Launch with commands : 
    pip3 install discord
    pip3 install python-dotenv
    python3 bot.py

## lauch with Docker :
    (from project folder)
    docker build . -t archiver
    docker run archiver

