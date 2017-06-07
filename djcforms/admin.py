from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'text',
        'question_type',
        'required'
    )
