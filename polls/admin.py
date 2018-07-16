from django.contrib import admin
from .models import *
from django import forms
from django.core import serializers
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
def export_as_json(modeladmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect("/polls/esc?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))
export_as_json.short_description = "随机抽奖"
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0
class AnswerInline(admin.TabularInline):
    model = answer
    extra = 0
class GtInline(admin.TabularInline):
    model = gt
    extra = 0
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['questionaire','question_text','sf']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
class Answer1(admin.ModelAdmin):
    list_display = ('questionaire','answer_name', 'answer_phonenumber', 'answer_number','answer_choice',)
class think1(admin.ModelAdmin):
    inlines = [GtInline]

class aire(admin.ModelAdmin):
    inlines = [AnswerInline]
    #inlines = [QuestionInline]
    fieldsets = (
        ['Main', {
            'fields': ('questionaire_text', 'questionaire_uid','questionaire_ad','drawnd'),
        }],
        ['Time', {
             'fields': ('pub_date', 'end_time')
        }]
)
    actions = [export_as_json]
admin.site.register(Choice)
admin.site.register(answer,Answer1)
admin.site.register(Questionaire,aire)
admin.site.register(Question,QuestionAdmin)
admin.site.register(think,think1)