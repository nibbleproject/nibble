from django.contrib.auth.models import User
from django.test import TestCase


class AccountTestCase(TestCase):
    """Shared methods for account tests."""
    def _create_new_account(
            self, username='test', email='test@test.com', password='test123'):
        """Creates a new author account."""
        response = self.client.post('/accounts/signup/', {
            'username': username,
            'email': email,
            'password1': password,
            'password2': password,
        })

        return response


class SignupTests(AccountTestCase):
    """Tests for the signup page."""
    def test_url(self):
        """The URL should exist and return a 200."""
        response = self.client.get('/accounts/signup/')

        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        """Submitting the form should create a user."""
        self.client.post('/accounts/signup/', {
            'username': 'test',
            'email': 'test@test.com',
            'password1': 'test123',
            'password2': 'test123',
        })

        self.assertIsNotNone(User.objects.get(username='test'))

    def test_email_required(self):
        """Submitting the form should require an email address."""
        response = self.client.post('/accounts/signup/', {
            'username': 'test',
            'password1': 'test123',
            'password2': 'test123',
        })

        self.assertGreater(len(response.context['form'].errors['email']), 0)

    def test_create_confirm_redirect(self):
        """Creating an account should redirect to the confirm email dialog."""
        response = self._create_new_account()

        self.assertRedirects(response, '/accounts/confirm/')


class LoginTests(AccountTestCase):
    """Tests for the login view."""
    def test_login_unconfirmed(self):
        """Logging in as unconfirmed user should redirect to confirmation."""
        self._create_new_account()

        response = self.client.post('/accounts/login/', {
            'login': 'test',
            'password': 'test123',
        })

        self.assertRedirects(response, '/accounts/confirm/')
