# Generated by Django 4.1.3 on 2022-12-05 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('trade_code', models.CharField(max_length=50)),
                ('high', models.CharField(max_length=50)),
                ('low', models.CharField(max_length=50)),
                ('open', models.CharField(max_length=50)),
                ('close', models.CharField(max_length=50)),
                ('volume', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JsonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('trade_code', models.CharField(max_length=50)),
                ('high', models.CharField(max_length=50)),
                ('low', models.CharField(max_length=50)),
                ('open', models.CharField(max_length=50)),
                ('close', models.CharField(max_length=50)),
                ('volume', models.CharField(max_length=50)),
            ],
        ),
    ]
