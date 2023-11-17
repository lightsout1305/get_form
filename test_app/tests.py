"""
Скрипт с тестами метода get_form.

В скрипте собраны тест-кейсы с позитивными и негативными проверками
"""
import pytest
import requests
from requests import Response


@pytest.mark.parametrize("email, template_name", [("test@example.com", "template1")])
def test_get_form_with_email_returns_template_name(email: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если в форме указан только email.
    :param email: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}", timeout=10)
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize("phone, template_name", [("+7 999 999 99 96", "template2")])
def test_get_form_returns_template_name(phone: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если в форме указан только телефон.
    :param phone: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?phone={phone}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize("date, template_name", [("1998.10.10", "template3")])
def test_get_form_with_date_returns_template_name(date: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указана дата.
    :param date: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?date={date}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize("text, template_name", [("test1", "template6")])
def test_get_form_with_text_returns_template_name(text: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан текст.
    :param text: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "email, phone, template_name", [("test@example.ru", "+7 999 999 99 96", "template2")])
def test_get_form_with_email_and_phone_returns_template_name(
        email: str, phone: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан email и телефон.
    :param email: str
    :param phone: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "email, date, template_name", [("test@example.fr", "1998.10.10", "template3")])
def test_get_form_with_email_and_date_returns_template_name(
        email: str, date: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан email и дата.
    :param email: str
    :param date: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "email, text, template_name", [("test@example.fr", "test", "template3")])
def test_get_form_with_email_and_text_returns_template_name(
        email: str, text: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан email и текст.
    :param email: str
    :param text: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "phone, date, template_name", [("+7 999 999 99 97", "1998.10.10", "template3")])
def test_get_form_and_date_returns_template_name(
        phone: str, date: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан телефон и дата.
    :param phone: str
    :param date: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?phone={phone}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "phone, text, template_name", [("+7 999 999 99 95", "test1", "template6")])
def test_get_form_and_text_returns_template_name(
        phone: str, text: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан телефон и текст.
    :param phone: str
    :param text: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?phone={phone}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "text, date, template_name", [("test", "1998.10.10", "template3")])
def test_get_form_with_text_and_date_returns_template_name(
        text: str, date: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан текст и дата.
    :param text: str
    :param date: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?text={text}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "email, phone, text, template_name",
    [("test@example.by", "+7 999 999 99 95", "test1", "template6")])
def test_get_form_with_email_phone_and_text_returns_template_name(
        email: str, phone: str, text: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан email, телефон и текст.
    :param email: str
    :param phone: str
    :param text: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "email, phone, date, template_name",
    [("test@example.by", "+7 999 999 99 95", "1999.10.10", "template6")])
def test_get_form_with_email_phone_and_date_returns_template_name(
        email: str, phone: str, date: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан email, телефон и дата.
    :param email: str
    :param phone: str
    :param date: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "email, phone, date, text, template_name",
    [("test@example.fr", "+7 999 999 99 97", "1998.10.10", "test", "template3")])
def test_get_form_with_email_phone_date_and_text_returns_template_name(
        email: str, phone: str, date: str, text: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если указан email, телефон, дата и текст.
    :param email: str
    :param phone: str
    :param date: str
    :param text: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}&date={date}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "email, phone, date, text, template_name",
    [("test@example.by", "+7 999 999 99 95", "1999.10.10", "test1", "template6")])
def test_get_form_with_less_fields_returns_template_name(
        email: str, phone: str, date: str, text: str, template_name: str) -> None:
    """
    Тест-кейс, что находится шаблон, если в нем больше полей, чем в форме.
    :param email: str
    :param phone: str
    :param date: str
    :param text: str
    :param template_name: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}&date={date}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["template_name"] == template_name


@pytest.mark.parametrize(
    "email, field_type", [("test@example.de", "EMAIL_FIELD")])
def test_get_form_with_email_returns_email_field_type(
        email: str, field_type: str) -> None:
    """
    Тест-кейс, что возвращается тип поля, если поле email.
    :param email: str
    :param field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["email"] == field_type


@pytest.mark.parametrize(
    "phone, field_type", [("+7 999 999 00 00", "PHONE_FIELD")])
def test_get_form_returns_phone_field_type(
        phone: str, field_type: str) -> None:
    """
    Тест-кейс, что возвращает тип поля, если поле телефон.
    :param phone: str
    :param field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?phone={phone}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["phone"] == field_type


@pytest.mark.parametrize("text, field_type", [("testtest", "TEXT_FIELD")])
def test_get_form_with_text_returns_text_field_type(
        text: str, field_type: str) -> None:
    """
    Тест-кейс, что возвращается тип поля, если поле текст.
    :param text: str
    :param field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["text"] == field_type


@pytest.mark.parametrize(
    "date, field_type", [("2000.02.11", "DATE_FIELD")])
def test_get_form_with_date_returns_date_field_type(
        date: str, field_type: str) -> None:
    """
    Тест-кейс, что возвращается тип поля, если поле дата.
    :param date: str
    :param field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?date={date}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["date"] == field_type


@pytest.mark.parametrize(
    "email, phone, email_field_type, phone_field_type",
    [("a.evans@gmail.com", "+7 995 441 00 15", "EMAIL_FIELD", "PHONE_FIELD")])
def test_get_form_with_email_and_phone_returns_field_types(
        email: str, phone: str, email_field_type: str, phone_field_type: str) -> None:
    """
    Тест-кейс, что возвращаются типы полей, если поля email и телефон.
    :param email: str
    :param phone: str
    :param email_field_type: str
    :param phone_field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["email"] == email_field_type
    assert get_form.json()["phone"] == phone_field_type


@pytest.mark.parametrize(
    "email, date, email_field_type, date_field_type",
    [("a.evans@gmail.com", "1992.10.11", "EMAIL_FIELD", "DATE_FIELD")])
def test_get_form_with_email_and_date_returns_field_types(
        email: str, date: str, email_field_type: str, date_field_type: str) -> None:
    """
    Тест-кейс, что возвращаются типы полей, если поля email и дата.
    :param email: str
    :param date: str
    :param email_field_type: str
    :param date_field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["email"] == email_field_type
    assert get_form.json()["date"] == date_field_type


@pytest.mark.parametrize(
    "email, text, email_field_type, text_field_type",
    [("a.evans@gmail.com", "tessssst", "EMAIL_FIELD", "TEXT_FIELD")])
def test_get_form_with_email_and_text_returns_field_types(
        email: str, text: str, email_field_type: str, text_field_type: str) -> None:
    """
    Тест-кейс, что возвращаются типы полей, если поля email и текст.
    :param email: str
    :param text: str
    :param email_field_type: str
    :param text_field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["email"] == email_field_type
    assert get_form.json()["text"] == text_field_type


@pytest.mark.parametrize(
    "phone, date, phone_field_type, date_field_type",
    [("+7 992 333 21 33", "1992.10.11", "PHONE_FIELD", "DATE_FIELD")])
def test_get_form_with_phone_and_date_returns_field_types(
        phone: str, date: str, phone_field_type: str, date_field_type: str) -> None:
    """
    Тест-кейс, что возвращаются типы полей, если поля телефон и дата.
    :param phone: str
    :param date: str
    :param phone_field_type: str
    :param date_field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?phone={phone}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["phone"] == phone_field_type
    assert get_form.json()["date"] == date_field_type


@pytest.mark.parametrize(
    "phone, text, phone_field_type, text_field_type",
    [("+7 992 333 21 33", "Just random text", "PHONE_FIELD", "TEXT_FIELD")])
def test_get_form_with_phone_and_text_returns_field_types(
        phone: str, text: str, phone_field_type: str, text_field_type: str) -> None:
    """
    Тест-кейс, что возвращаются типы полей, если поля телефон и текст.
    :param phone:
    :param text:
    :param phone_field_type:
    :param text_field_type:
    :return:
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?phone={phone}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["phone"] == phone_field_type
    assert get_form.json()["text"] == text_field_type


@pytest.mark.parametrize(
    "email, phone, date, "
    "email_field_type, phone_field_type, date_field_type",
    [("a.evans@mail.ru", "+7 992 333 21 33", "1992.05.01",
      "EMAIL_FIELD", "PHONE_FIELD", "DATE_FIELD")])
def test_get_form_with_email_phone_and_date_returns_field_types(
        email: str, phone: str, date: str,
        email_field_type: str, phone_field_type: str, date_field_type: str) -> None:
    # pylint: disable=too-many-arguments
    """
    Тест-кейс, что возвращаются типы полей, если поля email, телефон и дата.
    :param email: str
    :param phone: str
    :param date: str
    :param email_field_type: str
    :param phone_field_type: str
    :param date_field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["email"] == email_field_type
    assert get_form.json()["phone"] == phone_field_type
    assert get_form.json()["date"] == date_field_type


@pytest.mark.parametrize(
    "email, phone, date, text, "
    "email_field_type, phone_field_type, date_field_type, text_field_type",
    [("a.evans@mail.ru", "+7 992 333 21 33", "1992.05.01", "programme",
      "EMAIL_FIELD", "PHONE_FIELD", "DATE_FIELD", "TEXT_FIELD")])
def test_get_form_with_email_phone_date_and_text_returns_field_types(
        email: str, phone: str, date: str, text: str,
        email_field_type: str, phone_field_type: str,
        date_field_type: str, text_field_type: str) -> None:
    # pylint: disable=too-many-arguments
    """
    Тест-кейс, что возвращаются поля, если поля email, телефон, дата и текст.
    :param email: str
    :param phone: str
    :param date: str
    :param text: str
    :param email_field_type: str
    :param phone_field_type: str
    :param date_field_type: str
    :param text_field_type: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}&date={date}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 200
    assert get_form.json()["email"] == email_field_type
    assert get_form.json()["phone"] == phone_field_type
    assert get_form.json()["date"] == date_field_type
    assert get_form.json()["text"] == text_field_type


