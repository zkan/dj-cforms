from django.test import TestCase
from django import forms

from ..forms import CustomForm
from ..models import Question


class CustomFormTest(TestCase):
    def setUp(self):
        self.questions = [
            Question.objects.create(
                name='singlelinetext',
                text='Single Line Text?',
                question_type='singlelinetext',
                required=True
            ),
            Question.objects.create(
                name='paragraphtext',
                text='Paragraph Text?',
                question_type='paragraphtext',
                required=False
            ),
            Question.objects.create(
                name='another_singlelinetext',
                text='Another Single Line Text?',
                question_type='singlelinetext',
                required=True
            ),
        ]

        self.form = CustomForm(self.questions)

    def test_form_should_have_number_of_fields_equals_number_of_questions(
        self
    ):
        self.assertEqual(len(self.form.fields), 3)

    def test_form_should_have_defined_fields_correctly(self):
        fields = [
            (
                'custom_singlelinetext',
                forms.CharField,
                'Single Line Text?',
                True
            ),
            (
                'custom_paragraphtext',
                forms.CharField,
                'Paragraph Text?',
                False
            ),
            (
                'custom_another_singlelinetext',
                forms.CharField,
                'Another Single Line Text?',
                True
            ),
        ]
        for each in fields:
            field_name, field_class, field_text, field_required = each

            self.assertIsInstance(
                self.form.fields[field_name],
                field_class
            )
            self.assertEqual(
                self.form.fields[field_name].label,
                field_text
            )
            self.assertEqual(
                self.form.fields[field_name].required,
                field_required
            )

    def test_singlelinetext_should_have_textinput_widget(self):
        self.assertIsInstance(
            self.form.fields['custom_singlelinetext'].widget,
            forms.TextInput
        )
        self.assertEqual(
            self.form.fields['custom_singlelinetext'].widget.attrs,
            {'class': 'form-control'}
        )

    def test_paragraphtext_should_have_textarea_widget(self):
        self.assertIsInstance(
            self.form.fields['custom_paragraphtext'].widget,
            forms.Textarea
        )
        self.assertEqual(
            self.form.fields['custom_paragraphtext'].widget.attrs,
            {'class': 'form-control', u'cols': u'40', u'rows': 4}
        )
