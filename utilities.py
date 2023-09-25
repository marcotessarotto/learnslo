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


class PronNote: # pronunciation note
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
        self.slovensko = None # is list of strings
        self.italiansko = None # is a list of strings
        self.category = None
        self.bookpage = None
        self.wordtype = None
        self.level = None

    # make Item comparable
    def __eq__(self, other):
        return self.slovensko == other.slovensko and self.italiansko == other.italiansko

    def __str__(self):
        result = f"slovensko='{self.slovensko}' italiano='{self.italiansko}'"

        with contextlib.suppress(AttributeError):
            result += f" bookpage={self.bookpage}"
        with contextlib.suppress(AttributeError):
            result += f" wordtype={self.wordtype}"
        with contextlib.suppress(AttributeError):
            result += f" level={self.level}"
        with contextlib.suppress(AttributeError):
            result += f" gender={self.gender}"
        with contextlib.suppress(AttributeError):
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


def find_random_answers(dict_slo, current_question, current_answer,
                        # slo_dict_values, right_answer_pos: int,
                        result_len=5, ita2slo=False):
    """
    Costruisce un insieme di risposte sbagliate
    :param dict_slo:
    :param slo_dict_values:
    :param right_answer_pos:
    :param result_len:
    :param ita2slo: True se si sta facendo il test di traduzione dall'italiano allo sloveno
    :return:
    """

    result = []

    # if slo_dict_values is None:
    #     # raise exception
    #     raise ValueError("slo_dict_values is None")

    # right_answer = slo_dict_values[right_answer_pos]
    # right_answer is a list; find a random element in the list
    # right_answer = random.choice(right_answer)

    used_positions = []

    loop_counter = 0

    keys_to_select_from = list(dict_slo.keys())
    # remove current_question from the list
    keys_to_select_from.remove(current_question)

    while len(result) < result_len:

        loop_counter += 1
        if loop_counter > 1000:
            print("*** loop_counter > 1000 ***")
            break

        # choose a random key
        random_key = random.choice(keys_to_select_from)

        if random_key == current_question:
            raise Exception("random_key == current_question")

        # choose a random value in the list of values for the key
        random_answer = random.choice(dict_slo[random_key])

        if random_answer.multiple_words != current_answer.multiple_words:
            continue

        if random_answer in result:
            continue

        result.append(random_answer)
        # result.append(random_answer.slovensko if ita2slo else random_answer.italiansko)


        # if slo_dict_values[pos].multiple_words != right_answer.multiple_words:
        #     continue
        #
        #
        # pos = random.randrange(0, len(dict_slo))
        # if pos == right_answer_pos:
        #     continue
        # # multiple_words is true if slovensko has more than one word
        # if slo_dict_values[pos].multiple_words != right_answer.multiple_words:
        #     continue
        #
        # if pos in used_positions:
        #     continue
        #
        # result.append(slo_dict_values[pos].slovensko if ita2slo else slo_dict_values[pos].italiansko)
        #
        # used_positions.append(pos)

    return result


# def start_tests_ita2slo(my_dictionary, int_seed=0):
#     """
#     Effettua il test:
#     chiede all'utente di tradurre le parole dall'italiano allo sloveno scegliendo tra 5 possibili risposte (una sola è corretta)
#
#     :param my_dictionary:
#     :param int_seed:
#     :return:
#     """
#     # creare lista delle domande già fatte: ok
#     # creare lista delle domande sbagliate: ok
#
#     dict_slo, dict_ita = process_dictionary(my_dictionary)
#     # len(dict_slo) == len(dict_ita)
#
#     max_questions = len(dict_ita)
#
#     print(f"len(dict_slo) = {max_questions}")
#
#     if int_seed != 0:
#         random.seed(a=int_seed)
#
#     ita_dict_keys = list(dict_ita.keys())
#     ita_dict_values = list(dict_ita.values())
#
#     print("***tests***")
#
#     number_of_questions = 0
#     correct_answers = 0
#
#     asked_questions = []
#     wrong_answers = []
#
#     r = range(len(dict_ita))
#     questions_to_ask = list(r)
#
#     while 1:
#
#         if not questions_to_ask:
#             print("***finito!***")
#             break
#
#         rnd_value = random.randrange(0, len(questions_to_ask))
#
#         current_pos = questions_to_ask[rnd_value]
#         del questions_to_ask[rnd_value]
#
#         asked_questions.append(current_pos)
#
#         print()
#         print(f"item #{current_pos} - {len(asked_questions)}/{max_questions}")
#
#         test_key = ita_dict_keys[current_pos]
#         test_value = ita_dict_values[current_pos]
#
#         possible_answers = find_random_answers(dict_ita, ita_dict_values, current_pos, ita2slo=True)
#         possible_answers.append(ita_dict_values[current_pos].slovensko)
#
#         random.shuffle(possible_answers)
#
#         print(f"come tradurre: '{test_key}' ?")
#
#         for counter, i in enumerate(possible_answers):
#             print(f"{chr(ord('a') + counter)} : {i}")
#
#         data = input("risposta (q per uscire): ")
#         if data is None or data == "q":
#             break
#
#         number_of_questions += 1
#
#         try:
#             answer_pos = ord(data) - ord('a')
#         except TypeError:
#             print("?!?!?2")
#
#             answer_pos = 100
#         # print(answer_pos)
#
#         correct_answer = test_value.slovensko
#
#         try:
#             user_answer = possible_answers[answer_pos]
#         except IndexError:
#             print("?!?!?1")
#             user_answer = None
#
#         if correct_answer == user_answer:
#             print("OK")
#             correct_answers += 1
#             print(test_value)
#         else:
#             print("NOT OK")
#             print(f"*** risposta corretta: {correct_answer}")
#             wrong_answers.append(current_pos)
#
#         # print(tests)
#         # print(values[pos])
#
#         if answer_pos == -1:
#             break
#
#     print(f"number_of_questions = {number_of_questions}")
#     print(f"correct_answers = {correct_answers}")
#
#     if len(wrong_answers) > 0:
#         print()
#         print("***errori***")
#         for pos in wrong_answers:
#             question = ita_dict_values[pos]
#             print(question)


