# Meme API

## Описание

Веб-приложение на Python с использованием DRF, которое предоставляет API для работы с коллекцией мемов. Приложение состоит из двух сервисов: сервис с публичным API с бизнес-логикой и сервис для работы с медиа-файлами, используя S3-совместимое хранилище (MinIO).

## Функциональность

- GET /memes: Получить список всех мемов (с пагинацией).
- GET /memes/{id}: Получить конкретный мем по его ID.
- POST /memes: Добавить новый мем (с картинкой и текстом).
- PUT /memes/{id}: Обновить существующий мем.
- DELETE /memes/{id}: Удалить мем.

## Требования

- Docker и Docker Compose

## Запуск проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/TheLLiRRiKminD/MADSOFT_python_backend
cd MADSOFT_python_backend
```

2. Запустите Docker Compose:

```bash
docker-compose up
```

3. Создайте суперпользователя для доступа к admin панели:

```bash
docker-compose exec web python manage.py createsuperusercustom
```

5. Откройте браузер и перейдите на `http://0.0.0.0:8000/redoc/` для просмотра документации API.

## Тестирование

Запустите тесты:

```bash
docker-compose exec web python manage.py test