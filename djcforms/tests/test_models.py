from django.test import TestCase

from ..models import Question


class QuestionTest(TestCase):
    def setUp(self):
        self.question = Question()

    def test_save_new_question(self):
        self.question.name = 'favorite_color'
        self.question.text = 'What is your favorite color?'
        self.question.question_type = 'singlelinetext'
        self.question.required = True
        self.question.save()

        question = Question.objects.last()

        self.assertEqual(question.name, 'favorite_color')
        self.assertEqual(question.text, 'What is your favorite color?')
        self.assertEqual(question.question_type, 'singlelinetext')
        self.assertTrue(question.required)

    def test_question_should_have_defined_question_type_choices(self):
        expected = (
            ('singlelinetext', 'Single Line Text'),
            ('paragraphtext', 'Paragraph Text'),
        )
        self.assertEqual(self.question.question_type_choices, expected)
