from itemki import Bron, Pancerz, oferta_sklepu, Handlarz, wszystkie_przedmioty
import itemki
from lokacje import zbuduj_swiat
from gracz import Gracz, Thraex, Mirmillon, Retiarius
from walka import walka


def kreator_postaci():
    print("------- STWÓRZ SWOJĄ POSTAĆ ------\n")
    imie = input("Podaj imię swojego bohatera: ")

    print("\nWybierz klasę gladiatora:")
    print("1. Thraex (Agresywny) - Duże obrażenia, średnie HP i zwinność")
    print("2. Mirmillon (Ciężkozbrojny) - Duże HP i mała zwinność")
    print("3. Retiarius (Sieciaż) - Małe HP, duże obrażenia i bardzo duża zwinność")
# wybor klasy gladiatora
    while True:
        wybor = input("Jakim gladiatorem chcesz być? (1-3): ")
        if wybor == "1":
            return Thraex(imie)
        elif wybor == "2":
            return Mirmillon(imie)
        elif wybor == "3":
            return Retiarius(imie)
        else:
            print("\nNieprawidłowy wybór. Proszę wybrać klasę gladiatora (1-3).")


def start_gierki():
    # przywitanie
    print("\n============ WITAJ W STAROŻYTNYM RZYMIE! ============\n")
    print("Jako niewolnik zostałeś przewieziony do Rzymu, by walczyć na arenie.")
    print("Twoim celem jest przetrwać i zdobyć wolność, stając się legendarnym gladiatorem!\n")

# tworzenie gracza i świat
    gracz = kreator_postaci()
    obecna_lokacja = zbuduj_swiat()
    handlarz = Handlarz("Kupiec Binjamin", wszystkie_przedmioty)

    # menu główne
    while True:
        if gracz.walki_na_arenie >= 1 and not gracz.przechodzien:
            print("\n" + "*"*50)
            print(" [WYDARZENIE] Z cienia wyłania się zakapturzona postać...")
            print(" Szemrany przechodzień: ")
            print(" Widziałem jak walczysz. Masz potencjał.")
            print(" Jeśli zdobędziesz 100 punktów chwały, przyjdź w nocy do Katakumb...")
            print(" ...zobaczysz tam coś bardzo ciekawego. - po czym znika w mroku.")
            print("*"*50 + "\n")
            # zmiana na true żeby nie wyskakiwało za kazdym razem
            gracz.przechodzien = True
        print(
            f"\n-----------------------------Jesteś teraz w: {obecna_lokacja.nazwa}-----------------------------")
        print(obecna_lokacja.opis)
        print("\nCo chcesz zrobić?")
# ------------------------------------------------WYŚWIETLANE OPCJE------------------------------------------------
        for kierunek in obecna_lokacja.sciezki.keys():
            print(f"- idz {kierunek}")

    # specjalne activity w danych lokacjach
        # =-=-=-=-=-=-=->LUDUS<-=-=-=-=-=-=-
        if obecna_lokacja.nazwa == "Szkoła Gladiatorów (Ludus)":
            print("- trenuj (Koszty: -2HP, +1 Atak, +1 Zwinność)")
            print("- odpocznij (+5 HP)")
            print("- wykup (Wymagane: 1000g. To twoja szansa na wolność!)")

        # =-=-=-=-=-=-=->FORUM<-=-=-=-=-=-=-
        elif obecna_lokacja.nazwa == "Forum Romanum":
            print("- oferta (Zobacz, co ma do zaoferowania kupiec Binjamin)")
            print("- kup (Wpisz nazwę przedmiotu, np. 'kup Gladius', aby go kupić)")
            print("- sprzedaj (Odsprzedaj swoje przedmioty, np. 'sprzedaj Gladius'kup )")

        # =-=-=-=-=-=-=->KOLOSEUM<-=-=-=-=-=-=-
        elif obecna_lokacja.nazwa == "Koloseum":
            print(
                "- walcz (Stajesz do walki na arenie! Im silniejszy przeciwnik, tym większe nagrody!)")

        # =-=-=-=-=-=-=->KATAKUMBY<-=-=-=-=-=-=-
        elif obecna_lokacja.nazwa == "Mroczne Katakumby":
            print("- zejdz glebiej (Zaryzykuj i zbadaj mrok...)")

        print("- sprawdz statystyki")
        print("- koniec gry (aby zakończyć)")
