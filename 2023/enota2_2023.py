from utilities import start_tests, process_dictionary

enota = {}

# č š ž
enota[2] = (
    ("kaj je na slikah?", "cosa c'è nelle foto?"),
    ("tekme", "partite"),
    ("concert", "concerto"),
    ("nedelja", "domenica"),
    ("ponedeljek", "lunedì"),
    ("predstava ", "spettacolo"),
    ("pozor!", "attenzione!"),
    ("tekmovanja", "gare"), # 20231017
    ("rekreacija", "attività sportiva"),
    ("vabilo", "invito"),
    ("nedelja", "domenica"),
    ("ponedeljek", "lunedì"),
    ("tek", "corsa"),
    ("slike", "immagini"),
    ("smučanje", "sci"),
    ("je vcasih", "è a volte"),
    ("trenirala", "ha allenato"),
    ("festival je bil dober", "il festival è stato buono"),
    ("mi smo", "noi siamo"),
    ("tekmovanja ali rekreacija?", ""),
    ("katere besede imamo?", "che parole abbiamo?"),
    ("odgovor", "risposta"),
    ("zmagala", "ha vinto"),
    ("dobila kolajno", "ha ricevuto una medaglia"),
    ("v redu", "va bene"),
    ("je dvanajsta", "è la dodicesima"),
    ("olimpijskih igrah", "giochi olimpici"),
    ("seveda", "certo"),
    ("nisem tekla", "non ho corso"),
    ("mož je zelo ponosen", "mio marito è molto orgoglioso"),
    ("kje ste bili prejsnji vikend" , "dove siete stati il weekend scorso"),
    ("kdo je pri vas na obisku?", "chi è in visita da voi?"),
    ("o meni", "su di me"),
    ("o tebi", "su di te"),
    ("o njem", "su di lui"),
    ("o njej", "su di lei"),
    ("o vas", "su di voi"),
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