@pytest.mark.parametrize(
    "email, error_text",
    [("a.evans@mail",
      "E-mail 'a.evans@mail' некорректен. "
      "E-mail должен быть в формате 'a.ivanov@mail.ru'")])
def test_get_form_with_email_returns_error(
        email: str, error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если некорректный email.
    :param email: str
    :param error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["email"] == error_text


@pytest.mark.parametrize(
    "phone, error_text",
    [("+7 883 000 22",
      "Телефон '+7 883 000 22' некорректен. "
      "Телефон должен быть в формате '+7 999 999 99 99'")])
def test_get_form_with_phone_returns_error(
        phone: str, error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если некорректный телефон.
    :param phone: str
    :param error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?phone={phone}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["phone"] == error_text


@pytest.mark.parametrize(
    "date, error_text",
    [("1999.19",
      "Дата '1999.19' некорректная. "
      "Дата должна быть в формате 'ГГГГ.ММ.ДД'")])
def test_get_form_with_date_returns_error(
        date: str, error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если некорректная дата.
    :param date: str
    :param error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?date={date}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["date"] == error_text


@pytest.mark.parametrize(
    "text, error_text",
    [("", "Текст должен быть непустой")])
def test_get_form_with_text_returns_error(
        text: str, error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если пустой текст.
    :param text: str
    :param error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?text={text}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["text"] == error_text


@pytest.mark.parametrize(
    "email, phone, email_error_text, phone_error_text",
    [("dadsafaw", "sdffdsfsfs",
      "E-mail 'dadsafaw' некорректен. "
      "E-mail должен быть в формате 'a.ivanov@mail.ru'",
      "Телефон 'sdffdsfsfs' некорректен. "
      "Телефон должен быть в формате '+7 999 999 99 99'")])
def test_get_form_with_email_and_phone_returns_error(
        email: str, phone: str,
        email_error_text: str, phone_error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если некорректный email и телефон.
    :param email: str
    :param phone: str
    :param email_error_text: str
    :param phone_error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["email"] == email_error_text
    assert get_form.json()["phone"] == phone_error_text


@pytest.mark.parametrize(
    "email, date, email_error_text, date_error_text",
    [("dadsafaw", "sdffdsfsfs",
      "E-mail 'dadsafaw' некорректен. "
      "E-mail должен быть в формате 'a.ivanov@mail.ru'",
      "Дата 'sdffdsfsfs' некорректная. "
      "Дата должна быть в формате 'ГГГГ.ММ.ДД'")])
def test_get_form_with_email_and_date_returns_error(
        email: str, date: str,
        email_error_text: str, date_error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если некорректный email и дата.
    :param email: str
    :param date: str
    :param email_error_text: str
    :param date_error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form: Response = requests.post(
        f"{url}/api/get_form?email={email}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["email"] == email_error_text
    assert get_form.json()["date"] == date_error_text


@pytest.mark.parametrize(
    "email, text, email_error_text, text_error_text",
    [("example.com", "",
      "E-mail 'example.com' некорректен. "
      "E-mail должен быть в формате 'a.ivanov@mail.ru'",
      "Текст должен быть непустой")])
def test_get_form_with_email_and_text_returns_error(
        email: str, text: str,
        email_error_text: str, text_error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если некорректный email и пустой текст.
    :param email: str
    :param text: str
    :param email_error_text: str
    :param text_error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form = requests.post(
        f"{url}/api/get_form?email={email}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["email"] == email_error_text
    assert get_form.json()["text"] == text_error_text


@pytest.mark.parametrize(
    "phone, date, phone_error_text, date_error_text",
    [("9234213124", "1999.02.31",
      "Телефон '9234213124' некорректен. "
      "Телефон должен быть в формате '+7 999 999 99 99'",
      "Дата '1999.02.31' некорректная. "
      "Дата должна быть в формате 'ГГГГ.ММ.ДД'")])
def test_get_form_with_phone_and_date_returns_error(
        phone: str, date: str,
        phone_error_text: str, date_error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если некорректный телефон и дата.
    :param phone: str
    :param date: str
    :param phone_error_text: str
    :param date_error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form = requests.post(
        f"{url}/api/get_form?phone={phone}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["phone"] == phone_error_text
    assert get_form.json()["date"] == date_error_text


@pytest.mark.parametrize(
    "phone, text, phone_error_text, text_error_text",
    [("", "",
      "Телефон '' некорректен. "
      "Телефон должен быть в формате '+7 999 999 99 99'",
      "Текст должен быть непустой")])
def test_get_form_with_phone_and_text_returns_error(
        phone: str, text: str,
        phone_error_text: str, text_error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если некорректный телефон и текст.
    :param phone: str
    :param text: str
    :param phone_error_text: str
    :param text_error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form = requests.post(
        f"{url}/api/get_form?phone={phone}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["phone"] == phone_error_text
    assert get_form.json()["text"] == text_error_text


@pytest.mark.parametrize(
    "email, phone, date, email_error_text, phone_error_text, date_error_text",
    [("", "+7 888 2", "1998",
      "E-mail '' некорректен. "
      "E-mail должен быть в формате 'a.ivanov@mail.ru'",
      "Телефон '+7 888 2' некорректен. "
      "Телефон должен быть в формате '+7 999 999 99 99'",
      "Дата '1998' некорректная. "
      "Дата должна быть в формате 'ГГГГ.ММ.ДД'"
      )])
def test_get_form_with_email_phone_and_date_returns_error(
        email: str, phone: str, date: str,
        email_error_text: str, phone_error_text: str, date_error_text: str) -> None:
    # pylint: disable=too-many-arguments
    """
    Тест-кейс, что возвращается ошибка, если некорректный email, телефон и дата.
    :param email: str
    :param phone: str
    :param date: str
    :param email_error_text: str
    :param phone_error_text: str
    :param date_error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}&date={date}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["email"] == email_error_text
    assert get_form.json()["phone"] == phone_error_text
    assert get_form.json()["date"] == date_error_text


@pytest.mark.parametrize(
    "email, phone, date, text, "
    "email_error_text, phone_error_text, date_error_text, text_error_text",
    [("", "+7 888 2", "1998", "",
      "E-mail '' некорректен. "
      "E-mail должен быть в формате 'a.ivanov@mail.ru'",
      "Телефон '+7 888 2' некорректен. "
      "Телефон должен быть в формате '+7 999 999 99 99'",
      "Дата '1998' некорректная. "
      "Дата должна быть в формате 'ГГГГ.ММ.ДД'",
      "Текст должен быть непустой"
      )])
def test_get_form_with_email_phone_date_and_text_returns_error(
        email: str, phone: str, date: str, text: str,
        email_error_text: str, phone_error_text: str,
        date_error_text: str, text_error_text: str) -> None:
    # pylint: disable=too-many-arguments
    """
    Тест-кейс, что возвращается ошибка, если некорректный email, телефон, дата и текст.
    :param email: str
    :param phone: str
    :param date: str
    :param text: str
    :param email_error_text: str
    :param phone_error_text: str
    :param date_error_text: str
    :param text_error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}&date={date}&text={text}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["email"] == email_error_text
    assert get_form.json()["phone"] == phone_error_text
    assert get_form.json()["date"] == date_error_text
    assert get_form.json()["text"] == text_error_text


@pytest.mark.parametrize("error_text", ["Некорректное количество полей"])
def test_get_form_with_no_params_returns_error(error_text: str) -> None:
    """
    Тест-кейс, что возвращается ошибка, если не отправлены поля.
    :param error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form = requests.post(f"{url}/api/get_form", timeout=10)
    assert get_form.status_code == 400
    assert get_form.json()["error"] == error_text


@pytest.mark.parametrize(
    "email, phone, date, text, surname, error_text",
    [("test@example.uk", "+7 933 232 99 22", "2023.12.11", "Text", "Johnson",
      "Некорректное количество полей")])
def test_get_form_with_too_many_params_returns_error(
        email: str, phone: str, date: str, text: str, surname: str,
        error_text: str) -> None:
    # pylint: disable=too-many-arguments
    """
    Тест-кейс, что возвращается ошибка, если передано больше 4 параметров.
    :param email: str
    :param phone: str
    :param date: str
    :param text: str
    :param surname: str
    :param error_text: str
    :return: None
    """
    url: str = "http://127.0.0.1:8000"
    get_form = requests.post(
        f"{url}/api/get_form?email={email}&phone={phone}"
        f"&date={date}&text={text}&surname={surname}",
        timeout=10
    )
    assert get_form.status_code == 400
    assert get_form.json()["error"] == error_text
