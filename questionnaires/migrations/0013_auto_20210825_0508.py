# Generated by Django 3.1.13 on 2021-08-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0012_auto_20210827_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizformfield',
            name='skip_logic',
        ),
        migrations.AlterField(
            model_name='quizformfield',
            name='choices',
            field=models.TextField(blank=True, help_text='Pipe (|) separated list of choices.', verbose_name='choices'),
        ),
    ]
