from django.contrib import admin

from .models import Uzytkownik, Ksiazka, Gatunek
admin.site.register(Uzytkownik)
admin.site.register(Ksiazka)
admin.site.register(Gatunek)

admin.register(Uzytkownik)
class UzytkownikAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'email', 'plec', 'data_dodania')

