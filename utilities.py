import contextlib
from enum import Enum

import random


class WordType(Enum):
    NOP = 0
    VERB = 1
    SENTENCE = 2
    ADVERB = 3
    PRONOUN = 4
    CONJUNCTION = 5
    NUMBER = 6
    NOUN = 7
    ADJECTIVE = 8


class WordNote:
    def __init__(self, text):
        self.text = text


class PronNote:  # pronunciation note
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


class WebLink:
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f"url={self.url}"


class AudioLink:
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f"url={self.url}"


class Item:
    """
    Represents a language learning item with Slovenian and Italian translations.

    This class stores vocabulary items, phrases, or sentences along with their
    translations and associated metadata like word type, difficulty level,
    and reference information.

    Attributes:
        slovensko (list of str or None): Slovenian word(s) or phrase(s)
        italiansko (list of str or None): Italian word(s) or phrase(s)
        category (str or None): Category classification for the item
        bookpage (BookPage or None): Reference to book page where item appears
        wordtype (WordType or None): Type of word (noun, verb, adjective, etc.)
        level (Level or None): Difficulty level (easy, medium, difficult)
        multiple_words (bool): True if Slovenian contains multiple words
        ita_multiple_words (bool): True if Italian contains multiple words
        is_question (bool): True if the item represents a question
    """

    def __init__(self):
        self.slovensko = None  # list of strings
        self.italiansko = None  # list of strings
        self.category = None
        self.bookpage = None
        self.wordtype = None
        self.level = None
        self.multiple_words = False
        self.ita_multiple_words = False
        self.is_question = False

    # make Item comparable
    def __eq__(self, other):
        return self.slovensko == other.slovensko and self.italiansko == other.italiansko

    def __str__(self):
        result = f"slovensko='{self.slovensko}' italiano='{self.italiansko}'"

        with contextlib.suppress(AttributeError):
            if self.bookpage is not None:
                result += f" bookpage={self.bookpage}"
        with contextlib.suppress(AttributeError):
            if self.wordtype is not None:
                result += f" wordtype={self.wordtype}"
        with contextlib.suppress(AttributeError):
            if self.level is not None:
                result += f" level={self.level}"
        with contextlib.suppress(AttributeError):
            if self.gender is not None:
                result += f" gender={self.gender}"
        with contextlib.suppress(AttributeError):
            if self.weblink is not None:
                result += f" weblink={self.weblink}"
        return result


def process_dictionary(my_dict, dict_slo=None, dict_ita=None):
    """
    Processa il dizionario e restituisce due dizionari (sloveno e italiano)
    :param my_dict:
    :param dict_slo:
    :param dict_ita:
    :return:
    """
    if dict_slo is None:
        dict_slo = {}
    if dict_ita is None:
        dict_ita = {}

    def append_to_dict(d, key, item):
        if key not in d:
            d[key] = [item]
        else:
            d[key].append(item)

    def process_row(row):
        """
        Processa una riga del dizionario
        esempi:

        ("slovar", "dizionario"),
        ("", ""),
        ("neurje", ("temporale", "tempesta")),

        :param row:
        :return:
        """
        item = Item()

        for count, val in enumerate(row):
            if count == 0:
                item.category = k
                item.slovensko = val.lower()
                item.slovensko_num_words = len(val.split())
                # multiple_words is true if slovensko has more than one word
                item.multiple_words = item.slovensko_num_words > 1
                item.is_question = item.slovensko.endswith("?")
            elif count == 1:
                item.italiansko = val.lower()
                item.italiansko_num_words = len(val.split())
                item.ita_multiple_words = item.italiansko_num_words > 1
            elif type(val) is BookPage:
                # print("BookPage!")
                item.bookpage = val.page
            elif type(val) is WordType:
                # print("WordType!")
                item.wordtype = val
            elif type(val) is Level:
                # print("Level!")
                item.level = val
            elif type(val) is Gender:
                item.gender = val
            elif type(val) is WebLink:
                item.weblink = val

        return item

    for k, v in my_dict.items():
        print(f"process_dictionary key={k}")

        for row in v:
            if (type(row[0]) is tuple or type(row[0]) is list) and (type(row[1]) is tuple or type(row[1]) is list):
                print("ERROR: both slovensko and italiano are lists")
                exit(1)

            if type(row[0]) is tuple or type(row[0]) is list:
                for i in row[0]:
                    if i == "":
                        continue
                    new_row = list(row)
                    new_row[0] = i
                    new_item = process_row(new_row)

                    append_to_dict(dict_slo, new_item.slovensko, new_item)
                    append_to_dict(dict_ita, new_item.italiansko, new_item)
                continue

            if row[0] == "":
                continue

            # if row[1] is a tuple or a list, then expand to multiple rows
            if type(row[1]) is tuple or type(row[1]) is list:
                for i in row[1]:
                    if i == "":
                        continue
                    new_row = list(row)
                    new_row[1] = i
                    new_item = process_row(new_row)

                    append_to_dict(dict_slo, new_item.slovensko, new_item)
                    append_to_dict(dict_ita, new_item.italiansko, new_item)
                continue

            new_item = process_row(row)

            append_to_dict(dict_slo, new_item.slovensko, new_item)
            append_to_dict(dict_ita, new_item.italiansko, new_item)

    return dict_slo, dict_ita


