import discord
import random
import webbrowser
from discord.ext import commands, tasks
from itertools import cycle

###############################################################################  IMPORTANT!!!  ################################################################################################
#Everything is explained in great detail whenever something is used for the first time. After that, the notes on each command are more of a general explanation as a reminder.
#You will still need to create a bot through the Discord Developer Portal, however, if you put the bot token from YOUR bot into this file, you can use all of these commands for your own bot.
#The commands are listed right after "def" and are followed with parenthesis. Command aliases can also be used and will be pointed out whenever they come up in the code commands listed below.
#And again... please ensure that YOUR bot token is added at the very bottom of this file to ensure that your bot is able to use these commands.
###############################################################################################################################################################################################

#This enforces a required prefix to execute commands. You can alter the command prefix below and make it whatever you want. Right now, it looks something like this... bot.commandgoeshere.
client = commands.Bot(command_prefix = 'bot.') #Change the word 'bot' to your new prefix!

#This alters the "PLAYING" status to make it look like the bot is doing different things. It does not actually mean anything, it just gives the bot some personality.
status = cycle(['Reading The Paper', 
                'Self Optimization',
                'Having a Snack',
                'Recording a Mixtape',
                'Following Accounts',
                'Sending Spam',
                'Dwarf Fortress',
                'Sipping Coffee',
                'Cleaning Up',
                'Recharging',
                'Mowing The Lawn',
                'Caves of Qud',
                'Washing Dishes',
                'Cooking a Meal',
                'Baking Cookies',
                'Trimming The Hedges',
                'Watching Netflix',
                'Coding',
                'Solving a Rubiks Cube',
                'Arguing Online',
                'Browsing Reddit',
                'Sending a Tweet',
                'Watching YouTube',
                'Games With TASBOT'
                'Arguing With Alexa',
                'Super Mario Maker 2']) #These are a list of potential statuses for the bot and can be changed to whatever you want them to be.

#This tells you in the terminal whenever the bot comes online.
@client.event
async def on_ready():
    change_status.start()
    print ('Bot is now online.') #This can be changed to anything. It is completely optional but is useful incase the bot takes a while to load.

#This automatically launches your web browser and takes you to a website. I have it linked to my Twitter, but this can be changed to anything. You can make as many of these commands as you want.
@client.command()
async def twitter(ctx): #twitter is the command that will be used to execute (prefix.twitter).
    await webbrowser.open("https://twitter.com/lucaslsmith") #Change this to your desired link. 

#This throws an error when an invalid command is entered. An invalid command is anything that is not specified in your code.
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used') #Error message. This can be changed to anything.

#This determines how often the bot's status will change. This directly relates to the playing cycle at the top.
@tasks.loop(seconds=5) #How often the status changes. This can be changed to minutes, hours, etc. It is set to 5 seconds for the purpose of seeing how the cycle works.
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#This will display in the terminal whenever a member joins the server. It is completely optional but can sometimes be useful if you want to see a list of who all has joined recently.
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

#This will display in the terminal whenever a member leaves the server. It is completely optional but can sometimes be useful if you want to see a list of who all has left recently.
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

#This displays the response time of the bot and ensures that it can respond to commands. This is not essential, however it can be a useful tool.
@client.command()
async def check(ctx):
    await ctx.send(f'speed = {round(client.latency * 1000)}ms')

#This is a game that lets users ask the bot a question and it will respond in the "8-ball" format. Players will also have to ask questions in the correct format or the 
# responses will not make any sense. The format must go as follows... prefix.question QUESTION GOES HERE ON THE SAME LINE BEFORE SENDING.
@client.command(aliases=['8ball', 'questions']) #These are alternate commands that will yield the same results. You can add/change them to whatever you want them to be.
async def question(ctx, *, question): #This is the command that will be used to execute (prefix.question). The aliases listed above will also work.
    responses = ['Yes.',
                 'Probably.',
                 'Without a doubt.',
                 'Most definitely.',
                 'You can rely on it.',
                 'Yes, I see it.',
                 'Most likely.',
                 'The outlook is good.',
                 "I don't know.",
                 'I would rather not say...',
                 'What do you think?',
                 'Ask someone else.',
                 'Things will be fine! Oh wait, nevermind...',
                 'Signs point to you.',
                 'Not sure, try again.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'Definitely not.',
                 'No chance.',
                 'Very doubtful.',
                 'No.']
    await ctx.send(f'{random.choice(responses)}') #This allows for a random response to the question by choosing one of the listed responses at random.

#This tells the user how to correctly enter a question if they make a mistake. By design, the question comes directly after the command on the same line before sending.
@question.error
async def question_error(ctx, error):
    await ctx.send('Please type in the command and then ask a question on the same line before sending.') #This will be the bot's response if a question is not provided before sending.

#This will return a random joke that the bot has readily available.
@client.command(aliases=['jokes', 'funny', 'tellmeajoke']) #As you saw earlier, here are more aliases that can be used in place of the default command.
async def joke(ctx): #This is the command that will be used to execute (prefix.joke).
    jokes =     ['Why do we tell actors to break a leg? Because every film has a cast.',
                 'Why do we not eat clocks? Because it is very time consuming.',
                 'Did you hear about the guy who stole a calendar? He got twelve months.',
                 'I woke up this morning and forgot which side the sun rises on, then it dawned on me.',
                 'I will never buy velcro again. What a rip-off!',
                 'I recently sold my vacuum. All it did was collect dust.',]
    await ctx.send(f'{random.choice(jokes)}') #Just like before, this returns a random choice from the list of jokes.

