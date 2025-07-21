from __future__ import annotations
import contextlib
from enum import Enum
from typing import Optional, List, Dict, Tuple, Union, Any
from dataclasses import dataclass, field
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
    INTERROGATIVE_SENTENCE = 9
    OTHER = 10


@dataclass
class WordNote:
    text: str


@dataclass
class PronNote:  # pronunciation note
    text: str


@dataclass
class ImageUrl:
    url: str


@dataclass
class BookPage:
    page: int



class Level(Enum):
    NOP = 0
    EASY = 1
    MEDIUM = 2
    DIFFICULT = 3


class Gender(Enum):
    NEUTRAL = 0
    MALE = 1
    FEMALE = 2


@dataclass
class WebLink:
    url: str

    def __str__(self) -> str:
        return f"url={self.url}"


@dataclass
class AudioLink:
    url: str

    def __str__(self) -> str:
        return f"url={self.url}"


@dataclass
class Item:
    """
    Represents a language learning item with Slovenian and Italian translations.

    This class stores vocabulary items, phrases, or sentences along with their
    translations and associated metadata like word type, difficulty level,
    and reference information.
    """
    slovensko: Optional[str] = None
    italiansko: Optional[str] = None
    category: Optional[str] = None
    bookpage: Optional[int] = None
    wordtype: Optional[WordType] = None
    level: Optional[Level] = None
    gender: Optional[Gender] = None
    weblink: Optional[WebLink] = None
    slo_multiple_words: bool = field(init=False, default=False)
    ita_multiple_words: bool = field(init=False, default=False)
    is_question: bool = field(init=False, default=False)
    slovensko_num_words: int = field(init=False, default=0)
    italiansko_num_words: int = field(init=False, default=0)

    def __post_init__(self):
        if self.slovensko:
            self.slovensko = self.slovensko.lower()
            self.slovensko_num_words = len(self.slovensko.split())
            self.slo_multiple_words = self.slovensko_num_words > 1
            self.is_question = self.slovensko.endswith("?")

        if self.italiansko:
            self.italiansko = self.italiansko.lower()
            self.italiansko_num_words = len(self.italiansko.split())
            self.ita_multiple_words = self.italiansko_num_words > 1

    @classmethod
    def from_row(cls, row: Tuple, category: str) -> 'Item':
        """
        Create an Item object from a row tuple

        Args:
            row: Tuple containing item data (slovensko, italiansko, metadata...)
            category: Category classification for the item

        Returns:
            New Item instance
        """
        # Start with basic data
        kwargs = {'category': category}

        for count, val in enumerate(row):
            if count == 0:
                kwargs['slovensko'] = val
            elif count == 1:
                kwargs['italiansko'] = val
            elif isinstance(val, BookPage):
                kwargs['bookpage'] = val.page
            elif isinstance(val, WordType):
                kwargs['wordtype'] = val
            elif isinstance(val, Level):
                kwargs['level'] = val
            elif isinstance(val, Gender):
                kwargs['gender'] = val
            elif isinstance(val, WebLink):
                kwargs['weblink'] = val

        return cls(**kwargs)

    @classmethod
    def from_strings(cls, slovensko: str, italiansko: str, category: str = None) -> 'Item':
        """Create from simple string pair"""
        return cls(slovensko=slovensko, italiansko=italiansko, category=category)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Item':
        """Create from dictionary data"""
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def __str__(self) -> str:
        result = f"slovensko='{self.slovensko}' italiano='{self.italiansko}'"

        optional_attrs = ['bookpage', 'wordtype', 'level', 'gender', 'weblink']
        for attr in optional_attrs:
            value = getattr(self, attr, None)
            if value is not None:
                result += f" {attr}={value}"

        return result


