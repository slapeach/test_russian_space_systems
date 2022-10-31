# test_russian_space_systems
Создано приложение music. На главной странице отображается таблица со столбцами альбом[год выпуска], название альбома, артист, треки.
При нажатии на кнопку sort осуществляется сортировка по названию альбома или по имени артиста.

## **Как запустить проект**
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:slapeach/test_russian_space_systems.git
```
```
cd test_russian_space_systems
```
Перейти в директорию config и создать файл .env (шаблон наполнения env-файла - ниже):
```
cd test_project
```
```
cd config
```
```
touch .env
```
После заполнения env-файла по шаблону необходимо создать виртуальное окружение:
```
python3 -m venv env
```
На Windows:
```
python -m venv venv
```
Активировать виртуальное окружение:
```
source env/bin/activate
```
На Windows:
```
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
На Windows:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Перейти в директорию с файлом manage.py и выполнить миграции:
```
python3 manage.py migrate
```
На Windows:
```
python manage.py migrate
```
Заполнить базу тестовыми данными:
```
python3 python manage.py loaddata dump.json
```
На Windows:
```
python manage.py loaddata dump.json
```
Запустить проект:
```
python3 manage.py runserver
```
На Windows:
```
python manage.py runserver
```

## **Шаблон наполнения env-файла**
Указываем, что работаем с postgresql
```
DB_ENGINE=django.db.backends.postgresql
```
Указываем имя базы данных
```
DB_NAME=postgres
```
Логин для подключения к базе данных
```
POSTGRES_USER=username
```
Устанавливаем пароль для подключения в БД
```
POSTGRES_PASSWORD=user_password
```
Указываем хост
```
DB_HOST=localhost
```
Указываем порт для подключения к БД
```
DB_PORT=5432
```