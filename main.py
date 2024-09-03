from telegram.ext import *
from dotenv import load_dotenv
import os
from modules import ChatBot

load_dotenv()
bot_token = os.getenv('HTTP_API_TOKEN')

RegexBot = ChatBot(
    botName='RegexBot',
)

print("starting the chat bot in telegram .......")

async def start_command(update, context):
    await update.message.reply_text(RegexBot.intro)

async def handle_message(update, context):
    user_message = update.message.text
    bot_response, character = RegexBot.reply(user_message)
    await update.message.reply_text(bot_response)

if __name__ == '__main__':
    application = Application.builder().token(bot_token).build()

    # Commands
    application.add_handler(CommandHandler('start', start_command))
    
    # Message Handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print(f"{character}: {bot_response}")

    # Run bot
    application.run_polling(1.0)
