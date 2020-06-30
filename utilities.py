# https://docs.python.org/3.8/library/enum.html
from enum import Enum

import random


class WordType(Enum):
    NOP = 0
    VERB = 1
    SENTENCE = 2
    ADVERB = 3
    PRONOUN = 4


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


class Item:

    def __str__(self):
        result = f"slovensko='{self.slovensko}' italiansko='{self.italiansko}'"

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

        try:
            result += f" gender={self.gender}"
        except:
            pass

        return result


def process_dictionary(my_dict, dict_slo={}, dict_ita={}):
    # dict_slo = {}
    # dict_ita = {}

    for k, v in my_dict.items():
        print(f"process_dictionary key={k}")

        for row in v:

            if row[0] == "":
                continue

            i = Item()

            # print(row)

            for count, item in enumerate(row):
                if count == 0:
                    i.category = k
                    i.slovensko = item
                    i.slovensko_num_words = len(item.split())
                    i.multiple_words = i.slovensko_num_words > 1
                    continue
                elif count == 1:
                    i.italiansko = item
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
                    elif type(item) is Gender:
                        i.gender = item

                    # print(count, item)

            # print(i)
            # print("***\n")

            dict_slo[i.slovensko] = i
            dict_ita[i.italiansko] = i

    return dict_slo, dict_ita


def find_random_answers(dict_slo, slo_dict_values, right_answer_pos: int, result_len=3):

    result = []

    #slo_dict_keys = dict_slo.keys()

    if slo_dict_values is None:
        slo_dict_values = list(dict_slo.values())

    right_answer = slo_dict_values[right_answer_pos]

    used_positions = []

    while len(result) < result_len:

        pos = random.randrange(0, len(dict_slo) - 1)
        if pos == right_answer_pos:
            continue
        if slo_dict_values[pos].multiple_words != right_answer.multiple_words:
            continue

        if pos in used_positions:
            continue

        result.append(slo_dict_values[pos].italiansko)

        used_positions.append(pos)

    return result


def start_tests(my_dictionary, int_seed=0):
    # creare lista delle domande già fatte: ok
    # creare lista delle domande sbagliate: ok

    dict_slo, dict_ita = process_dictionary(my_dictionary)

    max_questions = len(dict_slo)

    print(f"len(dict_slo) = {max_questions}")

    if int_seed is not None:
        random.seed(a=0)

    slo_dict_keys = list(dict_slo.keys())
    slo_dict_values = list(dict_slo.values())

    print("***tests***")

    number_of_questions = 0
    correct_answers = 0

    asked_questions = []
    wrong_answers = []

    while 1:

        if len(asked_questions) == max_questions:
            print("***finito!***")
            break

        current_pos = random.randrange(0, len(dict_slo) )

        if current_pos in asked_questions:
            continue
        else:
            asked_questions.append(current_pos)

        print()
        print(f"item {current_pos} - {len(asked_questions)}/{max_questions}")

        test_key = slo_dict_keys[current_pos]
        test_value = slo_dict_values[current_pos]

        possible_answers = find_random_answers(dict_slo, slo_dict_values, current_pos)
        possible_answers.append(slo_dict_values[current_pos].italiansko)

        random.shuffle(possible_answers)

        print(f"cosa vuol dire: '{test_key}' ?")

        # print("scegli tra le risposte:")

        # print()
        counter = 0
        for i in possible_answers:
            print(f"{chr(ord('a') + counter)} : {i.lower()}")
            counter += 1

        data = input("risposta (q per uscire):")
        if data is None or data == "q":
            break

        number_of_questions += 1

        try:
            answer_pos = ord(data) - ord('a')
        except TypeError:
            print("?!?!?2")

            answer_pos = 100
        # print(answer_pos)

        correct_answer = test_value.italiansko

        try:
            user_answer = possible_answers[answer_pos]
        except IndexError:
            print("?!?!?1")
            user_answer = None

        if correct_answer == user_answer:
            print("OK")
            correct_answers += 1
            print(test_value)
        else:
            print("NOT OK")
            print(f"*** risposta corretta: {correct_answer}")
            wrong_answers.append(current_pos)

        # print(tests)
        # print(values[pos])

        if answer_pos == -1:
            break

    print(f"number_of_questions = {number_of_questions}")
    print(f"correct_answers = {correct_answers}")

    if len(wrong_answers) > 0:
        print()
        print("***errori***")
        for pos in wrong_answers:
            question = slo_dict_values[pos]
            print(question)