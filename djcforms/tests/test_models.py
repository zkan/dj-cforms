from django.test import TestCase

from ..models import Question


class QuestionTest(TestCase):
    def test_save_new_question(self):
        question = Question()
        question.name = 'favorite_color'
        question.text = 'What is your favorite color?'
        question.question_type = 'singlelinetext'
        question.required = True
        question.save()

        question = Question.objects.last()

        self.assertEqual(question.name, 'favorite_color')
        self.assertEqual(question.text, 'What is your favorite color?')
        self.assertEqual(question.question_type, 'singlelinetext')
        self.assertTrue(question.required)

    def test_question_should_have_defined_question_type_choices(self):
        question = Question()

        expected = (
            ('singlelinetext', 'Single Line Text'),
            ('paragraphtext', 'Paragraph Text'),
        )
        self.assertEqual(question.question_type_choices, expected)
