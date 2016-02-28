from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Page
from django.core.urlresolvers import reverse


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
        self.assertTrue(
            page,
            msg="Page could not be created."
        )

    def test_page_slug_generated(self):
        page = Page.objects.get(title='Unit Test Page')
        self.assertEqual(
            page.slug,
            'unit-test-page',
            msg='Page slug was not created or was created incorrectly.'
        )


class TestPageAPI(TestCase):

    def setUp(self):
        self.username = 'TestUser'
        self.email = 'example@example.com'
        self.password = 'bigpass'
        User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )
        Page.objects.create(
            title='Unit Test Page',
            meta_description='Meta Description',
            author=User.objects.get(username='TestUser'),
            status='published',
            content='Page Content'
        )
        self.user = User.objects.get(username='TestUser')
        self.page = Page.objects.get(title='Unit Test Page')
        self.client = APIClient()

    def test_page_can_be_retrieved(self):
        request = self.client.get('/pages/%d/' % self.page.id)
        self.assertEqual(request.status_code, 200)

    def test_correct_page_is_retrieved(self):
        request = self.client.get('/pages/%d/' % self.page.id)
        content = request.content
        self.assertIn('Unit Test Page', str(content))

    def test_page_can_be_created(self):
        url = '/pages/'
        data = {
            'id': None,
            'title': 'Post Test Page',
            'slug': 'post-test-page',
            'meta_description': 'meta description',
            'author': reverse('user-detail', kwargs={'pk': self.user.id}),
            'status': 'published',
            'parent': None,
            'children': [],
            'content': 'content'
        }
        self.client.login(
            username=self.username,
            password=self.password
        )
        response = self.client.post(
            path=url,
            data=data,
            format='json',
            follow=True,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Page.objects.get(slug='post-test-page'))

