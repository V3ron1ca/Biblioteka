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

    def print(self):
        S = str(self.numer_sezonu)
        E = str(self.numer_odcinka)
        if len(S) < 2:
            S = "0" + S
        if len(E) < 2:
            E = "0" + E

        print(f"{self.tytul} S{S} E{E}")


def get_movies(zbior):
    wynik = []
    for f in zbior:
        if type(f) == Film:
            wynik.append(f)
    return wynik


def get_series(zbior):
    wynik = []
    for s in zbior:
        if type(s) == Serial:
            wynik.append(s)
    return wynik


def search(zbior, title):
    for x in zbior:
        if x.tytul == title:
            return x


def generate_views(zbior):
    if len(zbior) > 0:
        f = choice(zbior)
        f.liczba_odtworzen += randint(1, 100)


if __name__ == '__main__':
    biblioteka = []
    biblioteka.append(Film(tytul="Braveheart", rok_wydania=1998, gatunek="Dramat"))
    biblioteka.append(Serial(tytul="Czarnobyl", rok_wydania=2019, gatunek="Dokumentalny", numer_sezonu=3, numer_odcinka=15))
    biblioteka.append(Serial(tytul="Wataha", rok_wydania=2020, gatunek="Dokumentalny", numer_sezonu=2, numer_odcinka=5))
    biblioteka.append(Film(tytul="Pulp Fiction", rok_wydania=1994, gatunek="Kryminał"))

    for f in biblioteka:
        f.play()
        f.print()

    print("Filmy:")
    for x in get_movies(biblioteka):
        x.print()

    print("Seriale:")
    for x in get_series(biblioteka):
        x.print()

    search(biblioteka, "Czarnobyl").print()

    generate_views(biblioteka)
    print()
    for f in biblioteka:
        f.print()
        print(f"Liczba wyswietlen: {f.liczba_odtworzen}")

print()


def top_titles():
    for w in sorted(biblioteka, key=lambda w: f.liczba_odtworzen):
        w.print()


top_titles()