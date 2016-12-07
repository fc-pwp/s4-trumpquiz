from django.contrib import admin

from .models import Quiz
from .models import Question


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_display_links = ['title']
    search_fields = ['title']

admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'sequence', 'created_at', 'updated_at']
    list_display_links = ['title', 'sequence']
    search_fields = ['title', 'sequence', 'quiz__title']
    list_filter = ['quiz']

admin.site.register(Question, QuestionAdmin)

