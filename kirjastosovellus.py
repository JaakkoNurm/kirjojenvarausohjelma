kirjat = {}

def tallenna_kirja(kirjat: dict, koodi: str, nimi: str, kirjoittaja: str, vuosi: int):
    kirjat[koodi] = (nimi, kirjoittaja, vuosi)


def onko_kirja(kirjat: dict, koodi: str) -> bool:
    if koodi in kirjat:
        return True
    else:
        return False


def poista_kirja(kirjat: dict, koodi: str) -> bool:
    if koodi in kirjat:
        del kirjat[koodi]
        print("Poistettiin!")
        return True
    else:
        return False


def kirjoittajan_kirjat(kirjat: dict, kirjoittaja: str) -> list:
    tuloste = []

    for kirja in kirjat:
        for kirjailija in kirjat[kirja]:
            if kirjailija == kirjoittaja:
                tuloste.append(kirjat[kirja])

    return tuloste


def tulosta_kirja(kirja: tuple):
    print(f"{kirja[0]} ({kirja[1]}), {kirja[2]}")


while True:
    print("Valitse:")
    print("1. Lisää kirja")
    print("2. Poista kirja")
    print("3. Tulosta kirja")
    print("4. Kirjoittajan kirjat")
    print("0. Poistu")

    valinta = int(input("Valinta: "))

    if valinta == 0:
        break

    if valinta == 1:
        koodi = input("Koodi: ")
        nimi = input("Nimi: ")
        kirjoittaja = input("Kirjoittaja: ")
        vuosi = int(input("Vuosi: "))

        tallenna_kirja(kirjat, koodi, nimi, kirjoittaja, vuosi)

    if valinta == 2:
        koodi = input("Koodi: ")

        poista_kirja(kirjat, koodi)


    if valinta == 3:
        koodi = input("Koodi: ")

        if koodi in kirjat:
            tulosta_kirja(kirjat[koodi])

        else:
            print("Kirjaa ei löytynyt.")

    if valinta == 4:
        kirjoittaja = input("Kirjoittaja: ")
        lista = kirjoittajan_kirjat(kirjat, kirjoittaja)

        if lista == []:
            print("Kirjoja ei löytynyt.")

        else:
            for i in range(len(lista)):
                print(f"{lista[i][0]} ({lista[i][1]}), {lista[i][2]}")

    
