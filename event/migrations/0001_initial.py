# Generated by Django 4.2.1 on 2023-05-13 02:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2023, 5, 13, 2, 5, 0, 734870))),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]