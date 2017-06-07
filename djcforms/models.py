from django.db import models


class Question(models.Model):
    question_type_choices = (
        ('singlelinetext', 'Single Line Text'),
        ('paragraphtext', 'Paragraph Text'),
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=50
    )
    text = models.TextField(
        null=False,
        blank=False
    )
    question_type = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        choices=question_type_choices
    )
    required = models.BooleanField(null=False, blank=False)
