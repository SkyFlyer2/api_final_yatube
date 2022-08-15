# API Yatube

REST API для учебного проекта  "Социальная сеть Yatube". Создано в рамках курса Яндекс.Практикум.

Аутентификация пользователей по JWT-токену

Работает со следующими модулями Yatube: посты, комментарии, группы, подписки

Поддерживаются методы GET, POST, PUT, PATCH, DELETE

Данные возвращаются в формате JSON

## Технологии
* Python, версия 3.8.10, Django REST Framework 2.2.16
* библиотека Djoser - аутентификация по JWT-токену
* python-dotenv - хранение секретных ключей и доступ к ним через переменные окружения
* git - система управления версиями


## Как запустить проект:

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/SkyFlyer2/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздайте и активируйте виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создайте в директории файл .env и поместите туда SECRET_KEY, необходимый для запуска проекта

Выполните миграции:

```
python manage.py migrate
```

Создайте суперпользователя:

```
python manage.py createsuperuser
```

Запустите проект:

```
python manage.py runserver
```
____________________________________

Проект доступен по адресу http://127.0.0.1:8000/

Документация по API http://localhost:8000/redoc/

Командой *pytest* можно запустить тесты модулей
```

## Примеры API-запросов

