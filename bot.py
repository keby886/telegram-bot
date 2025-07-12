from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# 从环境变量读取 Token（更安全）
TOKEN = os.environ.get("BOT_TOKEN")

# /start 命令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 我已经上线啦！你可以随时发消息给我～")

# 自动回复逻辑
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "你好" in text:
        await update.message.reply_text("你好！我是部署在 Render 云端的机器人 😎")
    elif "天气" in text:
        await update.message.reply_text("今天天气晴朗 ☀️")
    else:
        await update.message.reply_text(f"你说的是：{text}")

# 构建机器人应用
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

# 启动
app.run_polling()
