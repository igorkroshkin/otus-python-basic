# 1. Основной образ (Python 3.11)
FROM python:3.11-slim

# 2. Установка рабочей директории внутри контейнера
WORKDIR /app

# 3. Копирование зависимостей и их установка
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копирование всего кода приложения в контейнер
COPY . .

# 5. Экспонирование порта 8000
EXPOSE 8000

# 6. Запуск веб-сервера Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]