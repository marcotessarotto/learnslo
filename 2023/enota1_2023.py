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
    ("novica", ("notizia", "novità"), WebLink("https://it.glosbe.com/sl/it/novica")), # "novità"
    ("novice", "notiziario", WebLink("https://it.glosbe.com/sl/it/novice")),
    ("prenos", "trasmissione", WebLink("https://it.glosbe.com/sl/it/prenos")), # trasferimento, cessione
    # 20230926
    ("denarnica", "portafoglio"),
    ("denar", "denaro"),
    ("kreditna kartica", "carta di credito"),
    ("oprosti, je to tvoja denarnica?", "scusi, è il tuo portafoglio?"),
    ("neurje", ("temporale", "tempesta")),
    # https://www.rainews.it/tgr/fjk/articoli/2023/09/libija-neurje-daniel-povzrocil-3000-mrtvih-in-10000-pogresanih-f725fca7-fe65-47d6-8e65-70a4a784f814.html
    ("nevihta", "temporale"),
    ("neurje povzročilo mrtvih in pogrešanih", "la tempesta ha causato morti e dispersi"),
    ("povzročiti", "causare"),
    ("povzročil", "causato"),
    ("pogrešani", "dispersi"),
    # ("pogrešan", "disperso"),
    # ("pogrešana", "dispersa"),
    # ("pogrešano", "disperso"),
    ("pogrešana oseba", "persona dispersa"),
    ("oseba", "persona"),
    ("pogrešati", ("mancare", "perdere", "sentire la mancanza"), WebLink("https://it.glosbe.com/sl/it/pogre%C5%A1ati")),
    ("pogrešam te", "mi manchi"),
    ("pogrešam", "mi mancano"),
    ("pogrešal", "mancato"),
    # ("pogrešala", "mancata"),
    # ("pogrešalo", "mancato"),
    # ("pogrešali", "mancato"),
    ("ni za kaj", "non c'è di che"),
    ("izvoli", ("prego", "ecco"), WebLink("https://it.glosbe.com/sl/it/izvoli")),
    ("kaj je vidite?", "cosa vedete?"),

    ("Henrik prihaja iz finske", "Henrik viene dalla Finlandia"),
    ("Eno leto bo živel v Sloveniji", "Vivrà in Slovenia per un anno"),
    ("kaj je povedal Martin?", "cosa ha detto Martin?"), # pag. 7

    # slovenska beseda C Zivo 1b Sb, pag. 7

    ("vi zdaj stanuje tukaj?", "adesso abitate qui?"),
    ("jaz zem soseda iz prvega nadstopja", "io sono il vicino del primo piano"),
    ("me veseli", "piacere"),
    ("a bobne igrate", "suonate la batteria?"),
    ("veste, tukaj je ob desetih zvecer mir", "sapete, qui alle dieci di sera c'è silenzio"),
    ("tukaj", "qui"),
    ("seveda", ("certo", "ovviamente")),
    ("mir", ("silenzio", "pace", "tranquillità")),
    ("je ob desetih","è alle dieci"),
    ("rada imam mir", "mi piace la tranquillità"),
    ("rada", "piace"),
    ("veste", "sapete"),
    ("da imamo novega soseda", "abbiamo un nuovo vicino"),
    ("Henrik igra bobne", "Henrik suona la batteria"),
    ("zakaj", "perché"),
    ("martin se uči slovenščine", "martin sta imparando lo sloveno"),
    ("pogovarjati", "parlare"), # dialogare, interagire
    ("odgovor", "risposta"),
    ("odgovoriti", "rispondere"),
    ("katere jezike govoriš?", "quali lingue parli?"),
    ("delovni zvezek", "Quaderno di lavoro"),
    ("ucbenik", "libro di testo"),
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