def process_dictionary(
        my_dict: Dict[str, List[Tuple]],
        dict_slo: Optional[Dict[str, List[Item]]] = None,
        dict_ita: Optional[Dict[str, List[Item]]] = None
) -> Tuple[Dict[str, List[Item]], Dict[str, List[Item]]]:
    """
    Process the dictionary and return two dictionaries (Slovenian and Italian)

    Args:
        my_dict: Input dictionary to process
        dict_slo: Optional existing Slovenian dictionary
        dict_ita: Optional existing Italian dictionary

    Returns:
        Tuple of (slovenian_dict, italian_dict)
    """
    if dict_slo is None:
        dict_slo = {}
    if dict_ita is None:
        dict_ita = {}

    def append_to_dict(d: Dict[str, List[Item]], key: str, item: Item) -> None:
        """Helper function to append items to dictionary lists"""
        if key not in d:
            d[key] = [item]
        else:
            d[key].append(item)

    def process_row_variants(row: Tuple, category: str) -> List[Item]:
        """Process a row that might contain multiple variants"""
        items = []

        # Handle cases where both slovensko and italiansko are collections
        if (isinstance(row[0], (tuple, list)) and
                isinstance(row[1], (tuple, list))):
            raise ValueError("Both slovensko and italiansko cannot be collections")

        # Handle slovensko as collection
        if isinstance(row[0], (tuple, list)):
            for slo_variant in row[0]:
                if slo_variant:  # Skip empty strings
                    new_row = list(row)
                    new_row[0] = slo_variant
                    items.append(Item.from_row(tuple(new_row), category))

        # Handle italiansko as collection
        elif isinstance(row[1], (tuple, list)):
            for ita_variant in row[1]:
                if ita_variant:  # Skip empty strings
                    new_row = list(row)
                    new_row[1] = ita_variant
                    items.append(Item.from_row(tuple(new_row), category))

        # Handle simple case
        else:
            if row[0]:  # Skip empty slovensko
                items.append(Item.from_row(row, category))

        return items

    # Main processing loop
    for category, rows in my_dict.items():
        print(f"Processing category: {category}")

        for row in rows:
            try:
                items = process_row_variants(row, category)

                for item in items:
                    append_to_dict(dict_slo, item.slovensko, item)
                    append_to_dict(dict_ita, item.italiansko, item)

            except Exception as e:
                print(f"Error processing row {row} in category {category}: {e}")
                continue

    return dict_slo, dict_ita


def find_random_answers(
        dict_lang: Dict[str, List[Item]],
        current_question: str,
        current_answer: Item,
        number_of_answers: int = 5,
        slo2ita: bool = True,
        max_attempts: int = 1000
) -> List[Item]:
    """
    Build a set of wrong answers plus the correct one

    Args:
        dict_lang: Language dictionary
        current_question: The current question text
        current_answer: The correct answer
        number_of_answers: Total number of answers to return
        slo2ita: True if translating from Slovenian to Italian
        max_attempts: Maximum attempts to find suitable answers

    Returns:
        List of Item objects including the correct answer
    """
    answers = [current_answer]
    available_keys = [key for key in dict_lang.keys() if key != current_question]

    attempts = 0
    while len(answers) < number_of_answers and attempts < max_attempts:
        attempts += 1

        try:
            random_key = random.choice(available_keys)
            random_answer = random.choice(dict_lang[random_key])

            # Skip if word count doesn't match
            if random_answer.slo_multiple_words != current_answer.slo_multiple_words:
                continue

            # Skip if already in answers
            if random_answer in answers:
                continue

            # Check for duplicate translations
            if slo2ita:
                if any(item.italiansko == random_answer.italiansko for item in answers):
                    continue
            else:
                if any(item.slovensko == random_answer.slovensko for item in answers):
                    continue

            answers.append(random_answer)

        except (IndexError, ValueError):
            continue

    if len(answers) < number_of_answers:
        print(f"Warning: Could only find {len(answers)} answers out of {number_of_answers} requested")

    return answers


