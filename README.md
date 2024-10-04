# Бэкенд для сайта регистрации команд на хакатон

Добро пожаловать! Следуйте инструкциям ниже, чтобы настроить и запустить приложение.


1. **Скопируйте файл конфигурации**

   Сначала скопируйте файл `.env.example` в файл `.env`. Это сделает его доступным для Docker:
   
   ```bash
   cp .env.example .env

2. **Запустите контейнеры**

   Используйте docker-compose для сборки и запуска контейнеров:

   ```bash
   docker-compose up

3. **Остановка и удаление контейнеров**

   Если вам нужно остановить и удалить контейнеры, используйте:

   ```bash
   docker-compose down
   
# Документация 
- **GET /api/docs/**
- **GET /api/schema/**

# Библиотеки
- django==5.0 
- djangorestframework==3.15.2 
- djangorestframework-camel-case==1.4.2 
- django-environ==0.11.2 
- drf-spectacular==0.27.2
- django-cors-headers==4.4.0 
- psycopg2-binary~=2.0 
- gunicorn==22.0.0