#This will give the user a compliment.
@client.command(aliases=['nice', 'compliments', 'makemyday', 'benice', 'friendly']) #Aliases that can be used instead of the default command.
async def compliment(ctx): #This is the command that will be used to execute (prefix.compliment).
    compliments =['You are looking great today!',
                 'Woah! Looking good!',
                 'I hope you are doing well!',
                 'You are awesome!',
                 'If I had a galactic credit for every time I thought you were awesome, I would be rolling in the intergalactic dough.', #Just a little bit of extra quirkiness added.
                 'You are so cool!',
                 'Great to see you!',
                 'I wish I was as cool as you!',
                 'Woah! Are those new pants?', #Again, just adding some personality here. Please, feel free to change these to whatever you want.
                 'I wish the other bots were more like you.']
    await ctx.send(f'{random.choice(compliments)}') #Returns a random compliment from the compliments list.

#When the user is leaving they can use this command to get a goodbye from the bot.
@client.command(aliases=['bye', 'goodbyes', 'byebye', 'seeyoulater']) #Aliases that can be used instead of the default command.
async def goodbye(ctx): #This is the command that will be used to execute (prefix.goodbye).
    goodbyes =  ['See you later!',
                 "Bye friend!",
                 "See you soon!",
                 'Until next time!',
                 'Goodbye!',
                 'Catch you later!',
                 "Wait! Don't go!",
                 'It was good having you!']
    await ctx.send(f'{random.choice(goodbyes)}') #More random choices being generated.

#Much like the goodbye command, this one will greet the user whenever they give the hello command.
@client.command(aliases=['greeting', 'greetings', 'howdy', 'greet']) #Aliases that can be used instead of the default command.
async def hello(ctx): #This is the command that will be used to execute (prefix.hello).
    greetings =  ['Howdy partner!',
                 "Hello friend!",
                 "Good to have you!",
                 'Yay! I was hoping you would show up.',
                 'Hey there!',
                 "What's up?",
                 "Now it's a party!",
                 'Heddooh!', #This means hello in Huttese.
                 'My best friend!']
    await ctx.send(f'{random.choice(greetings)}') #Randomly picks from the list of greetings.

#This command will give the user a random fact. These are all facts that were pulled from the internet so if you intend to use this bot or this command in a serious setting, please do
#some more research to ensure the validity of the facts that are being provided. These were chosen for example purposes and might not be entirely true.
@client.command(aliases=['facts', 'tellmesomething', 'somethingcool', 'coolfact', 'didyouknow', 'tellfact', 'interesting']) #Aliases that can be used instead of the default command.
async def fact(ctx): #This is the command that will be used to execute (prefix.fact).
    facts =     ['Doritos are flamable.',
                 'The average person will spend 4 months of their life sitting at red lights.',
                 "You can hear a blue whale's heartbeat from 2 miles away.",
                 'Sears used to sell houses.',
                 'Your funny bone is actually the Ulnar nerve.',
                 "Captain Crunch's real name was Horation Magellan Crunch.",
                 'This "?!" is called an interrobang.',]
    await ctx.send(f'{random.choice(facts)}') #This randomly selects a fact from the list of facts.

#This will give information related to bot commands. You can remove my information and change the text to match your commands.
@client.command(aliases=['aboutbot', 'whoareyou', 'botinfo']) #Aliases that can be used instead of the default command.
async def info(ctx): #This is the command that will be used to execute (prefix.botinfo).
    await ctx.send("""This is a Discord bot that is designed to directly interact with users. The bot has a specified list of recognized commands that can be used at any time.
    bot.twitter - Links users to my twitter account or any website that you choose to add instead.
    bot.check - Returns the response time of commands.
    bot.question - Gives an answer to questions that users can ask. This is in 8-ball format.
    bot.joke - Tells a joke.
    bot.compliment - Gives the requesting user a compliment.
    bot.goodbye - Gives the user a special goodbye message if they enter this command before leaving.
    bot.hello - Greets the user whenever they use this command.
    bot.fact - Gives a fact.
    bot.news - Tells the user about any important news that you have listed.
    bot.info - Returns information on the bot and gives a list of commands.""")

#This displays any news that you might have for the members of a server.
@client.command(aliases=['updates', 'whats new', 'new stuff']) #Aliases that can be used instead of the default command.
async def news(ctx): #This is the command that will be used to execute (prefix.news).
    await ctx.send("1. Discord bot is currently undergoing maintinence.") #This is the news that you want to share. You can add multiple lines of text to display more information.


###############################################################################  IMPORTANT!!!  ################################################################################################
#This is your token that will be used to connect the bot's commands to your bot in the server.
#Please ensure that whenever you create a bot in the Discord Developer Portal, you copy the token in the Bot tab and paste it below.
###############################################################################################################################################################################################

client.run('TOKEN GOES HERE') #Do not share this token!!!

