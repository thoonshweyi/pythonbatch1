from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler,MessageHandler,  filters
from databaseconfig import dbconnect
from datetime import datetime
from firebase_admin import credentials,firestore
from dotenv import load_dotenv
import os

load_dotenv()

# Conversation States
CLASS,STUDENTID,ATTCODE = range(3)

# collection name 
COLLECTION_NAME = "attendances"

# Ask for CLASS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
     reply_keyboard = [["Nodejs B1","Python B2","Reactjs B3","WDF 15"]]
     markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
     await update.message.reply_text("Please choose your class: ",reply_markup=markup)
     return CLASS

# Temp Save CLASS and Ask for STUDENTID
async def getclass(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data["class"] = update.message.text
     await update.message.reply_text("Enter your Student ID (eg. WDF1001): ")
     return STUDENTID

# Temp Save STUDENTID and Ask for ATTCODE
async def getstudentid(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data["studentid"] = update.message.text
     await update.message.reply_text("Enter your Attendance Code ID (eg. 12CB): ")
     return ATTCODE

# Temp Save ATTCODE and inserto to DB
async def getattcode(update: Update, context: ContextTypes.DEFAULT_TYPE):
     context.user_data["attcode"] = update.message.text
     user = update.effective_user

     user_class = context.user_data["class"]
     user_studentid = context.user_data["studentid"]
     user_attcode = context.user_data["attcode"]

     # INSERT into Firebase
     db = dbconnect()

     doc_ref = db.collection(COLLECTION_NAME).document() # Auto ID

     data = {
          "user_id": str(user.id),
          "class": user_class,
          "studentid": user_studentid,
          "attcode": user_attcode,
          "createdAt": firestore.SERVER_TIMESTAMP
     }

     try:
          doc_ref.set(data)
          await update.message.reply_text("Attendance recorded successfully.")

     except Exception as e:
          print("Error inserting attendance: ",e)
          await update.message.reply_text("Failed to record attendance.")
 
     return ConversationHandler.END

# Fetch own Data
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
     user = update.effective_user
     user_id = str(user.id)


     # Fetch Firebase
     db = dbconnect()
     col_ref = db.collection(COLLECTION_NAME)

     try: 
          query =  (
               col_ref
               .where("user_id","==",user_id)
               .order_by("createdAt",direction=firestore.Query.DESCENDING)
               .stream()
          )

          records = [doc.to_dict() for doc in query ]

          if records:
               message = "Your Attendance Records: \n\n"

               for record in records:
                    message += (
                         f"Class: {record.get('class')}\n"
                         f"Student ID: {record.get('studentid')}\n"
                         f"Attendance Code: {record.get('attcode')}\n"
                         f"Date: {record.get('createdAt')}\n\n"
                    )
          else:
               message = "No attendance records found!"

          await update.message.reply_text(message)

     except Exception as e:
          print("Error fetching attendance: ",e,flush=True)
          await update.message.reply_text("Failed to fetch attendance records.")

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
          CLASS: [MessageHandler(filters.TEXT & ~filters.COMMAND,getclass)],
          STUDENTID: [MessageHandler(filters.TEXT & ~filters.COMMAND,getstudentid)],
          ATTCODE: [MessageHandler(filters.TEXT & ~filters.COMMAND,getattcode)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
     )
     
     app.add_handler(conv_handler)
     app.add_handler(CommandHandler("report", report))
     print("Bot is running ....", flush=True)
     app.run_polling()

if __name__ == "__main__":
     main()

