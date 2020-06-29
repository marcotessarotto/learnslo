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