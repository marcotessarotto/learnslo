from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, Gender

# sloveno, traduzione, tipo, note, unità

enota = {}

enota[1] = (
    ("enota", "unità"),
    ("dober dan", "buongiorno", BookPage(7)),
    ("in", "e", WordType.CONJUNCTION, Level.EASY),
    ("črkujte", "sillabare", WordType.VERB, Level.DIFFICULT),
    ("dopolnite", "completate", WordType.VERB, Level.DIFFICULT),
    ("napišite", "scrivete", WordType.VERB, Level.DIFFICULT),
    ("odgovorite", "rispondete", WordType.VERB, Level.DIFFICULT),
    ("poslušajte", "ascoltate", WordType.VERB, Level.DIFFICULT),
    ("ponovite", "ripetete", WordType.VERB, Level.DIFFICULT),
    ("preberite", "leggete", WordType.VERB, Level.DIFFICULT),
    ("sestavite besede", "compilate le parole", WordType.VERB, Level.DIFFICULT),  # ???
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
    ("avto", "automobile"),
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
    ("nič", "0", WordType.NUMBER),
    ("ena", "1", WordType.NUMBER),
    ("dve", "2", WordType.NUMBER),
    ("tri", "3", WordType.NUMBER),
    ("štiri", "4", WordType.NUMBER),
    ("pet", "5", WordType.NUMBER),
    ("šest", "6", WordType.NUMBER),
    ("sedem", "7", WordType.NUMBER),
    ("osem", "8", WordType.NUMBER),
    ("devet", "9", WordType.NUMBER),
    ("deset", "10", WordType.NUMBER),
    ("enajst", "11", WordType.NUMBER),
    ("dvanajst", "12", WordType.NUMBER),
    ("trinajst", "13", WordType.NUMBER),
    ("štirinajst", "14", WordType.NUMBER),
    ("dvajset", "20", WordType.NUMBER),
    ("enaindvajset", "21", WordType.NUMBER),
    ("trideset", "30", WordType.NUMBER),
    ("sto", "100", WordType.NUMBER),
    ("tisoč", "1000", WordType.NUMBER),
    ("milijon", "1.000.000", WordType.NUMBER),
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
    ("ime", "nome"),  # IDENTITETA
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
    ("jaz sem", "io sono"),  # GLAGOL BITI
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
    ("Tomaž je zdravnik", "Tomaž è un medico"),
    ("Maja, Peter in Nina so iz Slovenije", "Maja, Peter e Nina sono della Slovenia"),
    ("Mi smo študenti", "noi siamo studenti universitari"),
    ("Gospa Turner, a ste vi iz Avstralije?", "Signora Turner, lei viene dall'Australia?"),
    ("Peter, a si ti ekonomist?", "Peter, sei laureato in economia?"),
    ("jaz nisem", "io non sono"),  # BITI (negativno)
    ("negativno", "negativo"),
    ("ti nisi", "tu non sei"),
    ("on, ona ni", "lui, lei non è"),
    ("mi nismo", "noi non siamo"),
    ("vi niste", "voi non siete"),
    ("oni, one niso", "loro/esse non sono"),
    ("psiholog", "psicologo"),
    ("jaz govorim", "io parlo/sto parlando"),  # GLAGOL: GOVORITI
    ("ti govoriš", "tu parli"),
    ("on, ona govori", "lui/lei parla"),
    ("mi govorimo", "noi parliamo"),
    ("vi govorite", "voi parlate"),
    ("oni, one govorijo", "loro/esse parlano"),
    ("a ti govoriš slovensko?", "tu parli sloveno?"),
    ("mobitel (m)", "telefono cellulare", Gender.MALE),
    ("starost", "età"),
)


def run_me():
    start_tests(enota, int_seed=None)


if __name__ == "__main__":
    run_me()
