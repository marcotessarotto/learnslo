
# https://docs.python.org/3.8/library/enum.html
import random
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
#test = ("dober dan", WordType.NOP, "", "", 1)


enota = {}

enota[1] = (
    ("enota", "unità"),
    ("dober dan", "buongiorno", BookPage(7)),

    ("črkujte", "sillabare", WordType.VERB, Level.DIFFICULT),
    ("dopolnite", "completate", WordType.VERB, Level.DIFFICULT),
    ("napišite", "scrivete", WordType.VERB, Level.DIFFICULT),
    ("odgovorite", "rispondete", WordType.VERB, Level.DIFFICULT),
    ("poslušajte", "ascoltate", WordType.VERB, Level.DIFFICULT),
    ("ponovite", "ripetete", WordType.VERB, Level.DIFFICULT),
    ("preberite", "leggete", WordType.VERB, Level.DIFFICULT),
    ("sestavite besede", "compilate le parole", WordType.VERB, Level.DIFFICULT), # ???
    ("vprašajte in odgovorite", "chiedete e rispondete", WordType.VERB, Level.DIFFICULT),
    ("vstavite", "inserite", WordType.VERB, Level.DIFFICULT),
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
    ("kako si?", "come stai? (come sei?)", WordNote("letterale: come sei?")),
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
    ("enajst", "11"),
    ("dvanajst", "12"),
    ("trinajst", "13"),
    ("štirinajst", "14"),
    ("dvajset", "20"),
    ("enaindvajset", "21"),
    ("trideset", "30"),
    ("sto", "100"),
    ("tisoč", "1000"),
    ("milijon", "1.000.000"),
    ("a mi daš telefonsko številko, prosim?", "mi dai il numero di telefono, per favore?"),
    ("moja telefonska številka je ...", "il mio numero di telefono è ..."),
    ("koliko", "quanto"),
    ("koliko si star/a?", "quanti anni hai (quanto sei vecchio)?"),
    ("star/a sem oseminštirideset let", "io ho 48 anni"),
    ("leta", "anni"),
    ("koliko stane pica?", "quanto cosa la pizza?"),
    ("pica stane pet evrov", "la pizza costa cinque euro"),
    ("to je poceni", "questo cosa poco"),
    ("to je predrago", "questo è troppo caro"),
    ("poceni", "a buon mercato"),
    ("naslov", "indirizzo"),
    ("a mi daš naslov, prosim?", "mi dai l'indirizzo, per favore?"),
    ("a mi daš email, prosim?", "mi dai l'email, per favore?"),
    ("pika", "."),
    ("afna", "@"),
    ("minus", "-"),
    ("_ črtica spodaj", "linetta sotto"),
    ("od kod si?", "di dove sei/da dove vieni?"),
    ("kdo je to?", "chi è questo?"),
    ("kdo si?", "chi sei tu?"),
    ("sem iz Slovenije, iz Maribora", "(io) vengo (sono) dalla Slovenia, da Maribor"),
    ("Mark je iz Rusije", "Mark viene dalla Russia"),
    ("kaj si po poklicu?", "cosa sei di mestiere/che lavoro fai?"),
    ("po poklicu sem ...", "di mestiere sono ..."),
    ("delam kot ...", "lavoro come ..."),
    ("studiram ...", "studio ..."),
    ("poklic", "professione"),
    ("od kod", "da dove"),
    ("kaj", "che cosa"),
    ("ti si iz Avstrije", "tu vieni dall'Austria"),
    ("vi ste iz Italije", "voi venite dall'Italia"),
    ("drugi dialog", "secondo dialogo"),
    ("inženir", "ingegnere"),
    ("natakar", "cameriere"),
    ("študent", "studente universitario"),
    ("učitelj", "maestro"),
    ("zdravnik", "medico"),
    ("kot", "come"),
    ("inženirka", "ingegnera"),
    ("natakarica", "cameriera"),
    ("študentka", "studentessa universitaria"),
    ("učiteljica", "maestra"),
    ("zdravnica", "medica"),
    ("Peter je inženir", "Peter è un ingegnere"),
    ("katere jezike govoriš?", "quali lingue parli?"),
    ("katere", "quale/i"),
    ("jezika", "linguaggio/lingue"),
    ("govorim angleško", "io parlo inglese"),
    ("govorim angleško in malo slovensko", "parlo inglese ed un po' di sloveno"),
    ("malo", "poco"),
    ("a govoriš nemško?", "parli tedesco?"),
    ("ja, govorim", "si, lo parlo"),
    ("ne, ne govorim", "no, non lo parlo"),
    ("sem ekonomist", "sono laureato in economia"),
    ("ampak", "ma"),
    ("ampak zdaj ne delam", "ma ora non lavoro"),
    ("zdaj", "ora"),
    ("ime", "nome"), # IDENTITETA
    ("priimek", "cognome"),
    ("jezik", "linguaggio"),
    ("država", "stato"),
    ("kako ti je ime?", "quale è il tuo nome?"),
    ("kako se pišeš?", "quale è il tuo cognome? ('come ti cognomi')"),
    ("kolega", "il collega"),
    ("kolegica", "la collega"),
    ("neformalno", "non formale/informale"),
    ("formalno", "formale"),
    ("kako vam je ime?", "(formale) quale è il suo nome?"),
    ("kako se pišete?", "(formale) quale è il suo cognome?"),
    ("od kod ste?", "(formale) da dove viene/di dove è?"),
    ("kaj ste po poklicu?", "(formale) cosa fa di mestiere?"),
    ("koliko ste stari?", "(formale) quanti anni ha?"),
    ("katere jezike govorite", "(formale) quali lingue parlate?"),
    ("glagol", "verbo"),
    ("biti", "verbo essere"),
    ("jaz sem", "io sono"), # GLAGOL BITI
    ("ti si", "tu sei"),
    ("on, ona je", "egli/lei è"),
    ("mi smo", "noi siamo"),
    ("vi ste", "voi siete"),
    ("oni, one so", "loro/esse sono"),
    ("tudi", "anche"),
    ("gospa", "signora"),
    ("gospod", "signore"),
    ("Eva je študentka", "Eva è una studentessa"),
    ("Mark je iz Kanade", "Mark viene dal Canada"),
    ("Jaz sem študent", "Io sono uno studente universitario"),
    ("Sara, Mija in Tjaša so študentke", "Sara, Mija e Tjaša sono studentesse universitarie"),
    ("Tomaž Novak je zdravnik", "Tomaž Novak è un medico"),
    ("Maja, Peter in Nina so iz Slovenije", "Maja, Peter e Nina sono della Slovenia"),
    ("Mi smo študenti", "noi siamo studenti universitari"),
    ("Ana: Gospa Turner, a ste vi iz Avstralije?", "Signora Turner, lei viene dall'Australia?"),
    ("Tom: Peter, a si ti ekonomist?", "Peter, sei laureato in economia?"),
    ("jaz nisem", "io non sono"), # BITI (negativno)
    ("negativno", "negativo"),
    ("ti nisi", "tu non sei"),
    ("on, ona ni", "lui, lei non è"),
    ("mi nismo", "noi non siamo"),
    ("vi niste", "voi non siete"),
    ("oni, one niso", "loro/esse non sono"),
    ("psiholog", "psicologo"),
    ("jaz govorim", "io parlo/sto parlando"), # GLAGOL: GOVORITI
    ("ti govoriš", "tu parli"),
    ("on, ona govori", "lui/lei parla"),
    ("mi govorimo", "noi parliamo"),
    ("vi govorite", "voi parlate"),
    ("oni, one govorijo", "loro/esse parlano"),
    ("a ti govoriš slovensko?", "tu parli sloveno?"),
    ("mobitel", "telefono cellulare"),
    ("starost", "età"),
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


class Item:

    def __str__(self):
        result = f"slovensko='{self.slovensko}' italiankso='{self.italiankso}'"

        try:
            result += f" bookpage={self.bookpage}"
        except:
            pass

        try:
            result += f" wordtype={self.wordtype}"
        except:
            pass

        try:
            result += f" level={self.level}"
        except:
            pass

        return result


# words_dict = {}

dict_slo = {}
dict_ita = {}

for k, v in enota.items():
    print(f"enota {k}")

    for row in v:

        if row[0] == "":
            continue

        i = Item()

        # print(row)

        for count, item in enumerate(row):
            if count == 0:
                i.slovensko = item
                continue
            elif count == 1:
                i.italiankso = item
                continue
            else:
                if type(item) is BookPage:
                    # print("BookPage!")
                    i.bookpage = item.page
                elif type(item) is WordType:
                    # print("WordType!")
                    i.wordtype = item
                elif type(item) is Level:
                    # print("Level!")
                    i.level = item

                # print(count, item)

        # print(i)
        # print("***\n")

        dict_slo[i.slovensko] = i
        dict_ita[i.italiankso] = i

print(len(dict_slo))


def find_random_answers(right_answer_pos: int, result_len = 3):
    result = []

    keys = dict_slo.keys()
    values = list(dict_slo.values())

    while len(result) < result_len:
        pos = random.randrange(0, len(dict_slo) - 1)
        if pos == right_answer_pos:
            continue
        result.append(values[pos].italiankso)

    return result


random.seed(a=0)


keys = list(dict_slo.keys())
values = list(dict_slo.values())





print("***tests***")

while 1:
    pos = random.randrange(0, len(dict_slo) - 1)
    print(pos)

    test_key = keys[pos]
    test_value = values[pos]

    possible_answers = find_random_answers(pos)
    possible_answers.append(values[pos].italiankso)
    random.shuffle(possible_answers)

    print()
    print(f"cosa vuol dire: '{test_key}'")

    print("possibili risposte:")

    print()
    counter = 0
    for i in possible_answers:
        print(f"{counter} : {i}")
        counter += 1

    data = input("risposta (-1 to exit):")
    answer_pos = int(data)
    # print(answer_pos)

    correct_answer = test_value.italiankso
    user_answer = possible_answers[answer_pos]

    if correct_answer == user_answer:
        print("OK")
    else:
        print("NOT OK")

    # print(tests)
    # print(values[pos])

    if answer_pos == -1:
        break