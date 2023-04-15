BonkBot 

This is a Discord bot for managing user registration for an Ark server for the Rise of Kingdoms mobile game. The bot responds to commands sent in Discord messages and keeps track of registered users for each server. 

  

Prerequisites 

Python 3.8+ 

discord.py library 

 

Setup 

Clone the repository and navigate to the directory. 

Install the required dependencies using pip:  

              pip install discord.py 

Replace the placeholder token in the last line of the code with your own bot token. You can create a Discord bot and obtain a token by following the instructions in the Discord Developer Portal. 

Run the bot 

  

Usage 

The bot listens for the following commands in Discord messages: 

  

!join: Registers the user for Ark by assigning them the "Ark Member" role and adding their name to the server's user list. 

!members: Displays the current list of registered users for Ark. 

!clear: Clears the list of registered users. Only users with administrator permissions can use this command. 

!leave: Removes the user from the list of registered users by removing their name from the server's user list and removing the "Ark Member" role. 

Note: Make sure the bot has the necessary permissions (e.g., to assign and remove roles) in the Discord server where it is added. 

  

Contributing 

Contributions are welcome! Please feel free to open an issue or submit a pull request if you find any issues or want to improve the bot. 

  

License 

This project is licensed under the MIT License. 
