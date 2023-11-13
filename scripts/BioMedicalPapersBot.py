from telegram.ext import * #This means you import all from the module
from module import respond_to_query

TOKEN="YOUR-TOKEN-HERE"

async def start_commmand(update, context):
    await update.message.reply_text("INITIALIZATION MESSAGE HERE")


email="emailaddress@email.com" #Use a mock email address to access PubMed servers or provide a real one with email_command
maxresults=10

async def email_commmand(update, context): #provide a real email address to access PubMed servers
    text =  update.message.text
    a = text.replace("/email ", "")
    global email
    email=a
    await update.message.reply_text("EMAIL ADDRESS GOT")

async def maxnum_commmand(update, context): #provide a maximum number of results you want to see
    text =  update.message.text
    try:
        a = int(text.replace("/maxresults ", ""))
        global maxresults
        maxresults=a
        await update.message.reply_text("Awsome! Thanks for telling me how many results should I limit my search to!")
    except TypeError: #If the input provide is not an integer number
        await update.message.reply_text("Only integer values can be handled as maximum results number, setting the maximum to default value...")

async def query_command(update, context): #Pipe query into the function defined in module
    text =  update.message.text
    a=text.replace("/query ", "")
    str_container=respond_to_query(a, email, maxresults)
    await update.message.reply_text(str_container)



if __name__ == '__main__':
    print("My-bot is running") #Check the starting of the bot
    application = Application.builder().token(TOKEN).build() #Build the bot
    # Commands
    application.add_handler(CommandHandler('start', start_commmand))
    application.add_handler(CommandHandler('email', email_commmand))
    application.add_handler(CommandHandler('maxresults', maxnum_commmand))
    application.add_handler(CommandHandler('query', query_command))
    # Run bot
    application.run_polling(1.0)

##THE ACTUAL BOT CODE HAS ALSO HANDLERS THAT MANAGE NOT RECOGNIZED COMMAND OR THAT MAY BE USED TO ASK FOR INSTRUCTIONS ABOUT THE BOT; THEY ARE NOT REPORTED HERE FOR THE SAKE OF SIMPLICITY
