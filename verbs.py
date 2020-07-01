from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests

verbs = {}

verbs["pronomi"] = (
    ("jaz", "io"),
    ("ti", "tu"),
    ("on", "lui"),
    ("ona", "lei"),
    ("mi", "noi"),
    ("me", "noi (f)"),
    ("vi", "voi"),
    ("ve", "voi (f)"),
    ("oni", "essi"),
    ("one", "esse"),
    ("", ""),
)

verbs["extra"] = (
    ("sedanjik", "presente"),
    ("katere", "quale"),
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

verbs["biti"] = (
    ("jaz sem", "io sono", WordType.VERB), # pag. 69
    ("ti si", "tu sei", WordType.VERB),
    ("on/ona je", "lui/lei è", WordType.VERB),
    ("mi/me smo", "noi siamo", WordType.VERB),
    ("vi/ve ste", "voi siete", WordType.VERB),
    ("oni/one so", "essi/esse sono", WordType.VERB),
    ("jaz nisem", "io non sono", WordType.VERB),
    ("ti nisi", "tu non sei", WordType.VERB),
    ("on/ona ni", "lui/lei non è", WordType.VERB),
    ("mi/me nismo", "noi non siamo", WordType.VERB),
    ("vi/ve niste", "voi non siete", WordType.VERB),
    ("oni/one niso", "essi/esse non sono", WordType.VERB),
    ("", ""),
    ("sem", "sono"),
    ("si", "sei"),
    ("je", "è"),
    ("smo", "siamo"),
    ("ste", "siete"),
    ("so", "essi sono"),
    ("", ""),
    ("nisem", "non sono"),
    ("nisi", "non sei"),
    ("ni", "non è"),
    ("nismo", "non siamo"),
    ("niste", "non siete"),
    ("niso", "non sono"),
)

verbs["biti examples"] = (
    ("jaz sem zelo dobro", "io sto molto bene"),
    ("Anton je star 46 let", "Anton ha 46 anni"),
    ("on je star 46 let", "lui ha 46 anni"),
    ("ona je star 46 let", "lei ha 46 anni"),
    ("Nataša je zdravnica", "Nataša è medico"),
    ("Oni so stari 46 let", "essi hanno 46 anni"),
    ("Vi ste iz Argentine", "voi venite dall'Argentina"),
    ("Vi niste iz Maribora", "voi non siete di Maribor"),
    ("Eva ni zelo dobro", "Eva non sta molto bene"),
    ("Jaz nisem star/a 46 let", "io non ho 46 anni"),
    ("Ti nisi zdravnica", "tu non sei un medico"),
    ("Vi niste stari 46 let", "voi non avete 46 anni"),
    ("Mark ni iz Argentina", "Mark non viene dall'Argentina"),
    ("Ana, Boštjan in Matej so iz Maribora", "Ana, Boštjan e Matej sono di Maribor"),
    ("kako ti je ime?", "quale è il tuo nome?"),
    ("kako se pišeš?", "quale è il tuo cognome? ('come ti cognomi')"),
    ("koliko si star(a)?", "quanti anni hai?"),
    ("koliko ste stari?", "(formale) quanti anni ha?"),
    ("od kod si?", "di dove sei/da dove vieni?"),
    ("kaj si po poklicu?", "cosa sei di mestiere/che lavoro fai?"),
    ("katere jezike govoriš?", "quali lingue parli?"),
    ("katere jezike govorite?", "quali lingue parlate?"),
    ("a mi daš telefonsko številko, prosim?", "mi dai il numero di telefono, per favore?"),
    ("a mi daš naslov, prosim?", "mi dai l'indirizzo, per favore?"),
    ("a mi daš email, prosim?", "mi dai l'email, per favore?"),
    ("koliko stane pica?", "quanto cosa la pizza?"),
    ("kako se reče ...?", "come si dice ...?"),
    ("kaj je ...?", "cosa è ...?"),
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


verbs["brati"] = ( # leggere
    ("jaz berem", "io leggo", WordType.VERB),
    ("ti bereš", "tu leggi"),
    ("on/ona bere", "lui/lei legge"),
    ("mi/me beremo", "noi leggiamo"),
    ("vi/ve berete", "voi leggete"),
    ("oni/one bere", "essi/esse leggono"),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("", ""),
    ("ti bereš knjigo", "tu leggi un libro"),
    ("on bere knjigo", "lui legge un libro"),
    ("", ""),
    ("", ""),
    ("", ""),
)


verbs["delati"] = (
    ("jaz delam", "io lavoro/faccio"),
    ("ti delaš", "tu lavori"),
    ("on/ona dela", "lui/lei lavora"),
    ("mi/me delamo", "noi lavoriamo"),
    ("vi delate", "voi lavorate"),
    ("oni/one delajo", "essi/esse lavorano"),
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


verbs["imeti"] = (
    ("jaz imam", "io ho"),
    ("ti imaš", "tu hai"),
    ("on/ona ima", "lui/lei ha"),
    ("mi/me imamo", "noi abbiamo"),
    ("vi imate", "voi avete"),
    ("oni/one imajo", "essi/esse hanno"),
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


verbs["piti"] = (
    ("pijem", "io bevo", WordType.VERB),
    ("piješ", "tu bevi", WordType.VERB),
    ("pije", "egli/lei beve", WordType.VERB),
    ("pijemo", "noi beviamo", WordType.VERB),
    ("pijete", "voi bevete", WordType.VERB),
    ("pijejo", "essi bevono", WordType.VERB),
    ("ne pijem", "io non bevo", WordType.VERB),
    ("ne piješ", "tu non bevi", WordType.VERB),
    ("ne pije", "egli/lei non beve", WordType.VERB),
    ("ne pijemo", "noi non beviamo", WordType.VERB),
    ("ne pijete", "voi non bevete", WordType.VERB),
    ("ne pijejo", "essi/esse non bevono", WordType.VERB),
    ("", ""),

)



verbs[1] = (
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

verbs[1] = (
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


verbs["govoriti"] = (
    ("jaz govorim", "io parlo", WordType.VERB),
    ("ti govoris", "tu parli", WordType.VERB),
    ("on/ona govori", "lui/lei parla", WordType.VERB),
    ("mi govorimo", "noi parliamo", WordType.VERB),
    ("vi govorite", "voi parlate", WordType.VERB),
    ("oni/one govorijo", "essi/esse parlano", WordType.VERB),
    ("jaz ne govorim nemško", "io non parlo tedesco", WordType.VERB),
    ("", "", WordType.VERB),
    ("", "", WordType.VERB),
    ("", "", WordType.VERB),
    ("", "", WordType.VERB),
    ("", "", WordType.VERB),
    ("", "", WordType.VERB),
    ("ona govori angleško", "lei parla inglese"),
    ("Jaz govorim malo slovensko", "io parlo un po' di sloveno"),
    ("a ti govoriš špansko?", "parli spagnolo?"),
    ("Mi govorimo nemško", "Noi parliamo il tedesco"),
    ("Sara govori francosko", "Sara parla francese"),
    ("Oni govorijo arabsko", "Essi parlano arabo"),
    ("ti ne govoriš nemško", "tu non parli tedesco"),
    ("on ne govori nemško", "lui non parla tedesco"),
    ("mi ne govorimo nemško", "noi non parliamo tedesco"),
    ("vi ne govorite nemško", "voi non parlate tedesco"),
    ("oni ne govorijo nemško", "loro non parlano tedesco"),
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

verbs[1] = (
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


verbs[2] = (
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



# dict_slo, dict_ita = process_dictionary(verbs)


# print(f"len(dict_slo) = {len(dict_slo)}")

start_tests(verbs, int_seed=None)

