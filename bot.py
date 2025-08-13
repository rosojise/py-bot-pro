from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8398515910:AAFAlnCnUhVtTqAD3EuymwCiF7Hn3KB9tA4"  # توکن ربات رو اینجا بزار

# وقتی کاربر /start بفرسته
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات پایتونی تو هستم 😊")

# وقتی کاربر هر متن دیگه‌ای بفرسته
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"پیام شما: {text}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("ربات روشن شد...")
    app.run_polling()
