from django.contrib import admin
from .models import *

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
admin.site.register(Question,QuestionAdmin)

admin.site.register(Choice)
admin.site.register(answer)