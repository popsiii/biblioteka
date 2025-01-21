from datetime import date
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.core.validators import RegexValidator

PLEC = models.IntegerChoices('Płeć', 'Kobieta Męzczyzna Inna Nie_chcę_podawać')

class Uzytkownik(AbstractUser):
    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    plec = models.IntegerField(choices=PLEC.choices, default=PLEC.Kobieta)  
    data_dodania = models.DateField(default=date.today, blank=False, null=False)

    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.email})"

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

WYDAWNICTWA = models.IntegerChoices(
    'Wydawnictwo',
    'Inne'
    'Agencja_Dramatu_i_Teatru '
    'Agencja_Wydawnicza_Runa '
    'Agencja_Wydawniczo_Reklamowa_Skarpa_Warszawska '
    'Alkazar '
    'Alma_Press '
    'Ameet '
    'Franciszkańskie_Wydawnictwo_św_Antoniego '
    'ArtRage '
    'Bellona '
    'Biały_Kruk '
    'Biuro_Literackie '
    'Bogucki_Wydawnictwo_Naukowe '
    'CIA_Books '
    'Convivo '
    'Czuły_Barbarzyńca_Press '
    'Dom_Literatury_w_Łodzi '
    'Dom_Wydawniczy_Elipsa '
    'Dom_Wydawniczy_Rebis '
    'Doświadczalna_Oficyna_Graficzna '
    'Drzewo_Babel '
    'Edycja_Świętego_Pawła '
    'Elamed_Media_Group '
    'Elay '
    'Eneteia_Wydawnictwo_Szkolenia '
    'EscapeMagazine_pl '
    'Fabryka_Słów '
    'Flos_Carmeli '
    'Fundacja_Duży_Format '
    'Fundacja_Festina_Lente '
    'Fundacja_Instytut_Wydawniczy_Książka_i_Presa '
    'Gdańskie_Wydawnictwo_Psychologiczne '
    'Gebethner_i_Wolff '
    'Genius_Creations '
    'Hejnał '
    'Homo_Dei '
    'Towarzystwo_Wydawnicze_Ignis '
    'Inforteditions '
    'Insignis_Media '
    'Instytut_im_Oskara_Kolberga '
    'Instytut_Wydawniczy_Pax '
    'Instytut_Wydawniczy_Latarnik '
    'ISA '
    'Wydawnictwo_Kle '
    'Klub_dla_Ciebie '
    'Kolegium_Europy_Wschodniej_im_Jana_Nowaka_Jeziorańskiego '
    'Krakowska_Spółka_Wydawnicza '
    'Książka_i_Wiedza '
    'Książnica_Atlas '
    'Księgarnia_Akademicka '
    'Księży_Młyn_Dom_Wydawniczy '
    'Kurhaus_Publishing '
    'Wydawnictwo_Kusiński '
    'Lampa_i_Iskra_Boża '
    'Wydawnictwo_Literackie '
    'Wydawnictwo_Literatura '
    'Ludowa_Spółdzielnia_Wydawnicza '
    'Ładne_Halo '
    'Mamiko '
    'Marpress '
    'Media_Rodzina '
    'Młodzieżowa_Agencja_Wydawnicza '
    'Muza '
    'Mystic_Production '
    'Neriton '
    'Wydawnictwo_Nisza '
    'Noir_sur_Blanc '
    'Norbertinum '
    'Wydawnictwo_Novae_Res '
    'Nowy_Świat '
    'Wydawnictwo_Officyna '
    'Oficyna_21 '
    'Oficyna_Naukowa '
    'Oficyna_Wydawnicza_Rytm '
    'Oficyna_Wydawnicza_Vocatio '
    'Oficyna_Wydawnicza_Arax '
    'Oficyna_Wydawnicza_Atut '
    'Oficyna_Wydawnicza_Impuls '
    'Oficyna_Wydawnicza_Volumen '
    'Okultura '
    'Państwowy_Instytut_Wydawniczy '
    'Phantom_Press '
    'Polskie_Książki_Telefoniczne '
    'Polskie_Przedsiębiorstwo_Wydawnictw_Kartograficznych '
    'Polskie_Wydawnictwo_Ekonomiczne '
    'Powszechne_Wydawnictwo_Rolnicze_i_Leśne '
    'Presscom '
    'Prodoks '
    'Prószyński_i_Ska '
    'Rosikon_Press '
    'Towarzystwo_Wydawnicze_Rój '
    'Wydawnictwo_Salwator '
    'Słowo_Prawdy '
    'Słowo_obraz_terytoria '
    'Smak_Słowa '
    'Społeczny_Instytut_Wydawniczy_Znak '
    'Spółdzielnia_Wydawnicza_Czytelnik '
    'Spółdzielnia_Wydawnicza_Książka '
    'Wydawnictwo_Stalker_Books '
    'Stowarzyszenie_Salon_Literacki '
    'Świat_Książki '
    'Tern_Book '
    'Towarzystwo_Autorów_i_Wydawców_Prac_Naukowych_Universitas '
    'W_drodze '
    'WarBook '
    'Wiedza_i_Praktyka '
    'Wydawnictwo_Wolno '
    'Wolters_Kluwer_Polska '
    'Wydawnictwa_Akademickie_i_Profesjonalne '
    'Wydawnictwa_Artystyczne_i_Filmowe '
    'Wydawnictwa_Naukowo_Techniczne '
    'Wydawnictwa_Polskiego_Komitetu_Olimpijskiego '
    'Wydawnictwa_Szkolne_i_Pedagogiczne '
    'Wydawnictwa_Uniwersytetu_Warszawskiego '
    'Wydawnictwo_Nasza_Księgarnia '
    'Wydawnictwo_Wiedza_Powszechna '
    'Wydawnictwo_a5 '
    'Wydawnictwo_Adam_Marszałek '
    'Wydawnictwo_Akademickie_Dialog '
    'Wydawnictwo_Albatros '
    'Wydawnictwo_Aletheia '
    'Wydawnictwo_Alfa '
    'Wydawnictwo_Amber '
    'Wydawnictwo_Anagram '
    'Wydawnictwo_Archidiecezji_Lubelskiej_Gaudium '
    'Wydawnictwo_Armoryka '
    'Wydawnictwo_Astrum '
    'Wydawnictwo_Bajka '
    'Wydawnictwo_Buchmann '
    'Wydawnictwo_CiS '
    'Wydawnictwo_CM '
    'Wydawnictwo_Cyklady '
    'Wydawnictwo_Cyranka '
    'Wydawnictwo_Czarna_Owca '
    'Wydawnictwo_Czarne '
    'Wydawnictwo_Czerwone_i_Czarne '
    'Wydawnictwo_Czwarta_Strona '
    'Wydawnictwo_Dolnośląskie '
    'Wydawnictwo_Dowody '
    'Wydawnictwo_Dwie_Siostry '
    'Wydawnictwo_Edukacyjne '
    'Wydawnictwo_Episteme '
    'Wydawnictwo_Europa '
    'Wydawnictwo_FA_art '
    'Wydawnictwo_Forma '
    'Wydawnictwo_Format '
    'Wydawnictwo_Fundacji_Humaniora '
    'Wydawnictwo_Gutenberg '
    'Wydawnictwo_Harcerskie_Horyzonty '
    'Wydawnictwo_Harmonia '
    'Wydawnictwo_IFiS_PAN '
    'Wydawnictwo_Iskry '
    'Wydawnictwo_Jaguar '
    'Wydawnictwo_Karakter '
    'Wydawnictwo_KR '
    'Wydawnictwo_Kropka '
    'Wydawnictwo_Krytyki_Politycznej '
    'Wydawnictwo_Kwadratura '
    'Wydawnictwo_Lekarskie_PZWL '
    'Wydawnictwo_Lubelskie '
    'Wydawnictwo_Łódzkie '
    'Wydawnictwo_Mag '
    'Wydawnictwo_Marabut '
    'Wydawnictwo_Marek_Derewiecki '
    'Wydawnictwo_Marginesy '
    'Wydawnictwo_Medyk '
    'Wydawnictwo_MG '
    'Wydawnictwo_Miejskie_Posnania '
    'Wydawnictwo_Miniatura '
    'Wydawnictwo_Morskie '
    'Wydawnictwo_Naukowe_Śląsk '
    'Wydawnictwo_Naukowe_Brama '
    'Wydawnictwo_Naukowe_Dolnośląskiej_Szkoły_Wyższej '
    'Wydawnictwo_Naukowe_PWN '
    'Wydawnictwo_Naukowe_Scholar '
    'Wydawnictwo_Naukowe_Semper '
    'Wydawnictwo_Naukowe_UAM '
    'Wydawnictwo_Naukowe_Uniwersytetu_Mikołaja_Kopernika '
    'Wydawnictwo_papierwdole '
    'Wydawnictwo_Pielgrzym_Polski '
    'Wydawnictwo_Pojezierze '
    'Wydawnictwo_Politechniki_Łódzkiej '
    'Wydawnictwo_Polskie_R_Wegnera '
    'Wydawnictwo_Pomona '
    'Wydawnictwo_Poznańskie '
    'Wydawnictwo_Rabid '
    'Wydawnictwo_RM '
    'Wydawnictwo_Salezjańskie '
    'Wydawnictwo_Sic '
    'Wydawnictwo_Skrzat '
    'Wydawnictwo_Spacja '
    'Wydawnictwo_SQN '
    'Wydawnictwo_SWPS_Academica '
    'Wydawnictwo_Te_Deum '
    'Wydawnictwo_Trio '
    'Wydawnictwo_Trzecie_Oko '
    'Wydawnictwo_UMCS '
    'Wydawnictwo_Uniwersytetu_Ekonomicznego_w_Krakowie '
    'Wydawnictwo_Uniwersytetu_Gdańskiego '
    'Wydawnictwo_Uniwersytetu_Jagiellońskiego '
)

