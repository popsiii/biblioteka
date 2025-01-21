from django.contrib import admin

from .models import HistoriaWypozyczen, Uzytkownik, Ksiazka, Gatunek, Wypozyczenia, Autor
admin.site.register(Uzytkownik)
admin.site.register(Ksiazka)
admin.site.register(Gatunek)



class AutorAdmin(admin.ModelAdmin) :
    list_display = ("imie_autora", "nazwisko_autora")

admin.site.register(Autor, AutorAdmin)


admin.register(Uzytkownik)
class UzytkownikAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'email', 'plec', 'data_dodania')



class WypozyczeniaAdmin(admin.ModelAdmin) :
    list_display = ("uzytkownik", "ksiazka", "data_wypozyczenia")

admin.site.register(Wypozyczenia, WypozyczeniaAdmin)



class HistoriaWypozyczenAdmin(admin.ModelAdmin) :
    list_display = ("uzytkownik", "ksiazka", "data_wypozyczenia", "data_zwrotu")

admin.site.register(HistoriaWypozyczen, HistoriaWypozyczenAdmin)

