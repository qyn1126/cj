from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    number= models.IntegerField(default=0)
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
    answer_name = models.CharField(max_length=200)
    answer_email = models.EmailField(default=0)
    answer_number = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_name

