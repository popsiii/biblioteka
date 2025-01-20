from datetime import date
from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import RegexValidator

PLEC = models.IntegerChoices('Płeć', 'Kobieta Męzczyzna Inna Nie_chcę_podawać')

class Uzytkownik(models.Model):
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    plec = models.IntegerField(choices=PLEC.choices, default=PLEC.Kobieta)  # Poprawiono
    data_dodania = models.DateField(default=date.today, blank=False, null=False)

    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.email})"

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

