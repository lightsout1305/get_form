"""
Модуль с логикой приложения test_app.

В модуле есть класс GetForm,
который отвечает за логику get_form - POST-метода,
который ищет шаблон по отправленным полям формы.

"""
import os
import re
from datetime import datetime
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from tinydb import TinyDB
from test_project.settings import BASE_DIR


class GetForm(APIView):
    """
    Класс GetForm, который отвечает за всю логику метода get_form.
    """
    # pylint: disable=too-many-nested-blocks
    # pylint: disable=too-many-statements
    # pylint: disable=too-many-branches
    # pylint: disable=unused-argument

    db: TinyDB = TinyDB(f'{BASE_DIR}/db.json') \
        if os.path.exists(f'{BASE_DIR}/db.json') else None

    def post(self, request: Request) -> Response:
        """
        POST-метод get_form, который отправляет поля в URL,
        ищет совпадения по названию и типу данных
        отправленной формы в шаблонах в БД.

        Полей может передаваться от 1 до 4 включительно.

        Поля могут быть следующие:
        - email (Передается в формате 'test@example.com')
        - phone (Передается в формате '+7 999 999 99 99')
        - date (Передается в формате 'ГГГГ.ММ.ДД')
        - text (Передается строка)

        Метод возвращает имя подходящего шаблона в формате:
        {
            "template_name": <имя шаблона>
        }

        Если шаблон не найден, метод возвращает названия и тип данных
        отправленных полей в URL.

        :param request: Request
        :return: Response
        """

        field_types: dict = {  # Словарь с типами данных переданных полей
            "email": "EMAIL_FIELD",
            "phone": "PHONE_FIELD",
            "date": "DATE_FIELD",
            "text": "TEXT_FIELD"
        }
        errors: dict = {}  # Динамический словарь с ошибками,
        # который возвращается вместе с 400 статус-кодом
        form_data: dict = {}  # Динамический словарь с переданными полями формы и их значениями

        # Если передано меньше 1 поля и больше 4, то возвращается 400
        if len(self.request.query_params) == 0 or len(self.request.query_params) > 4:
            errors = {
                "error": "Некорректное количество полей"
            }
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)

        # Получаем значения переданных полей формы
        email = self.request.query_params.get("email")
        phone = self.request.query_params.get("phone")
        date = self.request.query_params.get("date")
        text = self.request.query_params.get("text")

        # Если в URL передан date, проверяем формат
        if date is not None:
            try:
                datetime.strptime(date, "%Y.%m.%d").strftime('%Y.%m.%d')
            except ValueError:
                # Если дата некорректная, пополняем словарь с ошибками
                errors.update(
                    {"date": f"Дата '{date}' некорректная. "
                             f"Дата должна быть в формате 'ГГГГ.ММ.ДД'"}
                )
            else:
                # Если дата корректная, пополняем словарь с данными формы
                form_data.update({"date": date})

        # Если в URL передан phone, проверяем формат
        if phone is not None:
            try:

                # Проверяем номер с динамическим добавлением символа '+',
                # так как в URL этот символ не парсится
                if not phonenumbers.is_valid_number(phonenumbers.parse('+' + phone)):
                    # Если телефон некорректный, пополняем словарь с ошибками
                    if phone.startswith(' '):
                        phone = phone.replace(" ", "+", 1)
                    errors.update(
                        {"phone": f"Телефон '{phone}' некорректен. "
                                  f"Телефон должен быть в формате '+7 999 999 99 99'"}
                    )

                # Если телефон корректный, добавляем '+' к нему
                # и заносим в словарь с данными формы
                else:
                    if phone.startswith(' '):
                        phone = phone.replace(" ", "+", 1)
                    form_data.update({"phone": phone})

            # Если вместо цифр была передана строка, то пополняем словарь с ошибками
            except NumberParseException:
                if phone.startswith(' '):
                    phone = phone.replace(" ", "+", 1)
                errors.update(
                    {"phone": f"Телефон '{phone}' некорректен. "
                              f"Телефон должен быть в формате '+7 999 999 99 99'"}
                )

        # Если в URL передан email, проверяем формат
        if email is not None:

            # Если email некорректный, пополняем словарь с ошибками
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                errors.update(
                    {"email": f"E-mail '{email}' некорректен. "
                              f"E-mail должен быть в формате 'a.ivanov@mail.ru'"}
                )

            # Если email корректный, добавляем в словарь с данными формы
            else:
                form_data.update({"email": email})

        # Если в URL передан text, проверяем, что непустые данные
        if text is not None:

            # Если данные не переданы, пополняем словарь с ошибками
            if len(text) == 0:
                errors.update({"text": "Текст должен быть непустой"})

            # Если есть данные, пополняем словарь с данными формы
            else:
                form_data.update({"text": text})

        # После валидации всех полей проверяем словарь с ошибками.
        # Если он непустой, то возвращаем 400 и какие валидации не прошли
        if len(errors) > 0:
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)

        # Если с валидацией все в порядке, идем в БД
        for record in self.db:  # Итерируемся по шаблонам в БД: record - словарь
            count: int = 0  # Создаем счетчик совпадений полей в форме и полей в шаблоне

            # Убираем поле name из записи БД и сохраняем его значение в template_name
            template_name = record.pop('name') if 'name' in record else None

            # Если вдруг name в record нет, переходим к следующей итерации по БД
            if template_name is None:
                continue

            # Если шаблон в БД и переданная форма одинаковы, возвращаем 200 и имя шаблона
            if record == form_data:
                return Response(data={"template_name": template_name}, status=status.HTTP_200_OK)

            # Если в форме полей больше, чем в шаблоне, то делаем следующее
            if len(form_data) < len(record):

                # Проходим по полям переданной формы
                for field, definition in form_data.items():
                    if field in record:  # Если поле есть в шаблоне

                        # И если значения полей в форме и шаблоне одинаковы
                        if record[field] == definition:
                            count += 1  # Увеличиваем счетчик совпадений по полям

                            # Если счетчик совпадений равен количеству полей формы,
                            # возвращаем 200 и имя шаблона
                            if count == len(form_data):
                                return Response(
                                    data={"template_name": template_name},
                                    status=status.HTTP_200_OK
                                )

            # Если в форме полей больше, чем в шаблоне, то делаем следующее
            if len(form_data) > len(record):

                # Проходим по полям переданной формы
                for field, definition in form_data.items():
                    if field in record:  # Если поле есть в шаблоне

                        # И если значения полей в форме и шаблоне одинаковы
                        if record[field] == definition:
                            count += 1  # Увеличиваем счетчик совпадений по полям

                            # Если счетчик совпадений равен количеству полей шаблона,
                            # возвращаем 200 и имя шаблона
                            if count == len(record):
                                return Response(
                                    data={"template_name": template_name},
                                    status=status.HTTP_200_OK
                                )

        # Если никаких совпадений не нашлось, то делаем следующее
        for field, field_type in field_types.items():  # Проходим по типам полей

            # Если этот тип есть в переданных полях формы,
            # то в словаре с переданными данными формы перезаписываем значение на тип поля
            if field in form_data:
                form_data[field] = field_type

        # В конце возвращаем 200 и словарь с переданными полями и их типами
        return Response(data=form_data, status=status.HTTP_200_OK)
