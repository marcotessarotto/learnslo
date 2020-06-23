

enota_1_dict = {}

# https://docs.python.org/3.8/library/enum.html
from enum import Enum


class WordType(Enum):
    NOP = 0
    VERB = 1
    SENTENCE = 2
    ADVERB = 3


class WordNote:
    def __init__(self, text):
        self.text = text


class PronNote: # pronounciation note
    def __init__(self, text):
        self.text = text


class ImageUrl:
    def __init__(self, url):
        self.url = url


class BookPage:
    def __init__(self, page):
        self.page = page


class Level(Enum):
    NOP = 0
    EASY = 1
    MEDIUM = 2
    DIFFICULT = 3


class Gender(Enum):
    NEUTRAL = 0
    MALE = 1
    FEMALE = 2

# sloveno, traduzione, tipo, note, unità
test = ("dober dan", WordType.NOP, "", "", 1)



enota_1 = (
    ("enota", "unità"),
    ("dober dan", "buongiorno", BookPage(7)),
    ("preberite", "leggete", WordType.VERB, Level.DIFFICULT),
    ("dopolnite", "completate", WordType.VERB, Level.DIFFICULT),
    ("napišite", "scrivete", WordType.VERB, Level.DIFFICULT),
    ("poslušajte", "ascoltate", WordType.VERB, Level.DIFFICULT),
    ("ponovite", "ripetete", WordType.VERB, Level.DIFFICULT),
    ("črkujte", "sillabare", WordType.VERB, Level.DIFFICULT),
    ("sestavite besede", "compilate le parole", WordType.VERB, Level.DIFFICULT), # ???
    ("besedišče", "vocabolario"),
    ("beseda", "parola"),
    ("besede", "parole"),
    ("črko", "lettera"),
    ("eno črko lahko uporabite večkrat", "puoi usare una lettera più di una volta"),
    ("eno črko", "una lettera"),
    ("lahko", "può"),
    ("večkrat", "parecchie volte"),
    ("lahko uporabite", "puoi usare"),
    ("identiteta", "identità"),
    ("abeceda", "alfabeto"),
    ("številka", "numero"),
    ("številke", "numeri"),
    ("države", "stati"),
    ("poklici", "professioni"),
    ("jeziki", "le lingue"),
    ("slovnica", "grammatica"),
    ("biti", "essere", WordType.VERB, WordNote("infinito")),
    ("govoriti", "parlare", WordType.VERB, WordNote("infinito")),
    ("jaz sem Marco", "io sono Marco", WordType.SENTENCE),
    ("me veseli!", "piacere", WordType.SENTENCE),
    ("živjo", "ciao"),
    ("vstative", "inserite", WordType.VERB),
    ("adijo", "ciao"),
    ("dober večer", "buonasera"),
    ("lahko noč", "buona notte"),
    ("se vidimo", "ci vediamo"),
    ("dobro jutro", "buon mattino"),
    ("nasvidenje", "arrivederci"),
    ("lep dan", "buona giornata"),
    ("pozdravljeni", "piacere/io vi saluto", WordNote("dober dan in pozdravljeni")),
    ("kako si?", "come stai?", WordNote("letterale: come sei?")),
    ("dobro", "bene", WordType.ADVERB),
    ("odlično", "eccellente", WordNote("kako si? odlično!")),
    ("slabo", "male", WordNote("kako si? slabo")),
    ("tako tako", "così così"),
    ("v redu", "ok"),
    ("zelo dobro", "molto bene", WordType.ADVERB),
    ("zelo", "molto"),
    ("auto", "automobile"),
    ("april", "aprile"),
    ("avgust", "agosto"),
    ("banka", "banca"),
    ("balkon", "balcone"),
    ("cigareta", "sigaretta"),
    ("center", "centro"),
    ("C-vitamin", "vitamina C"),
    ("čokolada", "cioccolato"),
    ("čips", "patatine"),
    ("čaj", "tè"),
    ("december", "dicembre"),
    ("direktor", "direttore"),
    ("dinozaver", "dinosauro"),
    ("Evropa", "Europa"),
    ("evro", "euro"),
    ("evrov", "euro (plurale)"),
    ("elektrika", "elettricità"),
    # film, festival
    ("februar", "febbraio"),
    ("galerija", "galleria d'arte"),
    ("garaža", "garage"),
    ("hvala", "grazie"),
    ("informacija", "informazione"),
    ("inštitut", "istituto"),
    ("januar", "gennaio"),
    ("junij", "giugno"),
    ("julij", "luglio"),
    ("ja", "si"),
    ("kava", "caffè"),
    ("kitara", "chitarra"),
    ("koncert", "concerto"),
    ("limona", "limone"),
    ("limonada", "limonata"),
    ("marec", "marzo", PronNote("c finale come z")),
    ("maj", "maggio"),
    ("muzej", "museo"),
    ("november", "novembre"),
    ("noč", "notte"),
    ("ne", "no"),
    ("oktober", "ottobre"),
    ("opera", "musica lirica"),
    ("pica", "pizza"),
    ("policija", "polizia"),
    ("park", "parco/giardino"),
    ("restavracija", "ristorante"),
    ("recepcija", "ricezione"),
    ("riž", "riso"),
    ("sendvič", "sandwitch"),
    ("solata", "insalata"),
    ("september", "settembre"),
    ("študent", "studente"),
    ("šola", "scuola"),
    ("špageti", "spaghetti"),
    ("telefon", "telefono"),
    ("tehnologija", "tecnologia"),
    ("tenis", "tennis"),
    ("univerza", "università"),
    ("ura", "ora"),
    ("učitelj", "maestro"),
    ("voda", "acqua"),
    ("veterinar", "veterinario"),
    ("zdravnik", "medico"),
    ("žirafa", "giraffa"),
    ("kaj je ...?", "cosa è ...?"),
    ("kako se reče ...?", "come si dice ...?"),
    ("oprostite", "mi scusi"),
    ("oprostite, ne razumem", "mi scusi, non capisco"),
    ("ne razumem", "non capisco"),
    ("ponovite, prosim", "ripeti, per favore"),
    ("prosim", "per favore"),
    ("nič", "0"),
    ("ena", "1"),
    ("dve", "2"),
    ("tri", "3"),
    ("štiri", "4"),
    ("pet", "5"),
    ("šest", "6"),
    ("sedem", "7"),
    ("osem", "8"),
    ("devet", "9"),
    ("deset", "10"),
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
