from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests

time_dict = {}

# č š ž


time_dict[1] = (
    ("dan", "(il) giorno"),
    ("jutro", "(il) mattino"),
    ("večer", "(la) sera"),
    ("leto", "(l') anno"),
    ("danes", "oggi/oggigiorno"),
    ("jutri", "domani"),
    ("včeraj", "ieri"),
    ("zjutraj", "di mattina"),
    ("zvečer", "di sera"),
    ("letos", "qest’anno"),
    ("zdaj/sedaj", "ora"),
    ("prej", "prima"),
    ("najprej", "prima (di tutto)"),
    ("potem", "dopo"),
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

start_tests(time_dict, int_seed=None)



