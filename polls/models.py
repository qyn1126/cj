from django.db import models
from django.utils import timezone
import datetime
class Questionaire(models.Model):
    questionaire_text = models.CharField('问卷名称',max_length=200)
    pub_date = models.DateTimeField('开始时间',default=timezone.now,)
    end_time = models.DateTimeField('结束时间',default=timezone.now()+datetime.timedelta(days=10))
    questionaire_uid= models.BigIntegerField('序号',default=0)
    drawnd = models.BooleanField(default=False, help_text='是否抽过奖')
    class Meta:
        verbose_name = "Questionaire"
        verbose_name_plural = "试卷"
    def __str__(self):
        return self.questionaire_text
class Question(models.Model):
    questionaire = models.ForeignKey(Questionaire, on_delete=models.CASCADE,help_text='问题所在问卷')
    pub_date = models.DateTimeField('问题创建时间' ,default=timezone.now())
    question_text = models.CharField('问题内容',max_length=200,help_text='问题内容')
    number= models.IntegerField(default=0)
    sf = models.BooleanField('是否多选',default=False)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "问题"
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('答案内容',max_length=200,help_text='需要加上选项字母，如"A.答案内容"')
    votes = models.IntegerField('答案分数',default=0,help_text='正确为一分，多选题非正确选项为-5分')
    answer = models.BooleanField(default = False)
    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "选项"
    def __str__(self):
        return self.choice_text
class answer(models.Model):
    questionaire = models.ForeignKey(Questionaire,on_delete=models.CASCADE)
    answer_name = models.CharField('答题人姓名',max_length=200)
    answer_choice = models.CharField('答题人的答案',max_length=200,default='')
    answer_email = models.EmailField('答案人人数',default=0)
    answer_number = models.IntegerField('答题人分数',default=0)
    answer_phonenumber=models.BigIntegerField('答案人电话号码',default=0)
    #是否中奖 = models.BooleanField(default=False)
    drawn = models.BooleanField('是否中奖',default=False)
    answer_drawn = models.CharField('奖品',max_length=200, default='未中奖')
    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "回答者"
    def __str__(self):
        return self.answer_name

class think(models.Model):
    think_text = models.CharField('抽奖方案名称',max_length=200,)
    votes = models.IntegerField('抽奖方案序号',default=0,)
    class Meta:
        verbose_name = "think"
        verbose_name_plural = "抽奖方案"
    def __str__(self):
        return self.think_text
class gt(models.Model):
    think = models.ForeignKey(think,on_delete=models.CASCADE)
    name = models.CharField('奖品名称',max_length=200,)
    num = models.IntegerField('获奖人数',default=0,)
    votes = models.IntegerField('获奖最低分数', default=0,help_text='优先从分数高的抽取')
    class Meta:
        verbose_name = "gt"
        verbose_name_plural = "奖品"
    def __str__(self):
        return self.name