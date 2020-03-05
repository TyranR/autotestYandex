# Задача №2 Автотест API Яндекса
# # Проверим актуальность API Яндекс.Переводчик'а для потенциального сервиса переводов. Используя библиотеку request
# напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
# #
# # Пример положительных тестов:
# #
# # Код ответа соответствует 200
# # результат перевода правильный - "привет"


import requests
import json
from urllib.parse import urlencode


def translate(message):
    """
    Создаем запрос
    :return:
    """
    params = {
        'key': TOKEN,
        'text': message,
        'lang': 'ru-en',
        'format': 'plain',
    }
    response = requests.get(
        'https://translate.yandex.net/api/v1.5/tr.json/translate',
        params
    )
    response_json = response.json()
    return response_json


def text_for_translate():
    """
    Запрос текста на перевод
    :return:
    """
    text = input("Введи слово для перевода с русского на английский: ")
    return text


def main():
    """
    Основая функция
    :return:
    """
    print(translate(text_for_translate()))


TOKEN = 'trnsl.1.1.20200305T205238Z.77c7a050a66a991c.576622bfa0eaa88f0aced1535c27efb07d816844'


if __name__ == '__main__':
    main()