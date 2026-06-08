import random


class przeciwnik:
    def __init__(self, nazwa, max_hp, atk, zwinnosc, nagroda_zloto, nagroda_exp, nagroda_chwala):
        self.nazwa = nazwa
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.zwinnosc = zwinnosc

        self.nagroda_zloto = nagroda_zloto
        self.nagroda_exp = nagroda_exp
        self.nagroda_chwala = nagroda_chwala


def losuj_przeciwnika(lvl_gracza):

    imiona = ["Tytus", "Marcus", "Lucjusz", "Gajusz", "Publiusz", "Aureliusz", "Decjusz", "Sextus", "Flawiusz", "Klaudiusz", "Nero", "Kaligula", "Kommodus", "Spartakus", "Crixus", "Gannicus", "Oenomaus", "Agron", "Clemens", "Carpo", "Hilarus",
              "Rufus", "Priscus", "Diodorus", "Gnaeus", "Vibius", "Lentulus", "Sulla", "Pompejusz", "Cezar", "Brutus", "Kasjusz",  "Vercingetorix", "Boudica", "Arminius", "Viriatus", "Jugurtha", "Mariusz", "Sulla", "Pompejusz", "Cezar", "Brutus", "Kasjusz"]
    nazwa = random.choice(imiona)

    hp = 10 + (lvl_gracza * 5) + random.randint(-5, 5)
    atk = 3 + (lvl_gracza * 2) + random.randint(-1, 1)
    zwinnosc = 2 + (lvl_gracza * 2) + random.randint(-1, 1)

    nagroda_zloto = 20 * lvl_gracza
    nagroda_exp = 40 * lvl_gracza
    nagroda_chwala = 20 + (lvl_gracza * 5)

    return przeciwnik(nazwa, hp, atk, zwinnosc, nagroda_zloto, nagroda_exp, nagroda_chwala)


def walka(gracz):
    wrog = losuj_przeciwnika(gracz.lvl)
    print("\n" + "!"*40)
    print(f" WALKA NA ARENIE: {gracz.imie} vs {wrog.nazwa}!")
    print("!"*40 + "\n")

    # kto zaczyna
    if gracz.zwinnosc >= wrog.zwinnosc:
        print(f"{gracz.imie} jest szybszy i zaczyna pierwszy!")
        tura_gracza = True
    else:
        print(f"{wrog.nazwa} jest szybszy i zaczyna pierwszy!")
        tura_gracza = False

    # pętla walki
    while gracz.hp > 0 and wrog.hp > 0:
        input("\nNaciśnij Enter, aby kontynuować...")
        if tura_gracza:
            # atak gracza
            rzut = random.randint(1, 6)
            obrazenia = gracz.atk + rzut
            wrog.hp -= obrazenia
            print(f"\n{gracz.imie} atakuje {wrog.nazwa} i zadaje {obrazenia} obrażeń! (HP przeciwnika: {max(0, wrog.hp)}/{wrog.max_hp})")
        else:
            # atak przeciwnika
            rzut = random.randint(1, 6)
            obrazenia = wrog.atk + rzut
            gracz.hp -= obrazenia
            print(f"{wrog.nazwa} atakuje {gracz.imie} i zadaje {obrazenia} obrażeń! (Twoje HP: {max(0, gracz.hp)}/{gracz.max_hp})")

        # zmiana tury
        tura_gracza = not tura_gracza

    # wynik walki
    if gracz.hp > 0:
        print("\n" + "="*40)
        print(f"\n{gracz.imie} ZWYCIĘŻA!!! Tłum wiwatuje na Twoją cześć!")
        print(
            f" Zdobywasz: {wrog.nagroda_zloto} złota, {wrog.nagroda_exp} EXP i {wrog.nagroda_chwala} chwały!")
        print("="*40)

        gracz.zloto += wrog.nagroda_zloto
        gracz.dodaj_exp(wrog.nagroda_exp)
        gracz.chwala += wrog.nagroda_chwala
        gracz.walki_na_arenie += 1

        return "wygrana"

    else:
        print("\n" + "="*40)
        print(" PORAŻKA... Padasz na piasek areny, krwawiąc z ran.")
        print(" Cesarz spogląda na tłum... i po chwili namysłu kieruje kciuk w górę!")
        print(" Darowano Ci życie, ale zhańbiony tracisz część złota i chwały.")
        print(" Strażnicy wloką Twoje nieprzytomne ciało do Ludusu...")
        print("="*40)

        gracz.zloto = max(0, gracz.zloto // 2)
        gracz.chwala = max(0, gracz.chwala // 2)
        gracz.dodaj_exp(wrog.nagroda_exp // 2)

        return "teleport_do_ludus"
