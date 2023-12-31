# Тестовое задание от Плотникова Дмитрия

### В приложении используются следующие ключевые зависимости:
- Django 4.2.7
- DRF 3.14
- Python 3.10
- requests
- pytest
- TinyDB

### Чтобы запустить приложение, нужно сделать следующее:
1. Установить виртуальное окружение с помощью команды *py -m venv <название окружения>*
2. Запустить виртуальное окружение с помощью команды *<название окружения>/scripts/activate*
3. Установить зависимости с помощью команды *py -m pip install -r requirements.txt*
4. Если нет файла с БД (db.json), создать его с помощью команды *py manage.py create_db*
5. Поместить файл .env в корень локального репозитория с проектом (файл будет в письме на почте)
6. Запустить сервер с помощью команды *py manage.py runserver*
7. Отправить POST-запрос по URL http://127.0.0.1:8000/api/get_form?email=<почта>&phone=<телефон>&date=<дата>&text=<текст>

PS: без файла .env приложения не запустится. Этот файл будет выслан на почту вместе с ссылкой на GitHub. Файл нужно поместить в локальный репозиторий в корень проекта.

#### Чтобы запустить тесты, нужно в консоли из локального репозитория с проектом запустить команду *pytest test_app/tests.py -v*

#### Чтобы запустить линтер, нужно в консоли из локального репозитория с проектом запустить команду *pylint test_app/views.py* или *pylint test_app/tests.py*

#### Чтобы запустить статический анализатор, нужно в консоли из локального репозитория с проектом запустить команду *mypy test_app/views.py* или *mypy test_app/tests.py*