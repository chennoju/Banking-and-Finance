# Generated by Django 3.2.3 on 2021-05-19 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminmessages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=1024)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'adminnmessage',
            },
        ),
    ]
