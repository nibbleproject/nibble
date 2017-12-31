from django.test import TestCase


class HomeTests(TestCase):
    """Tests for the home page."""
    def test_home_title(self):
        """The title should have "Nibble" in it."""
        response = self.client.get('/')

        self.assertIn('<title>Nibble', str(response.content))


class DashboardTests(TestCase):
    """Tests for the dasboard."""
    def test_dashboard(self):
        response = self.client.get('/dashboard/')

        self.assertEqual(response.status_code, 200)