# ------------------------------------------------LOGIKA WYBORÓW------------------------------------------------
    # bierzemy wpisaną komendę i zmieniamy ją na małe litery
        komenda = input("\n>>>Twój wybór: ").lower()
        if komenda.startswith("idz "):
            # wyciągamy kierunek z komendy(brany tekst od 4 znaku)
            kierunek = komenda[4:]
            if kierunek in obecna_lokacja.sciezki:
                obecna_lokacja = obecna_lokacja.sciezki[kierunek]
            else:
                print("\nNie możesz iść w tym kierunku! Wybierz inną opcję.\n")

        elif komenda == "sprawdz statystyki":
            gracz.statystyki()
        elif komenda == "koniec gry":
            print("\nBogowie Rzymu żegnają Cię. Do zobaczenia!\n")
            break  # przerywa pętlę i kończy program

        # ======LUDUS========
        elif komenda == "trenuj" and obecna_lokacja.nazwa == "Szkoła Gladiatorów (Ludus)":
            gracz.hp -= 2
            gracz.atk += 1
            gracz.zwinnosc += 1
            print(
                f"\nUderzasz w manekina treningowego do utraty tchu. Tracisz 2 HP, ale Twoja siła rośnie! (Obecna siła: {gracz.atk})")

            if gracz.hp <= 0:
                print(
                    "\nIgnorujesz ból i trenujesz dalej. Nagle w klatce piersiowej czujesz ostre kłucie...")
                print("Przetrenowałeś się! Padasz martwy na piasek w Ludusie.")
                print("\n--- KONIEC GRY ---")
                break  # KONIEC GRY ZŁE ZAKOŃCZENIE
            else:
                # jesli więcej niż 0 hp gra toczy się dalej
                print(
                    f"\nTrening przynosi efekty! Twoje umiejętności rosną, ale jesteś trochę zmęczony. (Obecne HP: {gracz.hp}/{gracz.max_hp})")

        elif komenda == "odpocznij" and obecna_lokacja.nazwa == "Szkoła Gladiatorów (Ludus)":
            if gracz.hp >= gracz.max_hp:
                print("\nJesteś już w pełni sił! Nie potrzebujesz odpoczynku.")
            else:
                gracz.hp += 5
                print(
                    f"\nOdpoczynek dodaje Ci sił. Czujesz się lepiej! (Obecne HP: {gracz.hp}/{gracz.max_hp})")

        elif komenda == "wykup" and obecna_lokacja.nazwa == "Szkoła Gladiatorów (Ludus)":
            if gracz.zloto >= 1000:
                print(
                    f"\nRzucasz worek z 1000 sztuk złota pod nogi Lanisty. Otrzymujesz drewniany miecz (Rudis). JESTEŚ WOLNY, {gracz.imie}!")
                print("--- WYGRAŁEŚ GRĘ! ---")

                input("\nNaciśnij Enter, aby zakończyć grę i zamknąć okno...")
                break  # KONIEC GRY DOBRE ZAKOŃCZENIE
            else:
                print(
                    "\nNie masz wystarczająco złota, aby się wykupić. Musisz zdobyć więcej, walcząc na arenie i zbierając łupy!")

        # ========TARG========
        elif komenda == "oferta" and obecna_lokacja.nazwa == "Forum Romanum":
            oferta = oferta_sklepu(gracz)
            print("\nOferta sklepu:")
            print("-" * 20)
            for przedmiot in oferta:
                print(
                    f">{przedmiot.nazwa} (Cena: {przedmiot.cena} zł, Wymagany lvl: {przedmiot.wymagany_lvl})")

        elif komenda.startswith("kup") and obecna_lokacja.nazwa == "Forum Romanum":
            # wyciągamy nazwę przedmiotu z komendy
            nazwa_przedmiotu = komenda[4:]
            oferta = oferta_sklepu(gracz)
            znaleziony_przedmiot = None
            # szukanie itema na liscie
            for przedmiot in oferta:
                if przedmiot.nazwa.lower() == nazwa_przedmiotu.lower():
                    znaleziony_przedmiot = przedmiot
                    break
            # jak znaleziony to kupic
            if znaleziony_przedmiot:
                handlarz.kupowanie(gracz, znaleziony_przedmiot)
            else:
                print(
                    "\nHandlarz krzywi się: 'Nie mam nawet takiego przedmiotu w ofercie?!'")

        elif komenda.startswith("sprzedaj") and obecna_lokacja.nazwa == "Forum Romanum":
            # wyciągamy nazwę przedmiotu z komendy
            nazwa_przedmiotu = komenda[8:]
            handlarz.sprzedawanie(gracz, nazwa_przedmiotu)

        # ========ARENA========
        elif komenda == "walcz" and obecna_lokacja.nazwa == "Koloseum":
            wynik_walki = walka(gracz)

            if wynik_walki == "teleport_do_ludus":
                obecna_lokacja = obecna_lokacja.sciezki["targ"].sciezki["szkola"]
                print(
                    "\n[Budzisz się obolały w swoim łóżku w Ludusie. Przynajmniej żyjesz...]")

        # ========KATAKUMBY========
        elif komenda == "zejdz glebiej" and obecna_lokacja.nazwa == "Mroczne Katakumby":
            if not gracz.katakumby_odkryte:
                if gracz.chwala < 100:
                    print("\n" + "!"*50)
                    print(" Schodzisz głęboko w wilgotne tunele Katakumb.")
                    print(
                        " Nagle z mroku wyłania się tuzin uzbrojonych, zamaskowanych zbirów.")
                    print(
                        " Rzucają się na Ciebie ze wszystkich stron. Bez szans na obronę, giniesz na miejscu.")
                    print("!"*50)
                    print("\n--- KONIEC GRY (ŚMIERĆ W KATAKUMBACH) ---")
                    break  # Przerwanie pętli i koniec gry
                else:
                    print("\n" + "*"*50)
                    print(" Schodzisz głęboko w wilgotne tunele Katakumb.")
                    print(
                        " Otacza Cię banda zamaskowanych zbirów. Jeden z nich wysuwa lśniące, ukryte ostrze z rękawa...")
                    print(
                        " Nagle ich przywódca unosi dłoń: 'Stać! To ten słynny gladiator z areny. Opuśćcie broń.'")
                    print(
                        " Mężczyzna podchodzi bliżej, ściąga kaptur i kładzie Ci rękę na ramieniu.")
                    print(
                        " 'Działamy w mroku, by służyć światłości. Witaj w Bractwie Ukrytych, bracie.'")
                    print(
                        " 'Nasz wspólny wróg to Cesarz. Przyjmij to złoto na lepszy rynsztunek i poznaj nasze sekrety!'")
                    print("*"*50)

                    gracz.atk += 20
                    gracz.zwinnosc += 20
                    gracz.zloto += 300

                    print(
                        f"\n[ ZYSKUJESZ: +20 Atak, +20 Zwinność, +300 Złota! ]")

                    gracz.katakumby_odkryte = True
                    obecna_lokacja.opis = "Mroczne korytarze są teraz niepokojąco ciche. Zbiry zniknęły bez śladu, zabierając swoje sekrety. Oprócz wilgoci, pajęczyn i echa Twoich kroków, nie ma tu już absolutnie nic ciekawego."
            else:
                print("\nJuż zbadałeś te korytarze. Nie ma tu nic więcej do odkrycia.")

        # error alert
        else:
            print(
                "\nNieznana komenda!\n")


if __name__ == "__main__":
    start_gierki()
