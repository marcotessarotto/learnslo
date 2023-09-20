from utilities import start_tests, WebLink, AudioLink

from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, Gender

# sloveno, traduzione, tipo, note, unità

enota = {}

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
    ("dnevnik", "diario"),
    ("a veste?", "lo sapete?"),
    ("kriza", "crisi"),
    ("plača", "stipendio", WebLink("https://app.glosbe.com/audio/166556:0002382616"), AudioLink("https://glosbe.com/fb_aud/mp3/e22382616_audio-by-166556.mp3")),
    ("kaj", "cosa"),
    ("vaš", "vostro"),
    ("beseda", "parola"),
    ("besedilo", "testo"),
    ("če ste spregledali", "se avete perso", WebLink("https://it.glosbe.com/sl/it/%C4%8De%20ste%20spregledali")),

)


def run_me():
    start_tests(enota, int_seed=None)


if __name__ == "__main__":
    run_me()
