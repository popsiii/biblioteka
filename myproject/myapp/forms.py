# filepath: /Users/werus/biblioteka/myproject/myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Uzytkownik

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Uzytkownik
        fields = ('email', 'imie', 'nazwisko', 'password1', 'password2') 

from .models import Ksiazka

class KsiazkaForm(forms.ModelForm):
    class Meta:
        model = Ksiazka
        fields = ['tytul', 'autor', 'wydawnictwo', 'rok_wydania', 'liczba_stron', 'ISBN', 'okładka', 'gatunek']