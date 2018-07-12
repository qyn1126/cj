# Generated by Django 2.0.7 on 2018-07-10 16:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_name', models.CharField(max_length=200)),
                ('answer_choice', models.CharField(default='', max_length=200)),
                ('answer_email', models.EmailField(default=0, max_length=254)),
                ('answer_number', models.IntegerField(default=0)),
                ('answer_phonenumber', models.BigIntegerField(default=0)),
                ('drawn', models.BooleanField(default=False, help_text='是否中奖')),
                ('answer_drawn', models.CharField(default='', help_text='奖品', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('answer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('number', models.IntegerField(default=0)),
                ('sf', models.BooleanField(default=False, help_text='是否是多选')),
            ],
        ),
        migrations.CreateModel(
            name='Questionaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionaire_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, help_text='开始时间')),
                ('end_time', models.DateTimeField(default=datetime.datetime(2018, 7, 20, 16, 33, 30, 405494), help_text='结束时间')),
                ('questionaire_uid', models.BigIntegerField(default=0)),
                ('drawnd', models.BooleanField(default=False, help_text='是否抽过奖')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='questionaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Questionaire'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='questionaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Questionaire'),
        ),
    ]
