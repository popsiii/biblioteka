# Generated by Django 5.1.1 on 2025-01-23 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_autor_remove_ksiazka_autor_ksiazka_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autorzy'},
        ),
    ]
