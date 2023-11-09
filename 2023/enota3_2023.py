from utilities import start_tests, process_dictionary

enota = {}

""" pag. 34
na dan brez avtomobila, 22. septembra, pustimo avto doma in se sprehodimo po mestnih ulicah ali uživamo v kolesarjeniu po središču mesta.

dan brez avtomobila bo poteakl na Brezovici, v Celiu, Gornji Radgoni, Gornjih Petrovcih, Kopru, Kranju, Ljubljani, Mariboru, Murski Soboti, Novi Gorici, Postojni, Radovljci, Slovenj Gradcu, Trbovliah, na Vrhniki in v Zagorju ob Savi. Ceste brez avtomobila lahko postanejo naša nova razvada.

Lepo je, če ...
- se vsaj enkrat spehodimo na delo ali pa se odpeljemo s kolesom,
- začnemo uporabljati javni prevoz
- se peljemo z avtomobilom in za sopotnike vzamemo svoie sodelavce ali kolege

domande:

kdaj je dan brez avtomobila?
kaj lahko delamo ta dan?
kje v Sloveniji organizirajo dan brez avtomobila?

"""

# č š ž
enota[3] = (
    ("kolesarjeti", "andare in bicicletta"),
    ("brez", "senza"),
    ("na dan", "in un giorno"),
    ("na dan brez", "in un giorno senza"),
    ("na dan brez avtomobila", "in un giorno senza automobile"),
    ("pustimo", "lasciamo"),
    ("pustiti", "lasciare"),
    ("pustimo avto doma", "lasciamo l'auto a casa"),
    ("se sprehodimo po mestnih ulicah", "facciamo una passeggiata per le strade della città"),
    ("sprehoditi", "fare una passeggiata"),
    ("ulica", "strada"),
    ("mesto", "città"),
    ("po", "per"),
    ("ali", "o"),
    ("uživamo", "godiamo"),
    ("uživamo v kolesarjeniu", "godiamo in bicicletta"),
    ("po središču mesta", "per il centro della città"),
    ("središče mesta", "centro della città"),
    ("kdaj", "quando"),
    ("kdaj je ", "quando è "),
    ("kdaj je dan", "quando è il giorno"),
    ("kdaj je dan brez avtomobila?", "quando è il giorno senza automobile?"),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
)


def run_me():
    dict_slo, dict_ita = process_dictionary(enota)

    number_of_answers = 10

    print("1 - test da sloveno a italiano")
    print("2 - test da italiano a sloveno")
    data = input("risposta (q per uscire): ")
    if data is None or data == "q":
        return
    elif data == "1":
        start_tests(dict_slo, number_of_answers=number_of_answers)
    elif data == "2":
        start_tests(dict_ita, slo2ita=False, number_of_answers=number_of_answers)
    else:
        print("risposta non valida")


if __name__ == "__main__":
    run_me()
