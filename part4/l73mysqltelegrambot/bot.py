from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,   ConversationHandler

from databaseconfig import dbconnect
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
     user = update.effective_user
     insert_sql = "INSERT INTO telegramusers (user_id,first_name,username) VALUE (%s,%s,%s)"
     value_sql = (user.id,user.first_name,user.username)

     # INSERT into Mysql
     conn = dbconnect()
     if conn.is_connected():
          cursor = conn.cursor() # Get a cursor

          try:
               cursor.execute(insert_sql,value_sql)
               conn.commit()
               await update.message.reply_text(f'Thank you {user.first_name}! You are now registered.')
          except Error as e:
               await update.message.reply_text(f"An unexpected error: {e}")
          finally:
               cursor.close()
               conn.close()
     else:
          await update.message.reply_text("Database connection error!")
     
     return ConversationHandler.END

def main():
     app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
     app.add_handler(CommandHandler("start", start))
     app.run_polling()

if __name__ == "__main__":
     main()



# user_id
# first_name
# username