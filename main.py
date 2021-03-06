from random import randint, choice


class Film:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen = 0):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen

    def play(self):
        self.liczba_odtworzen += 1

    def print(self):
        print(f"{self.tytul} ({self.rok_wydania})")


class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def print(self): #jezeli długość sezonu/odcinków będzie miała wartość jednoliterową to funckja będzie dodawac przed numerem odcinka
        numer_sezonu = str(self.numer_sezonu)  # /sezonu "0" i wtedy wyjdzie np. "S07E02"
        numer_odcinka = str(self.numer_odcinka)
        if len(numer_sezonu) < 2:
            numer_sezonu = "0" + numer_sezonu
        if len(numer_odcinka) < 2:
            numer_odcinka = "0" + numer_odcinka

        print(f"{self.tytul} S{numer_sezonu} E{numer_odcinka}")


def get_movies(zbior):
    wynik = []
    for filmy in zbior:
        if type(filmy) == Film:
            wynik.append(filmy)
    return wynik


def get_series(zbior):
    wynik = []
    for tv_series in zbior:
        if type(tv_series) == Serial:
            wynik.append(tv_series)
    return wynik


def search(zbior, title):
    for szukaj in zbior:
        if szukaj.tytul == title:
            return szukaj


def generate_views(zbior):
    if len(zbior) > 0:
        wyswietlenia = choice(zbior)
        wyswietlenia.liczba_odtworzen += randint(1, 100)


if __name__ == '__main__':
    biblioteka = []
    biblioteka.append(Film(tytul="Braveheart", rok_wydania=1998, gatunek="Dramat"))
    biblioteka.append(Serial(tytul="Czarnobyl", rok_wydania=2019, gatunek="Dokumentalny", numer_sezonu=3, numer_odcinka=15))
    biblioteka.append(Serial(tytul="Wataha", rok_wydania=2020, gatunek="Dokumentalny", numer_sezonu=2, numer_odcinka=5))
    biblioteka.append(Film(tytul="Pulp Fiction", rok_wydania=1994, gatunek="Kryminał"))

    for zbior in biblioteka:
        zbior.play()
        zbior.print()

    print("Filmy:")
    for filmy in get_movies(biblioteka):
        filmy.print()

    print("Seriale:")
    for seriale in get_series(biblioteka):
        seriale.print()

    search(biblioteka, "Czarnobyl").print()

    generate_views(biblioteka)
    print()
    for widok in biblioteka:
        widok.print()
        print(f"Liczba wyswietlen: {widok.liczba_odtworzen}")

print()


def top_titles():
    for topowe_tytuly in sorted(biblioteka, key=lambda topowe_tytuly: widok.liczba_odtworzen):
        topowe_tytuly.print()


top_titles()