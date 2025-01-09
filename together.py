import os
import httpx
import pandas as pd
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ваш токен доступу до бота
TOKEN = '7943185547:AAFpj0dPC1cYHq43BhDEU22XCa9u7oe7-BI'
API_KEY = 'AIzaSyCGKROsMORrekkpfN3-BA-CTIX8qv31h7U'
SEARCH_ENGINE_ID = '04047c2fa36a04636'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello, I am your bot! Send me a search query with /search <query>')

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    search_query = ' '.join(context.args)
    results = google_search(API_KEY, SEARCH_ENGINE_ID, search_query)
    response_text = '\n'.join([item['title'] + ": " + item['link'] for item in results['items']])
    await update.message.reply_text(response_text)

def google_search(key, engine_id, search_query, **params):
    base_url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': key,
        'cx': engine_id,
        'q': search_query,
        **params
    }
    response = httpx.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('search', search))
    application.run_polling()

if __name__ == '__main__':
    main()
