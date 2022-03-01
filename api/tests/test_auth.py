from .tests_setup import TestSetup
from ..models import CustomUser


class TestAuth(TestSetup):
    def test_user_cannot_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_can_register_successfully(self):
        response = self.client.post(self.register_url, data=self.user_data, format='json')
        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertEqual(response.data['username'], self.user_data['username'])
        self.assertEqual(response.status_code, 201)

    def test_user_cannot_register_with_existing_email(self):
        response = self.client.post(self.register_url, data=self.user_data, format='json')
        self.assertEqual(response.status_code, 201)
        response2 = self.client.post(self.register_url, data=self.user_data, format='json')
        self.assertEqual(response2.status_code, 400)

    def test_user_cannot_register_with_existing_username(self):
        response = self.client.post(self.register_url, data=self.user_data, format='json')
        self.assertEqual(response.status_code, 201)

        response2 = self.client.post(self.register_url, data=self.user_data, format='json')
        self.assertEqual(response2.status_code, 400)

    def test_user_cannot_login_with_no_data(self):
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code, 400)

    def test_user_cannot_login_with_wrong_data(self):
        register = self.client.post(self.register_url, data=self.user_data, format='json')
        self.assertEqual(register.status_code, 201)
        wrong_email = self.client.post(self.login_url, data=self.wrong_email_data, format='json')
        self.assertEqual(wrong_email.status_code, 400)
        wrong_password = self.client.post(self.login_url, data=self.wrong_password_data, format='json')
        self.assertEqual(wrong_password.status_code, 400)

    def test_user_cannot_login_with_unverified_email(self):
        register = self.client.post(self.register_url, data=self.user_data, format='json')
        self.assertEqual(register.status_code, 201)
        response = self.client.post(self.login_url, data=self.user_data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_user_can_login_successfully(self):
        self.client.post(self.register_url, data=self.user_data, format='json')
        # Verify the email
        user = CustomUser.objects.get(email=self.user_data['email'])
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url, data=self.user_data, format='json')
        self.assertEqual(response.status_code, 200)
