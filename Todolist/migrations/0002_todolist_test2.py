# Generated by Django 4.2.4 on 2023-09-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='test2',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
