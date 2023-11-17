import os
from django.core.management.base import BaseCommand
from tinydb import TinyDB
from test_project.settings import BASE_DIR


class Command(BaseCommand):

    help = "Создает БД TinyDB"

    def handle(self, *args, **options):
        if not os.path.exists(f"{BASE_DIR}/db.json"):
            db = TinyDB(f"{BASE_DIR}/db.json")
            db.insert_multiple([
                {"name": "template1", "email": "test@example.com", "phone": "+7 999 999 99 99"},
                {"name": "template2", "email": "test@example.ru", "phone": "+7 999 999 99 96"},
                {"name": "template3", "email": "test@example.fr", "phone": "+7 999 999 99 97",
                 "text": "test", "date": "1998.10.10"},
                {"name": "template4", "email": "test@example.cn", "phone": "+7 999 999 99 98"},
                {"field": "Jack", "field1": "Daniels"},
                {"name": "template5", "email": "test@example.us", "surname": "Thompson"},
                {"name": "template6", "email": "test@example.by", "phone": "+7 999 999 99 95",
                 "text": "test1", "date": "1999.10.10", "city": "Moscow"}
            ])
            self.stdout.write(self.style.SUCCESS("БД успешно создана"))
        else:
            self.stdout.write(self.style.ERROR("БД уже существует"))
