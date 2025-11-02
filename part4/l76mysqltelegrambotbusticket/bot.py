from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler,MessageHandler,  filters

from databaseconfig import dbconnect
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Conversation States
BUS,SEAT = range(2)

# Ask for CLASS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
     reply_keyboard = [[ "Yangon Express", "Mandalay Express" ]]
     markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
     await update.message.reply_text("Welcome! Choose your bus: ",reply_markup=markup)
     return BUS

# Temp Save BUS and Ask for SEAT
async def getbus(update: Update, context: ContextTypes.DEFAULT_TYPE):
     bus = update.message.text
     context.user_data["bus"] = bus

       # INSERT into Mysql
     conn = dbconnect()

     if conn.is_connected():
          cursor = conn.cursor(dictionary=True) # Get a cursor

          try:
               cursor.execute("SELECT seatno,status FROM seats WHERE busname = %s",(bus,))
               rows = cursor.fetchall()

               display = ""
               for row in rows:
                    if row['status'] == 'idle':
                         display += f"🟩 {row['seatno']} "
                    else:
                         display += f"🟥 {row['seatno']} "
                    
                    if row['seatno'].endswith('2') or row['seatno'].endswith('4') or row['seatno'].endswith('6') or row['seatno'].endswith('8'):
                         display += "\n"

               
               await update.message.reply_text(f"*{bus}* Seating Plan :\n\n{display}\n\nChoose your seat number(eg. A1):")
               return SEAT
                          
          except Error as e:
               await update.message.reply_text(f"An unexpected error: {e}")
          finally:
               cursor.close()
               conn.close()
     else:
          await update.message.reply_text("Database connection error!")
     

# Temp Save SEAT and inserto to DB
async def getseat(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data["seatno"] = update.message.text.upper()
     user = update.effective_user
     
     user_bus = context.user_data["bus"]
     user_seatno = context.user_data["seatno"]

     update_sql =   '''
          UPDATE seats SET status="occupied",user_id=%s,username=%s,booked_at=%s
          WHERE busname=%s AND seatno=%s
     '''
     value_sql = (user.id,user.username,datetime.now(),user_bus,user_seatno)

    
     # INSERT into Mysql
     conn = dbconnect()

     if conn.is_connected():
          cursor = conn.cursor(dictionary=True) # Get a cursor
          
          select_sql = "SELECT * FROM seats WHERE busname=%s AND seatno=%s"
          cursor.execute(select_sql,(user_bus,user_seatno))
          seat = cursor.fetchone()

          try:
               if not seat:
                    await update.message.reply_text("Invalid seat number! ")
               elif seat["status"] == "occupied":
                    await update.message.reply_text("That seat is already taken. Please choose another! ")
               else:
                    cursor.execute(update_sql,value_sql)
                    conn.commit()
                    await update.message.reply_text(f"Seat {user_seatno} booked successfully, {user.username}")
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
          BUS: [MessageHandler(filters.TEXT & ~filters.COMMAND,getbus)],
          SEAT: [MessageHandler(filters.TEXT & ~filters.COMMAND,getseat)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
     )
     
     app.add_handler(conv_handler)
     print("Bot is running ....", flush=True)
     app.run_polling()

if __name__ == "__main__":
     main()