OKLADKA = models.IntegerChoices('okładka', 'twarda miękka')

class Gatunek(models.Model):
    nazwa_gatunku = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa_gatunku
    
    class Meta:
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"



class Ksiazka(models.Model):
    tytul = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    wydawnictwo = models.IntegerField(choices=WYDAWNICTWA.choices)
    rok_wydania = models.CharField(max_length=4)
    liczba_stron = models.IntegerField()
    ISBN = models.CharField(max_length=13)  
    okładka = models.IntegerField(choices=OKLADKA.choices)
    gatunek = models.ManyToManyField(Gatunek)

    def __str__(self):
        return f"{self.tytul} by {self.autor} ({self.rok_wydania})"
    
    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"



class Wypozyczenia(models.Model):
    uzytkownik = models.ForeignKey('Uzytkownik', on_delete=models.CASCADE)
    ksiazka = models.ForeignKey('Ksiazka', on_delete=models.CASCADE)
    data_wypozyczenia = models.DateField(default=now, verbose_name="Data wypożyczenia")

    def __str__(self):
        return f"{self.uzytkownik} wypożyczył/a {self.ksiazka} w dniu {self.data_wypozyczenia.strftime('%Y-%m-%d')}"
    
    class Meta:
        verbose_name = "Wypożyczenie"
        verbose_name_plural = "Wypożyczenia"

class HistoriaWypozyczen(models.Model):
    uzytkownik = models.ForeignKey('Uzytkownik', on_delete=models.SET_NULL, null=True, related_name='historia_wypozyczen')
    ksiazka = models.ForeignKey('Ksiazka', on_delete=models.SET_NULL, null=True, related_name='historia_wypozyczen')
    data_wypozyczenia = models.DateField()
    data_zwrotu = models.DateField(default=now)

    def __str__(self):
        return f"{self.uzytkownik} zwrócił/a {self.ksiazka} (wypożyczona {self.data_wypozyczenia.strftime('%Y-%m-%d')}, zwrócona {self.data_zwrotu.strftime('%Y-%m-%d')})"
    
    class Meta:
        verbose_name = "Historia wypożyczeń"
        verbose_name_plural = "Historia wypożyczeń"