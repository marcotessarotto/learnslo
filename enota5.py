from utilities import WordType, WordNote, PronNote, BookPage, Level, Item, process_dictionary, find_random_answers, \
    start_tests, Gender

enota = {}

# č š ž

enota[5] = (

    ("kakšno pico imate radi?", "che tipo di pizza vi piace?"),
    ("kakšno pico imaš rad/a?", "che tipo di pizza ti piace?"),
    ("kakšen sendvič imaš rad/a?", ""),
    ("potem", "dopo"),
    ("kam greš ?", "dove vai?"),
    ("od kod si?", "da dove arrivi/di dove sei?"),
    ("sem iz Trsta", "vengo da Trieste", Gender.MALE),
    ("sem iz Italije", "vengo dall'Italia", Gender.FEMALE),
    ("grem v Trst", "vado a Trieste", Gender.MALE),
    ("grem v italijo", "vado in Italia", Gender.FEMALE),
    ("sem iz Celja", "sono di Celje", Gender.NEUTRAL),
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


