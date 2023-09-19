from utilities import start_tests, WebLink

from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, Gender

# sloveno, traduzione, tipo, note, unità

enota = {}

enota[1] = (
    ("enota", "unità"),
    ("plačati", "pagare", WordType.VERB, WebLink("https://app.glosbe.com/audio/183515:0004896222")),
    ("plačilo", "pagamento"),
    ("plačljiv", "a pagamento"),
    ("slovar", "dizionario"),
    ("svet", "mondo"),
    ("svetovati", "consigliare", WordType.VERB),
    ("svetovalec", "consigliere"),
    ("dnevne novice", "notizie del giorno"),
    ("dnevnik", "diario"),
    ("a veste?", "lo sapete?"),
    ("kriza", "crisi"),
    ("plača", "stipendio", WebLink("https://app.glosbe.com/audio/166556:0002382616")),
    ("kaj", "cosa"),
    ("vaš", "vostro"),

)


def run_me():
    start_tests(enota, int_seed=None)


if __name__ == "__main__":
    run_me()
