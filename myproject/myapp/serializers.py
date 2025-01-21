from rest_framework import serializers
from .models import Ksiazka

class KsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = ['tytul', 'autor', 'wydawnictwo', 'rok_wydania', 'liczba_stron', 'ISBN', 'okładka', 'gatunek']


