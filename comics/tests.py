from django.test import TestCase


class HomeTests(TestCase):
    """Tests for the home page."""
    def test_home_title(self):
        """The title should have "Minicomi" in it."""
        response = self.client.get('/')

        self.assertIn('<title>Minicomi', str(response.content))
