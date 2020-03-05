import unittest
from unittest.mock import patch
import json
from main import translate
from main import text_for_translate


class TestYandex(unittest.TestCase):

    def test_translate_work_code(self):
        """
        Проверка на ответ 200
        :return:
        """
        answer_json = translate("Привет")
        self.assertEqual(answer_json['code'], 200)

    def test_correct_translation(self):
        """
        ПРоверил на правильный перевод
        :return:
        """
        answer_json = translate("Привет")
        result = answer_json.get('text')
        self.assertEqual(result[0], "Hi")


TOKEN = 'trnsl.1.1.20200305T205238Z.77c7a050a66a991c.576622bfa0eaa88f0aced1535c27efb07d816844'


if __name__ == '__main__':
    unittest.main()
