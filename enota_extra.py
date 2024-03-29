from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, Gender

extra = {}

# č š ž



extra[1] = (
    ("Kako ti je ime?", "Come è il tuo nome?"),
    ("Kako se reče?", "Come si dice?"),
    ("Kako se piše?", "Come si scrive?"),
    ("Kako greš v službo? ", "Come vai al lavoro?"),
    ("Kako prideš?", "Come vieni?"),
    ("Delam kot natakar", "Lavoro come cameriere"),
    ("Velik je kot oče", "È grande come il padre"),
    ("Danes je vreme lepo kot včeraj", "Oggi il tempo è bello come ieri"),
    ("Kakšen je tvoj prijatelj?", "Com’è il tuo amico?"),
    ("Kakšna je kava?", "Com’è il caffè?"),
    ("Kakšna je hiša?", "Com’è la casa?"),
    ("Kakšno je vreme?", "Com’è  il tempo?"),
    ("DOBER PRIJATELJ", "Buon amico"),
    ("DOBRA PRIJATELJICA", "Buona amica"),
    ("DOBRO PIVO", "Buona birra"),
    ("DOBRO SEM!", "Sto bene"),
    ("DOBRO GOVORIM ITALIJANSKO", "Parlo bene l’italiano"),
    ("DOBRO POZNAM MARKA", "Conosco bene Marko"),
    ("kako si?", "come stai?"),
    ("KAKO GOVORIŠ ITALIJANSKO?", "come parli italiano?"),
    ("LEP POZDRAV", "saluti"),
    ("zdravo", "ciao"),
    ("dobrodošli", "benvenuto"),
    ("pozdravljen", "salutato!"),
    ("LEPO POZDRAVLJEN", "saluti!"),
    ("od kod si?", "da dove vieni?/di dove sei?"),
    ("sem iz Trsta", "sono di Trieste", Gender.MALE),
    ("sem iz Rima", "sono di Roma", Gender.MALE),
    ("sem iz Italije", "vengo dall'Italia", Gender.FEMALE),
    ("sem iz Ljubljane", "vengo da Lubiana", Gender.FEMALE),
    ("sem iz Gradišča", "vengo da Gradisca", Gender.NEUTRAL),
    ("sem iz Celja", "vengo da Celje", Gender.NEUTRAL),
    ("Milje", "Muggia", Gender.FEMALE), # č š ž
    ("Celje", "Celje", Gender.NEUTRAL),
    ("včeraj", "ieri"),
    ("Danes", "oggi"),
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
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
)


def run_me():
    dict_slo, dict_ita = process_dictionary(extra)

    print("1 - test da sloveno a italiano")
    print("2 - test da italiano a sloveno")
    data = input("risposta (q per uscire): ")
    if data is None or data == "q":
        return
    elif data == "1":
        start_tests(dict_slo)
    elif data == "2":
        start_tests(dict_ita, slo2ita=False)
    else:
        print("risposta non valida")


if __name__ == "__main__":
    run_me()
