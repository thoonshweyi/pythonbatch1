# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler,MessageHandler,  filters

# from databaseconfig import dbconnect
# import mysql.connector
# from mysql.connector import Error
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Conversation States
# FULLNAME,EMAIL = range(2)

# # Ask for FULLNAME
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#      await update.message.reply_text("Welcome! Please enter your Full Name: ")
#      return FULLNAME

# # Temp Save FULLNAME and Ask for EMAIL
# async def fullname(update: Update, context: ContextTypes.DEFAULT_TYPE):
#      context.user_data["fullname"] = update.message.text
#      await update.message.reply_text("Great! Please enter your Email: ")
#      return EMAIL

# async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
#      context.user_data["email"] = update.message.text
#      user_fullname = context.user_data["fullname"]
#      user_email = context.user_data["email"]

#      insert_sql = "INSERT INTO employees (fullname,email) VALUE (%s,%s)"
#      value_sql = (user_fullname,user_email)

#      # INSERT into Mysql
#      conn = dbconnect()

#      if conn.is_connected():
#           cursor = conn.cursor() # Get a cursor

#           try:
#                cursor.execute(insert_sql,value_sql)
#                conn.commit()
#                await update.message.reply_text(f'Thank you {user_fullname}! You are now registered.')
#                print(f"Data Inserted, ID is {cursor.lastrowid}")
#           except Error as e:
#                await update.message.reply_text(f"An unexpected error: {e}")
#           finally:
#                cursor.close()
#                conn.close()
#      else:
#           await update.message.reply_text("Database connection error!")
     
#      return ConversationHandler.END


# # Cancel command "/cancel"
# async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
#      await update.message.reply_text("Registration canceled!")
#      return ConversationHandler.END

# def main():
#      app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
#      conv_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states={
#           FULLNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND,fullname)],
#           EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND,email)],
#         },
#         fallbacks=[CommandHandler("cancel", cancel)],
#      )
     
#      app.add_handler(conv_handler)
#      print("Bot is running ....", flush=True)
#      app.run_polling()

# if __name__ == "__main__":
#      main()



from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler,MessageHandler,  filters

from databaseconfig import dbconnect
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

# Conversation States
FULLNAME,EMAIL = range(2)

# Ask for FULLNAME
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text("Welcome! Please enter your Full Name: ")
     return FULLNAME

# Temp Save FULLNAME and Ask for EMAIL
async def fullname(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data["fullname"] = update.message.text
     await update.message.reply_text("Great! Please enter your Email: ")
     return EMAIL

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data["email"] = update.message.text
     user_fullname = context.user_data["fullname"]
     user_email = context.user_data["email"]

     # check if username is missing or blank
     # if not fullname or fullname.strip() == "":
     #      await update.message.reply_text('Full Name cannot be empty! Please restart with /start and enter a value full name.')
     #      return ConversationHandler.END
     
     # if not email or email.strip() == "":
     #      await update.message.reply_text('Email cannot be empty! Please restart with /start and enter a valid email')
     #      return ConversationHandler.END

     insert_sql = "INSERT INTO employees (fullname,email) VALUE (%s,%s)"
     value_sql = (user_fullname,user_email)

     # INSERT into Mysql
     conn = dbconnect()

     if conn.is_connected():
          cursor = conn.cursor() # Get a cursor

          try:
               cursor.execute(insert_sql,value_sql)
               conn.commit()
               await update.message.reply_text(f'Thank you {user_fullname}! You are now registered.')
               print(f"Data Inserted, ID is {cursor.lastrowid}")
          except mysql.connector.IntegrityError as e:
               # check if it's a duplicate entry error
               if e.errno == 1062:
                    await update.message.reply_text(f"That email already exists. Please try again with a different one. ")
               else:
                    await update.message.reply_text(f"Database error: {e}")
          except Error as e:
               await update.message.reply_text(f"An unexpected error: {e}")

          finally:
               cursor.close()
               conn.close()
     else:
          await update.message.reply_text("Database connection error!")
     
     return ConversationHandler.END


# Cancel command "/cancel"
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text("Registration canceled!")
     return ConversationHandler.END

def main():
     app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
     conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
          FULLNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND,fullname)],
          EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND,email)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
     )
     
     app.add_handler(conv_handler)
     print("Bot is running ....", flush=True)
     app.run_polling()

if __name__ == "__main__":
     main()

