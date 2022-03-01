from rest_framework.test import APITestCase
# from django.urls import reverse
from faker import Faker


class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = '/auth/users/'
        self.login_url = '/auth/token/login/'
        self.logout_url = '/auth/token/logout/'
        self.user_url = '/auth/users/'
        self.fake = Faker()
        self.email = self.fake.email()
        self.username = self.email.split('@')[0]
        self.password = self.fake.password()

        self.user_data = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            're_password': self.password
        }
        self.wrong_email_data = {
            'email': 'test2@test.com',
            'password': 'test_password@#$123409*',
        }

        self.wrong_password_data = {
            'email': 'test@test.com',
            'password': 'test_password$123409*',
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
