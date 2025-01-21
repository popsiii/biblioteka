from datetime import date
from rest_framework import serializers
from .models import Gatunek, Ksiazka, Uzytkownik 


class UzytkownikSerializer(serializers.ModelSerializer):
    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Pole 'imie' musi zawierać tylko litery ")
        return value 

    def validate_nazwisko(self, value):
            if not value.isalpha():
                raise serializers.ValidationError("Pole 'nazwisko' musi zawierać tylko litery ")
            return value 

    class Meta:
        model = Uzytkownik 
        fields = ['id', 'imie', 'nazwisko', 'plec', 'data_dodania', "email"]
        read_only_fields = ['id']

class GatunekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatunek
        fields = ['nazwa']
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = ['tytul', 'autor', 'wydawnictwo', 'rok_wydania', 'liczba_stron', 'ISBN', 'okładka', 'gatunek']


