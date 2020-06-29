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


def process_dictionary(my_dict):
    dict_slo = {}
    dict_ita = {}

    for k, v in my_dict.items():
        print(f"my_dict {k}")

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

    return dict_slo, dict_ita

