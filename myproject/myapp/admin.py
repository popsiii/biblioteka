from django.contrib import admin

from .models import Uzytkownik
admin.site.register(Uzytkownik)

admin.register(Uzytkownik)
class UzytkownikAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'email', 'plec', 'data_dodania')