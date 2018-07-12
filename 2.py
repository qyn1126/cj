f = request.POST['f']
w = f[:5]
s = 0
for i in w:
    s = s + i
q = answer(answer_name=f[6], answer_email=f[7], answer_number=s)
q.save()

question.id = 100;
action="{% url 'polls:vote'%}" method="post"


from django.contrib import admin
from .models import *

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text','是否多选']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
class Answer1(admin.ModelAdmin):
    list_display = ('answer_name', 'answer_email', 'answer_number','answer_phonrnumber')
admin.site.register(Question,QuestionAdmin)

admin.site.register(Choice)
admin.site.register(answer,Answer1)


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    number= models.IntegerField(default=0)
    是否多选 = models.BooleanField(default=False)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    answer = models.BooleanField(default = False)

    def __str__(self):
        return self.choice_text

class answer(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    #phonenumber = models.ForeignKey(phonenumber, on_delete=models.CASCADE)
    answer_name = models.CharField(max_length=200)
    answer_email = models.EmailField(default=0)
    answer_number = models.IntegerField(default=0)
    answer_phonrnumber = models.BigIntegerField(default=0)
    def __str__(self):
        return self.answer_name



class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text','是否多选']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
class Answer1(admin.ModelAdmin):
    list_display = ('answer_name', 'answer_email', 'answer_number','answer_phonrnumber')
admin.site.register(Question,QuestionAdmin)

admin.site.register(Choice)
admin.site.register(answer,Answer1)