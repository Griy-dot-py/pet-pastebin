from unittest import TestCase
import requests

from typing import Optional

from pathlib import Path


URL = "http://localhost:5000/api/pastebin/"
TEST_USER = 1
UNEXISTING_USER = 0
UNEXISTING_ID = "Thiscannotbehashid"
TEXT = "Hello, world!"
ID = "AAAAAAAAABU="
MAX_SIZE_IN_MB = 10


class PastebinTest(TestCase):
    def __test_post(
        self,
        *,
        user_id: int|None = TEST_USER,
        text: int|None = TEXT
    ) -> requests.Response:
        json = {}
        if user_id is not None:
            json["user_id"] = user_id
        if text is not None:
            json["text"] = text
        
        return self.session.post(URL, json=json)
    
    def __test_get(self, *, id: Optional[str] = ID):
        return self.session.get(URL + f"/{id}")
        
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
        path = Path("test_text.txt")
        
        max_file_bytes = 10 * 1024 * 1024
        times_to_print_text = max_file_bytes / len(TEXT) * 1.2
        with open(path, "w") as file:
            for _ in range(round(times_to_print_text)):
                file.write(TEXT + "\n")
        cls.path = path
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()
        cls.path.unlink()
    
    def test_post_status_code(self):
        resp = self.__test_post()
        self.assertEqual(resp.status_code, 201)
    
    def test_post_content(self):
        json = self.__test_post().json()
        self.assertTrue("id" in json)
    
    def test_post_with_no_text(self):
        resp = self.__test_post(text=None)
        self.assertTrue(resp.status_code, 400)
    
    def test_post_with_no_user(self):
        resp = self.__test_post(user_id=None)
        self.assertTrue(resp.status_code, 400)
    
    def test_cannot_post_as_unexistng_user(self):
        resp = self.__test_post(user_id=UNEXISTING_USER)
        self.assertEqual(resp.status_code, 400)
    
    def test_cannot_post_huge_file(self):
        with open(self.path) as file:
            content = file.read()
        
        response = self.__test_post(text=content)
        self.assertEqual(response.status_code, 400)
    
    def test_can_get(self):
        resp = self.__test_get()
        self.assertEqual(resp.status_code, 200)
    
    def test_get_content(self):
        json = self.__test_get().json()
        self.assertEqual(json["text"], TEXT)
    
    def test_get_unexisting(self):
        resp = self.__test_get(id=UNEXISTING_ID)
        self.assertEqual(resp.status_code, 404)
