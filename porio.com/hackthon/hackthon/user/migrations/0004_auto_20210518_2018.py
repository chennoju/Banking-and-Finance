# Generated by Django 3.2.3 on 2021-05-18 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_banklist_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banklist',
            name='maxamount',
        ),
        migrations.RemoveField(
            model_name='banklist',
            name='minsaly',
        ),
    ]
