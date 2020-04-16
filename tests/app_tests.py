import app
import unittest
from unittest.mock import patch
import requests


class TestMainFunctions(unittest.TestCase):
    def setUp(self):
        self.documents = app.documents
        self.directories = app.directories

    def test_get_doc_number(self):
        with patch("app.input") as in_mock:
            in_mock.return_value = "10006"
            doc_name = app.get_doc_number(self.documents)
            self.assertEqual("Аристарх Павлов", doc_name)

    def test_get_shelf_number(self):
        with patch("app.input", return_value="2207 876234"):
            shelf_number = app.get_shelf_number(self.directories)
            self.assertEqual("1", shelf_number)

    def test_check_document_existance(self):
        with patch("app.input", return_value="11-2"):
            doc_founded = app.check_document_existance(self.documents)
            self.assertTrue(doc_founded)


class MyTestApi(unittest.TestCase):

    def setUp(self) -> None:
        self.url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        self.api_key = ""

    def test_api(self):
        params = {'key': self.api_key, 'text': "hello", 'lang': "en-ru"}
        res = requests.get(self.url, params=params)
        good_result = res.status_code
        self.assertEqual(good_result, 200)

    def test_not_get_connection(self):
        params = {'key': self.api_key}
        response = requests.get(self.url, params=params)
        result = response.status_code
        self.assertNotEqual(result, 200)


if __name__ == '__main__':
    unittest.main()








