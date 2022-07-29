from books.requests.books import *


class TestBooks:

    def test_get_books_200(self):
        r = get_books()
        assert r.status_code == 200, 'status code is not ok'

    def test_books_invalid_type(self):
        r = get_books(book_type = 'abc')
        assert r.status_code == 400, 'status code is not ok'
        assert r.json()['error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    def test_all_books(self):
        r = get_books()
        assert len(r.json()) == 6, 'bool total is wrong'

    def test_get_all_books_limit(self):
        r = get_books(limit = 3)
        assert len(r.json()) == 3, 'limit is not working'

    def test_get_all_books_type_fiction(self):
        r = get_books(book_type = 'fiction')
        assert len(r.json()) == 4, 'type fiction not working'

    def test_get_all_books_type_non_fiction(self):
        r = get_books(book_type = 'non-fiction')
        assert len(r.json()) == 2, 'type non-fiction not working'

    def test_get_all_books_type_and_limit(self):
        r = get_books(book_type = 'fiction', limit=2)
        assert len(r.json()) == 2, 'type&limit not working'
        assert r.json()[0]['type'] == 'fiction', 'type filter not working'
        assert r.json()[0]['type'] == 'fiction', 'type filter not working'

    # def aatest_get_all_books_type_and_limit(self):
    #     r = get_books(book_type = 'non-fiction', limit=1)
    #     assert len(r.json()) == 2, 'type&limit not working'

    def test_get_book(self):
        r = get_book(1)
        expected = {
            "id": 1,
            "name": "The Russian",
            "author": "James Patterson and James O. Born",
            "isbn": "1780899475",
            "type": "fiction",
            "price": 12.98,
            "current-stock": 12,
            "available": True
        }
        assert r.status_code == 200, 'status code is not ok'
        assert r.json() == expected, 'book data not ok'

    def test_get_book_invalid_id(self):
        r = get_book(202)
        assert r.status_code == 404, 'code not ok'
        assert r.json()['error'] == 'No book with id 202', 'invalid id message is not ok'
