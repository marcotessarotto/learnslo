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


class AudioLink:
    def __init__(self, url):
        self.url = url


class Item:

    def __init__(self):
        self.slovensko = None  # is list of strings
        self.italiansko = None  # is a list of strings
        self.category = None
        self.bookpage = None
        self.wordtype = None
        self.level = None
        self.multiple_words = False

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
        item = Item()

        for count, val in enumerate(row):
            if count == 0:
                item.category = k
                item.slovensko = val.lower()
                item.slovensko_num_words = len(val.split())
                # multiple_words is true if slovensko has more than one word
                item.multiple_words = item.slovensko_num_words > 1
            elif count == 1:
                item.italiansko = val.lower()
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

    if max_questions == 0:
        max_questions = len(dict_lang)

    print(f"max_questions = {max_questions}")

    if int_seed != 0:
        random.seed(a=int_seed)
    else:
        random.seed()

    # make a copy of dict_slo.keys() because we will remove items from it
    dict_keys = list(dict_lang.keys())

    # Using list comprehension to concatenate all values into a single list
    # slo_dict_values = [item for sublist in dict_slo.values() for item in sublist]

    # print("***tests***")

    number_of_questions = 0
    correct_answers = 0
    current_pos = 0

    asked_questions = []
    wrong_answers = []

    r = range(len(dict_lang))
    # questions_to_ask = list(r)

    while dict_keys:
        current_pos += 1

        # Choose a random item from the list slo_dict_keys
        current_question = random.choice(dict_keys)

        # Remove the chosen question from the list
        dict_keys.remove(current_question)

        asked_questions.append(current_question)

        # choose random answer
        correct_answer = random.choice(dict_lang[current_question])

        possible_answers = find_random_answers(dict_lang,
                                               answers=[correct_answer],
                                               current_question=current_question,
                                               current_answer=correct_answer,
                                               slo2ita=slo2ita,
                                               number_of_answers=number_of_answers
                                               )

        random.shuffle(possible_answers)

        print()
        print(f"item #{current_pos} - {len(asked_questions)}/{max_questions}")

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
            if len(data) == 0:
                continue

            if data is None or data == "q":
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

    print("***finito!***")

    print(f"number_of_questions = {number_of_questions}")
    print(f"correct_answers = {correct_answers}")

    if wrong_answers:
        print()
        print("***errori***")
        for pos in wrong_answers:
            print(pos)

