from django.contrib import admin

from .models import HistoriaWypozyczen, Uzytkownik, Ksiazka, Gatunek, Wypozyczenia
admin.site.register(Uzytkownik)
admin.site.register(Ksiazka)


admin.site.register(Gatunek)

admin.register(Uzytkownik)
class UzytkownikAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'email', 'plec', 'data_dodania')



class WypozyczeniaAdmin(admin.ModelAdmin) :
    list_display = ("uzytkownik", "ksiazka", "data_wypozyczenia")

admin.site.register(Wypozyczenia, WypozyczeniaAdmin)



class HistoriaWypozyczenAdmin(admin.ModelAdmin) :
    list_display = ("uzytkownik", "ksiazka", "data_wypozyczenia", "data_zwrotu")

admin.site.register(HistoriaWypozyczen, HistoriaWypozyczenAdmin)

