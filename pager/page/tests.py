from rest_framework.test import APITestCase, force_authenticate
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .models import Page


class PageTest(TestCase):

    def setUp(self):
        User.objects.create(
            username='TestUser',
            password='blargh123'
        )
        Page.objects.create(
            title='Unit Test Page',
            meta_description='Meta Description',
            author=User.objects.get(username='TestUser'),
            status='published',
            content='Page Content'
        )

    def test_page_created(self):
        page = Page.objects.get(title='Unit Test Page')
        assert page is not None

    def test_page_slug_generated(self):
        page = Page.objects.get(title='Unit Test Page')
        assert page.slug is not None

    def test_page_slug_generated_correctly(self):
        page = Page.objects.get(title='Unit Test Page')
        print(page.slug)
        assert page.slug == 'unit-test-page'


class TestPageAPI(APITestCase):
    # TODO: Fix 'test_model_can_be_created'
    def setUp(self):
        User.objects.create(
            username='TestUser',
            password='blargh123'
        )
        Page.objects.create(
            title='Unit Test Page',
            meta_description='Meta Description',
            author=User.objects.get(username='TestUser'),
            status='published',
            content='Page Content'
        )
        self.page = Page.objects.get(title='Unit Test Page')

    def test_model_can_be_retrieved(self):
        response = self.client.get('/pages/%d' % self.page.id, follow=True)
        self.assertTrue(response.status_code == 200)

    def test_model_can_be_created(self):
        url = '/pages/'
        data = {
            "title": "Post Test Page",
            "slug": "post-tes-page",
            "meta_description": "Meta Description",
            "status": "published",
        }
        self.client.login(username='TestUser', password='blargh123')
        response = self.client.post(
            url,
            data,
            fomat='json',
        )
        print(response)
        page = Page.objects.get(slug='post-test-page')
        assert page is not None


