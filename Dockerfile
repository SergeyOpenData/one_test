# Використання базового образу Python
FROM python:3.9-slim

# Встановлення робочої директорії
WORKDIR /app

# Копіювання файлу залежностей
COPY requirements.txt requirements.txt

# Встановлення залежностей
RUN pip install -r requirements.txt

# Копіювання всіх файлів проєкту до контейнера
COPY . .

# Команда для запуску вашого бота
CMD ["python", "mytelegrambot.py"]

