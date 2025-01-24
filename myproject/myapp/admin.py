from django.contrib import admin

from .models import Autor, HistoriaWypozyczen, Uzytkownik, Ksiazka, Gatunek, Wypozyczenia
admin.site.register(Uzytkownik)
admin.site.register(Gatunek)




class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'get_autor', 'rok_wydania', 'ISBN')

    def get_autor(self, obj):
        return ", ".join([str(autor) for autor in obj.autor.all()])
    get_autor.short_description = 'Autor'

    filter_horizontal = ('gatunek',)

admin.site.register(Ksiazka, KsiazkaAdmin)


class AutorAdmin(admin.ModelAdmin):
    list_display = ('imie_autora', 'nazwisko_autora')

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



