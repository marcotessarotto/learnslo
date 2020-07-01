from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, Gender

enota = {}

enota[2] = (
    ("družina", "famiglia"),
    ("oče", "padre"),
    ("mama", "madre"),
    ("starši", "genitori"),
    ("otrok/otroci", "bambini"),
    ("sin", "figlio"),
    ("hčerka", "figlia"),
    ("brat", "fratello"),
    ("sestra", "sorella"),
    ("dedek", "nonno"),
    ("babica", "nonna"),
    ("vnuk", "nipote"),
    ("vnukinja", "nipotina"),
    ("mož", "marito"),
    ("žena", "moglie"),
    ("fant", "ragazzo"),
    ("punca", "ragazza"),
    ("partner", "partner (m)"),
    ("partnerka", "partner (f)"),
    ("prijatelj", "amico"),
    ("prijateljica", "amica"),
    ("poročen", "sposato"),
    ("ločen", "separato"),
    ("prijatelji", "amici"),
    ("šola", "scuola"),
    ("vrtec", "asilo"),
    ("fakulteta", "facoltà"),
    ("glagoli", "verbi"),
    ("delati", "lavorare"),
    ("biti", "essere"),
    ("govoriti", "parlare"),
    ("hoditi", "camminare"),
    ("imeti", "avere"),
    ("čigav?", "di chi è?", WordType.PRONOUN),
    ("moj", "mio"),
    ("tvoj", "il tuo"),
    ("vaš", "il vostro"),
    ("želite, prosim?", "desidera, prego?"),
    ("dober tek", "buon appetito"),
    ("čestitam!", "congratulazioni!"),
    ("joj, oprostite", "ahi, mi scusi"),
    ("hvala enako", "grazie anche a te"),
    ("je že v redu", "va bene"),
    ("oprosti, a lahko ponoviš?", "scusa, puoi ripetere?"),
    ("oprosti, ne razumem", "scusa, non capisco"),
    ("na zdravje!", "saluti!"),
    ("kakšen je?", "com'è?"),
    ("kakšen", "che cosa"),
    ("mlad", "giovane"),
    ("star", "vecchio"),
    ("suh", "asciutto/magro"),
    ("debel", "di spessore/grasso/obeso"),
    ("majhen", "piccolo"),
    ("velik", "alto"),
    ("lep", "bello"),
    ("grd", "brutto"),
    ("ima dolge lase", "lei ha i capelli lunghi"),
    ("ima kratke lase", "lei ha i capelli corti"),
    ("ima rjave/blond/črne/sive/rdeče lase", "lei ha i capelli castani/biondi/neri/grigi/rossi"),
    ("ima velike oči", "ha occhi grandi"),
    ("ima majhne oči", "ha occhi piccoli"),
    ("ima rjave/modre/ zelene/sive/črne oči", "ha occhi castani/azzurri/ verdi/grigi/neri"),
    ("pijača", "bevanda"),
    ("voda", "acqua"),
    ("mineralna voda", "acqua minerale"),
    ("kava", "caffè"),
    ("čaj", "thè"),
    ("limonada", "limonata"),
    ("pivo", "birra"),
    ("belo vino", "vino bianco"),
    ("rdeče vino", "vino rosso"),
    ("Od kod je družina Martinez?", "da dove viene la famiglia Martinez?"),
    ("Koliko je star oče?", "quanti anni ha il padre?"),
    #("Koliko je star oče?", "da dove viene il padre?"),
    ("Ali mama zdaj dela?", "ma la mamma lavora adesso?"),
    ("Kaj je oče po poklicu?", "cosa fa di mestiere il padre?"),
    ("Kaj študira hčerka?", "cosa sta studiando la figlia?"),
    ("moj brat", "mio fratello"),
    ("tvoj brat", "tuo fratello"),
    ("moja sestra", "mia sorella"),
    ("tvoja sestra", "tua sorella"),
    ("to je moja družina", "questa è la mia famiglia"),
    ("a je to tvoj oče?", "questo è tuo padre?"),
    ("ne, to je moj brat", "no questo è mio fratello"),
    ("a je to tvoja sestra?", "questa è tua sorella?"),
    ("ne, to je moja žena", "no, questa è mia moglie"),
    ("seveda", "ovviamente"),
    ("a je to tvoj telefon?", "è questo il tuo telefono?"),
    ("ja, to je moj telefon", "si, questo è il mio telefono"),
    ("ne, to ni moj telefon", "no, questo non è il mio telefono"),
    ("torba", "borsa/sacchetto"),
    #("cigava je to cigareta?", ""),
    ("čigav cigaret je?", "di chi è la sigaretta?"),
    ("čigave so torbe?", "di chi sono le borse?"),
    ("knjiga", "libro", Gender.FEMALE),
    ("svinčnik", "matita (penna)"),
    ("zvezek", "quaderno"),
    ("ura", "orologio/ora"),
    ("to je moje mleko", "questo è il mio latte"),
    ("gremo na kavo", "andiamo a prendere un caffè"),
    ("kemični svinčnik", "matita chimica (biro)"),
    ("gremo na pico", "andiamo a prendere una pizza"),
    ("kakšen je?", "com'è?"),
    ("čigav je mobitel?", "di chi è il cellulare?", Gender.MALE),
    ("čigava je knjiga?", "di chi è il libro?", Gender.FEMALE),
    ("čigava je pica?", "di chi è la pizza?", Gender.FEMALE),
    ("čigavo je pivo?", "di chi è la birra", Gender.NEUTRAL),
    ("pivo (n)", "birra", Gender.NEUTRAL),
    ("bratov mobitel", "il cellulare del fratello"),
    ("kaj je to?", "cosa è questo?"),
    ("kdo je to?", "chi è questo?"),
    ("to je star telefon", "questo è un vecchio telefono"),
    ("to je stari telefoni", "questi sono vecchi telefoni"),
    ("to je knjiga", "questo è il libro"),
    ("moja sestra je majhna in ni suha", "mia sorella è piccola e non magra"),
    ("kuli", "penna"),
    ("to so mobiteli", "questi sono telefoni"), #???
    ("to so knjige", "questi sono libri"),
    ("to so italijani", "questi sono gli italiani"),
    ("sem v italiji", "sono in Italia"),
    ("a so to italijani?", "questi sono gli italiani?"),
    ("zdaj", "adesso"),
    ("majhna", "piccola"),
    ("suha", "magra"),
    ("mlada", "giovane (f)"),
    ("lepa", "bella"),
    ("stara", "vecchia"),
    ("grda", "brutta"),
    ("velika", "grande (f)"),
    ("debela", "grassa"),
    ("to je moje pivo", "questa è la mia birra", Gender.NEUTRAL),
    ("to je moje vino", "questo è il mio vino", Gender.NEUTRAL),
    ("to je moje mleko", "questo è il mio latte", Gender.NEUTRAL),
    ("on veliko dela", "lui lavora molto"),
    ("jas imam črne lase ", "io ho i capelli neri"),
    ("moj brat je velik in debel", "mio fratello è grande e grasso"),
    ("moj oče je star in velik", "mio padre è vecchio e grande"),
    ("moja prijateljica", "la mia amica"),
    ("moj prijatelj", "il mio amico"),
    ("vedno je vesel", "è sempre allegro"), # č š ž
    ("vesel", "allegro"),
    ("je zelo prijazen", "è molto amichevole"),
    ("prijazen", "amichevole"),
    ("ona je lepa in suha", "lei è bella e magra"),
    ("star je 46 let", "ha 46 anni"),
    ("mož je star 46 let", "il marito ha 46 anni"),
    ("sin po poklicu je študent", "il figlio studia all'università"),
    ("hčerca je majhna in suha", "la figlia è piccola e magra"),
    ("hčerca je velika in suha", "la figlia è grande e magra"),
    ("hčerca je velika in debela", "la figlia è grande e grassa"),
    ("ona ima sive lase in modre oči", "lei hai capelli grigi e gli occhi azzurri"), # pag. 25
    ("on ima rjave lase in sive oči", "lui ha i capelli castani e gli occhi grigi"),
    ("on ima sive lase in rjave oči", "lui hai capelli grigi e gli occhi castani"),
    ("ona ima rjave lase in modre oči", "lei ha i capelli castani e gli occhi azzurri"),
    ("ona ima rjave lase in rjave oči", "lei ha i capelli castani e gli occhi castani"),
    ("on ima rdeče lase in modre oči", "ha i capelli rossi e gli occhi azzurri"),
    ("ona ima blond lase in modre oči", "lei ha i capelli biondi e gli occhi azzurri"),
    ("on ima rjave lase in modre oči", "ha i capelli castani e gli occhi azzurri"),
    ("ona ima blond lase in sive oči", ""),
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



start_tests(enota, int_seed=None)