class LanguageQuiz:
    """Modern quiz interface with better organization and error handling"""

    def __init__(self, dict_lang: Dict[str, List[Item]], seed: int = 0):
        self.dict_lang = dict_lang
        self.seed = seed
        self.reset_stats()

        if seed != 0:
            random.seed(seed)
        else:
            random.seed()

    def reset_stats(self) -> None:
        """Reset quiz statistics"""
        self.wrong_answers = []
        self.number_of_questions = 0
        self.correct_answers = 0

    def prepare_questions(
            self,
            slo2ita: bool = True,
            max_questions: int = 0,
            number_of_answers: int = 5
    ) -> List[Tuple[str, Item, List[Item]]]:
        """Prepare list of questions and answers"""

        if max_questions == 0:
            max_questions = len(self.dict_lang)

        dict_keys = list(self.dict_lang.keys())
        questions_and_answers = []

        while dict_keys and len(questions_and_answers) < max_questions:
            current_question = random.choice(dict_keys)
            dict_keys.remove(current_question)

            correct_answer = random.choice(self.dict_lang[current_question])

            possible_answers = find_random_answers(
                self.dict_lang,
                current_question,
                correct_answer,
                number_of_answers,
                slo2ita
            )

            random.shuffle(possible_answers)
            questions_and_answers.append((current_question, correct_answer, possible_answers))

        return questions_and_answers

    def run_quiz(
            self,
            slo2ita: bool = True,
            max_questions: int = 0,
            number_of_answers: int = 5
    ) -> Dict[str, Union[int, float]]:
        """Run the interactive quiz"""

        questions_and_answers = self.prepare_questions(slo2ita, max_questions, number_of_answers)
        self.reset_stats()

        for current_pos, (current_question, correct_answer, possible_answers) in enumerate(questions_and_answers, 1):
            print(f"\nQuestion #{current_pos} / {len(questions_and_answers)}")

            if slo2ita:
                print(f"What does '{current_question}' mean?")
            else:
                print(f"How do you translate '{current_question}'?")

            # Display options
            for counter, answer in enumerate(possible_answers):
                display_text = answer.italiansko if slo2ita else answer.slovensko
                print(f"{chr(ord('a') + counter)}: {display_text}")

            # Get user input
            user_answer = self._get_user_input(possible_answers)
            if user_answer is None:  # User chose to quit
                break

            self.number_of_questions += 1

            # Check answer
            if correct_answer == user_answer:
                print("✓ Correct!")
                self.correct_answers += 1
                print(f"Answer: {correct_answer}")
            else:
                print("✗ Incorrect")
                print(f"Correct answer: {correct_answer}")
                self.wrong_answers.append(correct_answer)

        return self._display_results()

    def _get_user_input(self, possible_answers: List[Item]) -> Optional[Item]:
        """Get and validate user input"""
        while True:
            try:
                data = input("Answer (q to quit): ").strip().lower()

                if not data:
                    continue

                if data == "q":
                    return None

                if len(data) == 1 and 'a' <= data <= chr(ord('a') + len(possible_answers) - 1):
                    answer_pos = ord(data) - ord('a')
                    return possible_answers[answer_pos]
                else:
                    print("Invalid input. Please enter a valid option.")

            except (EOFError, KeyboardInterrupt):
                return None

    def _display_results(self) -> Dict[str, Union[int, float]]:
        """Display quiz results"""
        print("\n" + "=" * 50)
        print("QUIZ COMPLETED!")
        print("=" * 50)

        if self.number_of_questions > 0:
            ratio = (self.correct_answers / self.number_of_questions) * 100
            print(f"Questions answered: {self.number_of_questions}")
            print(f"Correct answers: {self.correct_answers}")
            print(f"Score: {ratio:.1f}%")

            if self.wrong_answers:
                print(f"\nIncorrect answers ({len(self.wrong_answers)}):")
                for answer in self.wrong_answers:
                    print(f"  • {answer}")
        else:
            ratio = 0
            print("No questions were answered.")

        return {
            "total_questions": self.number_of_questions,
            "correct_answers": self.correct_answers,
            "score_percentage": ratio
        }


# Backward compatibility function
def start_tests(dict_lang: Dict[str, List[Item]], int_seed: int = 0, slo2ita: bool = True,
                max_questions: int = 0, number_of_answers: int = 5) -> Dict[str, Union[int, float]]:
    """
    Legacy function for backward compatibility
    """
    quiz = LanguageQuiz(dict_lang, int_seed)
    return quiz.run_quiz(slo2ita, max_questions, number_of_answers)
