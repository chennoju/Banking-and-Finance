# Generated by Django 3.2.3 on 2021-05-18 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210518_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='loans',
            name='bankname',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
