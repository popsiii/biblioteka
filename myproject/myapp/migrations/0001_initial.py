# Generated by Django 5.1.2 on 2025-01-20 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=60)),
                ('nazwisko', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('plec', models.IntegerField(choices=[(1, 'Kobieta'), (2, 'Męzczyzna'), (3, 'Inna'), (4, 'Nie Chcę Podawać')], default=1)),
                ('data_dodania', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name': 'Użytkownik',
                'verbose_name_plural': 'Użytkownicy',
            },
        ),
    ]