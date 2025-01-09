import  os
import  httpx
import  pandas as pd

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

api_key = 'AIzaSyCGKROsMORrekkpfN3-BA-CTIX8qv31h7U'
search_engine_id = '04047c2fa36a04636'
query = 'Python tutorial'

search_results = []
for i in range(1, 100, 10):
    response = google_search(
        key=api_key,
        engine_id=search_engine_id,
        search_query=query,
        start=i
    )
    search_results.extend(response.get('items', []))

df = pd.json_normalize(search_results)
df.to_csv('google_search_results.csv', index=False)


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ваш токен доступу до бота
TOKEN = '7943185547:AAFpj0dPC1cYHq43BhDEU22XCa9u7oe7-BI'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello, I am your bot!')


def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))

    application.run_polling()


if __name__ == '__main__':
    main()
