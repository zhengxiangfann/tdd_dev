from django.test import TestCase
from django.urls import resolve
from .views import home_page
from django.http import HttpRequest
# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        found = resolve('/lists/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #➊
        response = home_page(request) #➋
        self.assertTrue(response.content.startswith(b'<html>')) #➌
        self.assertIn(b'<title>To-Do lists</title>', response.content) #➍
        self.assertTrue(response.content.endswith(b'</html>')) #➎
