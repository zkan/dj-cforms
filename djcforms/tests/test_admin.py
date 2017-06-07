from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Question


class QuestionAdminTest(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'admin@pronto.com', 'admin')
        self.client.login(username='admin', password='admin')

        self.url = '/admin/djcforms/question/'

    def test_access_question_admin_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_access_question_admin_should_have_columns(self):
        Question.objects.create(
            name='favorite_color',
            text='What is your favorite color?',
            question_type='singlelinetext',
            required=True
        )
        response = self.client.get(self.url)

        expected = '<div class="text"><a href="?o=1">Name</a></div>'
        self.assertContains(response, expected, count=1, status_code=200)

        expected = '<div class="text"><a href="?o=2">Text</a></div>'
        self.assertContains(response, expected, count=1, status_code=200)

        expected = '<div class="text"><a href="?o=3">Question type</a></div>'
        self.assertContains(response, expected, count=1, status_code=200)

        expected = '<div class="text"><a href="?o=4">Required</a></div>'
        self.assertContains(response, expected, count=1, status_code=200)