def find_random_answers(dict_lang,
                        answers,
                        current_question: str,
                        current_answer: Item,
                        questions_list=None,
                        number_of_answers=5,
                        slo2ita=True):
    """
    Costruisce un insieme di risposte sbagliate
    :param dict_lang:
    :param answers: lista di risposte (include quella corretta)
    :param current_question:
    :param current_answer:
    :param number_of_answers: numero di risposte da restituire
    :param ita2slo: True se si sta facendo il test di traduzione dall'italiano allo sloveno
    :return:
    """

    result = answers

    loop_counter = 0

    keys_to_select_from = list(dict_lang.keys())

    # remove current_question from the list
    keys_to_select_from.remove(current_question)

    # if current_answer.is_question:
    #     # find at least 2 other questions

    while len(result) < number_of_answers:

        loop_counter += 1
        if loop_counter > 1000:
            print("*** loop_counter > 1000 ***")
            break

        # choose a random key
        random_key = random.choice(keys_to_select_from)

        if random_key == current_question:
            raise Exception("random_key == current_question")

        # choose a random value in the list of values for the key
        random_answer = random.choice(dict_lang[random_key])

        if random_answer.multiple_words != current_answer.multiple_words:
            continue

        if random_answer in result:
            continue

        if not slo2ita:
            # if the answer is already in the list, skip it
            skip = any(i.slovensko == random_answer.slovensko for i in result)
        else:
            # if the answer is already in the list, skip it
            skip = any(i.italiansko == random_answer.italiansko for i in result)

        if skip:
            continue

        result.append(random_answer)

    return result


def prepare_list_of_questions_and_answers(dict_lang, slo2ita=True, max_questions=0, number_of_answers=5):

    print(f"max_questions = {max_questions}")

    # make a copy of dict_slo.keys() because we will remove items from it
    dict_keys = list(dict_lang.keys())    

    questions_list = [item for item_list in dict_lang.values() for item in item_list if item.is_question]

    print(f"len(questions_list) = {len(questions_list)}")

    list_of_questions_and_answers = []

    while dict_keys and len(list_of_questions_and_answers) < max_questions:
        # Choose a random item from the list slo_dict_keys
        current_question = random.choice(dict_keys)

        # Remove the chosen question from the list
        dict_keys.remove(current_question)

        # asked_questions.append(current_question)

        # choose random answer
        correct_answer = random.choice(dict_lang[current_question])

        possible_answers = find_random_answers(dict_lang,
                                               answers=[correct_answer],
                                               current_question=current_question,
                                               current_answer=correct_answer,
                                               questions_list=questions_list,
                                               slo2ita=slo2ita,
                                               number_of_answers=number_of_answers
                                               )

        random.shuffle(possible_answers)

        list_of_questions_and_answers.append((current_question, correct_answer, possible_answers))

    return list_of_questions_and_answers


def start_tests(dict_lang, int_seed=0, slo2ita=True, max_questions=0, number_of_answers=5):
    """
    Effettua il test:
    chiede all'utente di tradurre le parole dallo sloveno all'italiano scegliendo tra 5 possibili risposte (una sola è corretta)

    :param dict_lang: dizionario da utilizzare nel test
    :param slo2ita: True se si sta facendo il test di traduzione dallo sloveno all'italiano
    :param int_seed:
    :param max_questions: numero massimo di domande da fare
    :param number_of_answers: numero di risposte da mostrare per ogni domanda
    :return:
    """

    if int_seed != 0:
        random.seed(a=int_seed)
    else:
        random.seed()

    if max_questions == 0:
        max_questions = len(dict_lang)

    list_of_questions_and_answers = prepare_list_of_questions_and_answers(dict_lang,
                                                                           slo2ita=slo2ita,
                                                                           max_questions=max_questions,
                                                                           number_of_answers=number_of_answers)

    wrong_answers = []
    number_of_questions = 0
    correct_answers = 0
    current_pos = 0

    for current_question, correct_answer, possible_answers in list_of_questions_and_answers:
        current_pos += 1

        print()
        print(f"domanda #{current_pos} / {max_questions}")

        if slo2ita:
            print(f"cosa significa: '{current_question}' ?")
        else:
            print(f"come si traduce: '{current_question}' ?")

        for counter, i in enumerate(possible_answers):
            print(f"{chr(ord('a') + counter)} : {i.italiansko if slo2ita else i.slovensko}")

        exit_while = False
        user_answer = None

        while 1:
            data = input("risposta (q per uscire): ")
            if data is None or len(data) == 0:
                continue

            if data == "q":
                exit_while = True
                break

            number_of_questions += 1

            try:
                answer_pos = ord(data) - ord('a')
            except TypeError:
                continue

            try:
                user_answer = possible_answers[answer_pos]
            except IndexError:
                continue

            break

        if exit_while:
            break

        if correct_answer == user_answer:
            print("OK")
            correct_answers += 1
            print(correct_answer)
        else:
            print("NOT OK")
            print(f"*** risposta corretta: {correct_answer}")
            wrong_answers.append(correct_answer)

    print()
    print("***finito!***")

    print(f"number_of_questions = {number_of_questions}")
    print(f"correct_answers = {correct_answers}")
    print(f"ratio = {correct_answers / number_of_questions * 100:.2f}%")

    if wrong_answers:
        print()
        print("***errori***")
        for pos in wrong_answers:
            print(pos)
