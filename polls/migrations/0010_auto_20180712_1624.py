# Generated by Django 2.0.7 on 2018-07-12 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20180712_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'answer', 'verbose_name_plural': '回答者'},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Choice', 'verbose_name_plural': '选项'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': '问题'},
        ),
        migrations.AlterModelOptions(
            name='questionaire',
            options={'verbose_name': 'Questionaire', 'verbose_name_plural': '试卷'},
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 12, 16, 24, 43, 481461), verbose_name='问题创建时间'),
        ),
        migrations.AlterField(
            model_name='questionaire',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 22, 16, 24, 43, 457175), verbose_name='结束时间'),
        ),
    ]
