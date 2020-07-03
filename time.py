from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests

time_dict = {}

# č š ž


# disp. 2 pag. 27
time_dict["adverbs"] = (
    ("dan", "(il) giorno"),
    ("podnevi", "di giorno"),
    ("jutro", "(il) mattino"),
    ("večer", "(la) sera"),
    ("leto", "(l') anno"),
    ("danes", "oggi/oggigiorno"),
    ("jutri", "domani"),
    ("včeraj", "ieri"),
    ("zjutraj", "di mattina"),
    ("zvečer", "di sera"),
    ("letos", "quest’anno"),
    ("zdaj/sedaj", "ora"),
    ("prej", "prima"),
    ("najprej", "prima (di tutto)"),
    ("potem", "dopo"),
    ("poldan", "mezzogiorno"),
    ("opoldan", "a mezzogiorno"),
    ("zima", "inverno"),
    ("pozimi", "d'inverno"),
    ("poletje", "estate"),
    ("poleti", "in/d'estate"),
    ("noč", "notte"),
    ("ponoči", "di notte"),
    ("pomlad", "primavera"),
    ("spomladi", "in primavera"),
    ("jesen", "autunno"),
    ("jeseni", "in/d' autunno"),
    ("kolikokrat", "Quante volte?"),
    ("Enkrat", "Una volta"),
    ("Dvakrat", "Due volte"),
    ("Trikrat", "Tre volte"),
    ("Štirikrat", "Quattro volte"),
    ("Desetkrat", "Dieci volte"),
    ("Stokrat", "Cento volte"),
    ("Tisočkrat", "Mille volte"),
    ("Tukaj", "Qua"), # avverbi di luogo
    ("Tam", "Là"),
    ("tja", "Là"),
    ("Spodaj", "Sotto"),
    ("Zgoraj", "Sopra"),
    ("Noter", "Dentro"),
    ("Zunaj", "Fuori"),
    ("Na desni/desno", "A destra"),
    ("Na levi/levo", "A sinistra"),
    ("Spredaj", "Davanti"),
    ("Zadaj", "Dietro"),
    ("Daleč", "Lontano"),




    ("Včeraj", "Ieri"), # avverbi di tempo
    ("Danes", "Oggi"),
    ("Jutri", "Domani"),
    ("Takoj", "Subito"),
    ("Prej, preden", "Prima"),
    ("Najprej", "Prima (di tutto)"),
    ("Potem", "Dopo"),
    ("Zgodaj", "Presto"),
    ("Zvečer", "Di sera"),
    ("Zjutraj", "Di mattina"),
    ("Popoldne", "Di pomeriggio"),
    ("Pridi sem!", "vieni qua"),
    ("Pojdi tja!", "Vai là"),
    ("Tja grem!", "Vado là"),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
)



time_dict["week"] = (

    ("Ponedeljek – v ponedeljek, ob ponedeljkih", "Lunedì"),
    ("Torek – v torek, ob torkih", "Martedì"),
    ("Sreda – v sredo, ob sredah", "Mercoledì"),
    ("Četrtek – v četrtek, ob četrtkih", "Giovedì"),
    ("Petek – v petek, ob petkih", "Venerdì"),
    ("Sobota – v soboto, ob sobotah", "Sabato"),
    ("Nedelja – v nedeljo, ob nedeljah", "Domenica"),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),

)


time_dict["year"] = (

    ("Januar – v januarju, januarja", "Gennaio"),
    ("Februar – v februarju, februarja", "Febbraio"),
    ("Marec – v marcu, marca", "Marzo"),
    ("April – v aprilu, aprila", "Aprile"),
    ("Maj – v maju, maja", "Maggio"),
    ("Junij – v juniju, junija", "Giugno"),
    ("Julij – v juliju, julija", "Luglio"),
    ("Avgust -  v avgustu, avgusta", "Agosto"),
    ("September – v septembru, septembra", "Settembre"),
    ("Oktober – v oktobru, oktobra", "Ottobre"),
    ("November – v novembru, novembra", "Novembre"),
    ("December – v decembru, decembra", "Dicembre"),
    ("", ""),
    ("", ""),
    ("", ""),

)

time_dict["extra"] = (
    ("V ponedeljek imam izpit", "Lunedì ho l'esame"),
    ("Ob ponedeljkih imam lekcije", "Di lunedì ho le lezioni"),
    ("Vsak ponedeljek imam lekcije", "Ogni lunedì ho le lezioni"),
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

start_tests(time_dict, int_seed=None)



