from datetime import date
from rest_framework import serializers
from .models import Ksiazka, Uzytkownik, Wypozyczenia, HistoriaWypozyczen

class KsiazkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ksiazka
        fields = ['id', 'tytul', 'autor', 'wydawnictwo', 'rok_wydania', 'liczba_stron', 'ISBN', 'okładka', 'gatunek']

    def validate_liczba(self, value):
        if value <= 0:
            raise serializers.ValidationError("Liczba stron musi być większa niż zero!")
        return value


class UzytkownikSerializer(serializers.ModelSerializer):
    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Pole imię musi zawierać tylko litery!")
        return value
    
    def validate_nazwisko(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Pole imię musi zawierać tylko litery!")
        return value
    
    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Nieprawidłowy adres email!")
        return value

class WypozyczeniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczenia
        fields = ['id', 'uzytkownik', 'ksiazka', 'data_wypozyczenia']

class HistoriaWypozyczenSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaWypozyczen
        fields = ['id', 'uzytkownik', 'ksiazka', 'data_wypozyczenia', 'data_zwrotu']




