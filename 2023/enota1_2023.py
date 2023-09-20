from utilities import start_tests, WebLink, AudioLink, start_tests_ita2slo

from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, Gender

# sloveno, traduzione, tipo, note, unità

enota = {}

# TODO: supporto significati multipli
# es: ("novica", ("notizia", "novità"))

enota[1] = (
    ("enota", "unità"),
    ("plačati", "pagare", WordType.VERB, WebLink("https://app.glosbe.com/audio/183515:0004896222"), AudioLink("https://glosbe.com/fb_aud/mp3/dB4896222_audio-by-183515.mp3")),
    ("plačilo", "pagamento", WebLink("https://it.glosbe.com/sl/it/pla%C4%8Dilo")),
    ("plačljiv", "pagabile"), # "a pagamento"
    ("slovar", "dizionario"),
    ("svet", "mondo"),
    ("svetovati", "consigliare", WordType.VERB),
    ("svetovalec", "consigliere"),
    ("dnevne novice", "notizie del giorno"),
    ("dnevnik", "diario"), # "giornale"
    ("a veste?", "lo sapete?"),
    ("kriza", "crisi"),
    ("plača", "stipendio", WebLink("https://app.glosbe.com/audio/166556:0002382616"), AudioLink("https://glosbe.com/fb_aud/mp3/e22382616_audio-by-166556.mp3")),
    ("kaj", "cosa"),
    ("vaš", "vostro"),
    ("beseda", "parola"),
    ("besedilo", "testo"),
    ("če ste spregledali", "se avete perso", WebLink("https://it.glosbe.com/sl/it/%C4%8De%20ste%20spregledali")),
    ("Ne najdem besed", "Non trovo le parole", WebLink("https://it.glosbe.com/sl/it/Ne%20najdem%20besed")),
    ("novica", "notizia", WebLink("https://it.glosbe.com/sl/it/novica")), # "novità"
    ("novice", "notiziario", WebLink("https://it.glosbe.com/sl/it/novice")),
    ("prenos", "trasmissione", WebLink("https://it.glosbe.com/sl/it/prenos")), # trasferimento, cessione
)


def run_me():
    print("1 - test da sloveno a italiano")
    print("2 - test da italiano a sloveno")
    data = input("risposta (q per uscire): ")
    if data is None or data == "q":
        return
    elif data == "1":
        start_tests(enota, int_seed=None)
    elif data == "2":
        start_tests_ita2slo(enota, int_seed=None)
    else:
        print("risposta non valida")


if __name__ == "__main__":
    run_me()
