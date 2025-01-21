from datetime import date
from rest_framework import serializers
from .models import Gatunek, Ksiazka, Uzytkownik 

<<<<<<< HEAD

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
=======
class KsiazkaSerializer(serializers.ModelSerializer):
>>>>>>> 31b6cf79c82ce6c9cc72082ffed60aeb00ee9db2
    class Meta:
        model = Ksiazka
        fields = ['tytul', 'autor', 'wydawnictwo', 'rok_wydania', 'liczba_stron', 'ISBN', 'okładka', 'gatunek']


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

class KsiazkaSerializer(serializers.ModelSerializer):
    def validate_liczba(self, value):
        if value <= 0:
            raise serializers.ValidationError("Liczba stron musi być większa niż zero!")
        return value



