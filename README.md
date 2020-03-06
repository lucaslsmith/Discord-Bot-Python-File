# Discord Bot Python File - Uses discord.py
This is a Python file that I wrote for a Discord bot using the discord.py module. The bot accepts user commands and also performs different server related functions. This is the only file that you will need in order to get your bot running on a server. All you have to do is add your bot token at the bottom of the file. If you do not already have a Discord bot created, please see the first set of instructions below. If you do already have a bot created and just want to add the Python file, please see the second set of instructions.

---HOW TO CREATE A BOT---
1. Go to the Discord website. https://discordapp.com/
2. Navigate to the Developer Portal which is listed under the Developers tab.
3. Create a new application and give it a name. This will be the name of your bot.
4. After the new application has been created, open the bot tab listed in the settings and select Add Bot.
5. You will be given a warning that once you turn the application into a bot, it cannot be changed back.
6. A list of bot permissions will be added below and you can select whatever you would like. Administrator permissions will give the bot access to just about anything that you can think of. This ensures that if we give the bot a command that requires Administrator permissions, it will be able to execute the command without any problems.
7. Select the OAuth2 tab and click the box labeled "bot" so that we can generate an invite link for your bot.
8. A link will appear below, copy and paste it into your address bar to invite the bot. You will be prompted to select which server you would like the bot to join. Select a server and click authorize. 
9. The bot is now an official member of your server. You can update and manage the bot from the Developer Portal, but any commands or functions that you set for the bot will need to be modified in your Python file.
10. This is the final and most important step! The bot tab has a spot under the username that is labeled as TOKEN. Copy this token and paste it into the Python file at the bottom where it says to input your token. This is how the Python file interacts with your bot and server. Without it, the bot just sits there in an idle state and cannot do anything specified in the Python file.

---USING THE PYTHON FILE WITH YOUR BOT---
You must have the discord.py module installed for this to work! You can find installation instructions at the link below... https://discordpy.readthedocs.io/en/latest/intro.html#installing

1. Ensure that your bot token has been added to the very bottom of the Python file where it says client.run('TOKEN GOES HERE').
2. Once you run the Python file, it will tell you in the terminal that your bot is online. Once you see that message appear, the bot can now do everything that is defined within the Python file.
3. Simply stop running the file to have your bot go offline.
4. Comments have been added throughout the code to ensure that you have a better understanding of how to modify the file and personalize it for your own server.

---COMMANDS AND BOT FUNCTIONS---
To give a command, the user must enter the prefix for commands and follow it with a command that is listed in the Python file. I have the prefix set to "bot." but you can change this to whatever works best for you. All it does is separate normal chatter from the commands so the bot knows when to reply. The currently defined commands are listed below.

bot.twitter - For demonstration purposes, this links users to my Twitter account. You can change this command name from .twitter to something else if you want to link users to another website. Also be sure to change the actual link to wherever you want this command to take the user.

bot.check - Returns the response time of commands.
bot.question - Gives an answer to questions that users can ask. This is in 8-ball format.
bot.joke - Tells a joke.
bot.compliment - Gives the requesting user a compliment.
bot.goodbye - Gives the user a special goodbye message if they enter this command before leaving.
bot.hello - Greets the user whenever they use this command.
bot.fact - Gives a fact.
bot.news - Tells the user about any important news that you have listed.
bot.info - Returns information about the bot and gives a list of commands.

There are plenty of comments to help guide you while making changes to the file and personalizing the bot. There are a few other non-command functions that the bot can do, such as automatically updating its status or printing to the terminal whenever someone joins/leaves the server so that you can keep track of these changes without seeing the rest of the chatter. 
