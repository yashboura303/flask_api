import unittest
import requests


class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:5000/course"
    COURSE_OBJ = {
        "description": "This is a brand new course",
        "discount_price": 5,
        "title": "Brand new course",
        "price": 25,
        "image_path": "images/some/path/foo.jpg",
        "on_discount": False
    }
    BAD_COURSE_OBJ = {
        "description": "This is a brand new course",
        "discount_price": 5,
        "title": "Brand new course",
        "price": "this_should_be_integer",
        "image_path": "images/some/path/foo.jpg",
        "on_discount": False
    }
    UPDATE_COURSE = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 5,
        "id": 17,
        "price": 25,
        "title": "Blah blah blah",
        "on_discount": False,
        "description": "New description"
    }
    BAD_PRICE_UPDATE_COURSE = {
        "image_path": "images/some/path/foo.jpg",
        "discount_price": 5,
        "id": 17,
        "price": "this_should_be_integer",
        "title": "Blah blah blah",
        "on_discount": False,
        "description": "New description"
    }
    BAD_IMAGE_PATH_ADD_COURSE = {
        "image_path": "images/some/path/foo.jpg/images/some/path/foo.jpg/images/some/path/foo.jpg/images/some/path/foo.jpg/images/some/path/foo.jpg/images/some/path/foo.jpg/images/some/path/foo.jpg/images/some/path/foo.jpg/images/some/path/foo.jpg/images/some/path/foo.jpg/images/some/path/foo.jpg",
        "discount_price": 5,
        "price": "this_should_be_integer",
        "title": "Blah blah blah",
        "on_discount": False,
        "description": "New description"
    }

    def test_get_course_by_id(self):
        id = 8
        r = requests.get(ApiTest.API_URL + f"/{id}")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers["Content-Type"], 'application/json')

    def test_get_course_by_bad_id(self):
        id = -8
        r = requests.get(ApiTest.API_URL + f"/{id}")
        self.assertEqual(r.status_code, 404)

    def test_delete_course(self):
        id = 62
        r = requests.delete(ApiTest.API_URL + f"/{id}")
        self.assertEqual(r.status_code, 204)
        self.assertEqual(r.headers["Content-Type"], 'application/json')

    def test_add_course(self):
        r = requests.post(ApiTest.API_URL,
                          data=ApiTest.COURSE_OBJ)
        self.assertEqual(r.status_code, 200)

    def test_add_bad_price_course(self):
        r = requests.post(ApiTest.API_URL,
                          data=ApiTest.BAD_COURSE_OBJ)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["message"], "Not a valid integer. ")

    def test_add_bad_image_path_course(self):
        r = requests.post(ApiTest.API_URL,
                          data=ApiTest.BAD_IMAGE_PATH_ADD_COURSE)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(
            r.json()["message"], "Not a valid integer. Longer than maximum length 100. ")

    def test_update_course(self):
        id = ApiTest.UPDATE_COURSE["id"]
        r = requests.put(ApiTest.API_URL +
                         f"/{id}", data=ApiTest.UPDATE_COURSE)
        self.assertEqual(r.status_code, 200)

    def test_update_bad_course(self):
        id = ApiTest.BAD_PRICE_UPDATE_COURSE["id"]
        r = requests.put(ApiTest.API_URL +
                         f"/{id}", data=ApiTest.BAD_PRICE_UPDATE_COURSE)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()["message"], "Not a valid integer. ")

    def test_nth_page_of_courses(self):
        r = requests.get(ApiTest.API_URL, params={
                         "page-number": "20", "page-size": "10"})
        self.assertEqual(r.status_code, 200)

    def test_default_page_of_courses(self):
        r = requests.get(ApiTest.API_URL)
        self.assertEqual(r.status_code, 200)
