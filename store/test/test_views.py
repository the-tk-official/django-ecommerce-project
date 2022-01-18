from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products

# from unittest import skip


"""Demonstrating skipping test"""
# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


class TestViewResponses(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(
            category_id=1, title='django beginners', created_by_id=1,
            slug='django-beginners', price='20.00', image='django'
        )

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.client.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.client.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """
        Test allowed hosts
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.client.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.client.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = all_products(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    # def test_view_factory(self):
    #     """
    #     Example: Using request factory
    #     """
    #     request = self.factory.get('/')
    #     response = all_products(request)
    #     html = response.content.decode('utf-8')
    #     self.assertIn('<title>BookStore</title>', html)
    #     self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
    #     self.assertEqual(response.status_code, 200)
