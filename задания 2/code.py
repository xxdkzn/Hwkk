import unittest
import requests
import json
from datetime import datetime

class TestYandexDiskAPI(unittest.TestCase):
    # Замените на ваш токен доступа к Яндекс.Диску
    ACCESS_TOKEN = "your_access_token_here"
    
    def setUp(self):
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {
            "Authorization": f"OAuth {self.ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        self.folder_name = f"test_folder_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def test_create_folder_success(self):
        # Проверяем создание папки
        response = requests.put(f"{self.base_url}?path={self.folder_name}", headers=self.headers)
        self.assertEqual(response.status_code, 201)

        # Проверяем, что папка появилась в списке файлов
        response = requests.get(self.base_url, headers=self.headers)
        self.assertIn(self.folder_name, [item["name"] for item in response.json()["items"]])

    def test_create_folder_empty_name(self):
        # Проверяем создание папки с пустым именем
        response = requests.put(f"{self.base_url}?path=", headers=self.headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_create_folder_unauthorized(self):
        # Проверяем создание папки без авторизации
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.put(f"{self.base_url}?path={self.folder_name}", headers=headers)
        self.assertEqual(response.status_code, 401)
        self.assertIn("error", response.json())

    def test_create_folder_existing(self):
        # Проверяем создание папки, которая уже существует
        response = requests.put(f"{self.base_url}?path={self.folder_name}", headers=self.headers)
        self.assertEqual(response.status_code, 409)
        self.assertIn("error", response.json())

if __name__ == "__main__":
    unittest.main()