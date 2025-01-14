from datetime import date
from django.db import models
from django.contrib.auth.models import User 

PLEC = models.IntegerChoices('Płeć', 'Kobieta Męzczyzna Inna Nie_chcę_podawać')

class Uzytkownik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='uzytkownik')
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    plec = models.IntegerField(choices=PLEC.choices, default=PLEC.choices, default = "-" )
    data_dodania = models.DateField(default=date.today, blank=False, null=False)


    



