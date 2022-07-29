from books.requests.api_clients import *
from random import randint


class TestApiClient:
    nr = randint(1, 9999999999)
    clientName = 'Alex'
    clientEmail = f'valid_email{nr}@email.com'
    response = login(clientName, clientEmail)

    def test_login_200(self):
        assert self.response.status_code == 201, 'status code is not ok'

    def test_login_has_token_key(self):
        assert 'accessToken' in self.response.json().keys(), 'Token key is not present'

    def test_invalid_email_400(self):
        self.response = login('Alex', 'abc')
        assert self.response.status_code == 400, 'status code is not ok'
        assert self.response.json()['error'] == 'Invalid or missing client email.', 'invalid error message'

    def test_login_409(self):
        self.response = login(self.clientName, self.clientEmail)
        assert self.response.status_code == 409, 'status code is not ok'
        assert self.response.json()['error'] == 'API client already registered. Try a different email.'
