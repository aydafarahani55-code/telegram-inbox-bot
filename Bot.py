import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    msg = f"""
📩 پیام جدید

👤 نام: {user.first_name}
🔖 یوزرنیم: @{user.username}
🆔 آیدی: {user.id}

💬 پیام:
{text}
"""

    await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
app.run_polling()
