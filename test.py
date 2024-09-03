from telegram.ext import *
from dotenv import load_dotenv
import os

print('Starting a bot....')
load_dotenv()
bot_token = os.getenv('HTTP_API_TOKEN')
     
async def start_commmand(update, context):
    await update.message.reply_text('Bot Alex dan Ryan')

if __name__ == '__main__':
    application = Application.builder().token(bot_token).build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))
    
    # Message Handler
    application.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Run bot
    application.run_polling(1.0)