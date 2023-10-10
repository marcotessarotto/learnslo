from utilities import start_tests, process_dictionary

enota = {}


enota[2] = (
    ("kaj je na slikah?", "cosa c'è nelle foto?"),
    ("tekme", "partite"),
    ("concert", "concerto"),
    ("nedelja", "domenica"),
    ("ponedeljek", "lunedì"),
    ("predstava ", " spettacolo"),
    ("pozor!", " attenzione!"),
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