def start_tests(dict_slo, int_seed=0, slo2ita=True):
    """
    Effettua il test:
    chiede all'utente di tradurre le parole dallo sloveno all'italiano scegliendo tra 5 possibili risposte (una sola è corretta)

    :param my_dictionary: dizionario delle parole da tradurre
    :param int_seed:
    :return:
    """

    # dict_slo, dict_ita = process_dictionary(my_dictionary)
    # print(len(dict_slo))
    # print(len(dict_ita))

    max_questions = len(dict_slo)

    print(f"len(dict_slo) = {max_questions}")

    if int_seed != 0:
        random.seed(a=int_seed)

    # slo_dict_keys = list(dict_slo.keys())
    # make a copy of dict_slo.keys() because we will remove items from it
    slo_dict_keys = list(dict_slo.keys())

    #
    # slo_dict_values = list(dict_slo.values())
    # Using list comprehension to concatenate all values into a single list
    # slo_dict_values = [item for sublist in dict_slo.values() for item in sublist]

    print("***tests***")

    number_of_questions = 0
    correct_answers = 0
    current_pos = 0

    asked_questions = []
    wrong_answers = []

    r = range(len(dict_slo))
    questions_to_ask = list(r)

    while slo_dict_keys:

        current_pos += 1

        # if not slo_dict_keys:
        #     print("***finito!***")
        #     break

        # Choose a random item from the list slo_dict_keys
        current_question = random.choice(slo_dict_keys)

        # Remove the chosen key from the list
        slo_dict_keys.remove(current_question)

        asked_questions.append(current_question)

        # choose random answer
        correct_answer = random.choice(dict_slo[current_question])

        possible_answers = find_random_answers(dict_slo,
                                               current_question=current_question,
                                               current_answer=correct_answer,
                                              )
        # possible_answers.append(slo_dict_values[current_pos].italiansko)
        possible_answers.append(correct_answer)

        random.shuffle(possible_answers)

        #
        # rnd_value = random.randrange(0, len(questions_to_ask))
        #
        # current_pos = questions_to_ask[rnd_value]
        # del questions_to_ask[rnd_value]
        #
        # asked_questions.append(current_pos)

        print()
        print(f"item #{current_pos} - {len(asked_questions)}/{max_questions}")

        # test_key = slo_dict_keys[current_pos]
        # test_value = slo_dict_values[current_pos]
        #
        # possible_answers = find_random_answers(dict_slo, slo_dict_values, current_pos)
        # possible_answers.append(slo_dict_values[current_pos].italiansko)
        #
        # random.shuffle(possible_answers)

        print(f"cosa significa: '{current_question}' ?")

        for counter, i in enumerate(possible_answers):
            print(f"{chr(ord('a') + counter)} : {i.italiansko if slo2ita else i.slovensko}")

        data = input("risposta (q per uscire): ")
        if data is None or data == "q":
            break

        number_of_questions += 1

        try:
            answer_pos = ord(data) - ord('a')
        except TypeError:
            print("?!?!?2")

            answer_pos = 100
        # print(answer_pos)

        # correct_answer = current_answer.italiansko

        try:
            user_answer = possible_answers[answer_pos]
        except IndexError:
            print("?!?!?1")
            user_answer = None

        if correct_answer == user_answer:
            print("OK")
            correct_answers += 1
            print(correct_answer)
        else:
            print("NOT OK")
            print(f"*** risposta corretta: {correct_answer}")
            wrong_answers.append(correct_answer)

        # print(tests)
        # print(values[pos])

        if answer_pos == -1:
            break

    print("***finito!***")

    print(f"number_of_questions = {number_of_questions}")
    print(f"correct_answers = {correct_answers}")

    if wrong_answers:
        print()
        print("***errori***")
        for pos in wrong_answers:
            print(pos)
            # question = slo_dict_values[pos]
            # print(question)