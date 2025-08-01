"""
Slovenian-Italian Language Learning Utilities

This module provides a comprehensive framework for creating and managing
Slovenian-Italian vocabulary learning applications with quiz functionality.

The module supports:
- Vocabulary item management with metadata (difficulty, word types, etc.)
- Dictionary processing from structured data
- Interactive quiz generation with multiple choice answers
- Support for complex language features (gender, pronunciation, etc.)

Author: Marco T.
Version: 2.0
Python: 3.7+ (requires dataclasses)
"""

from __future__ import annotations
from enum import Enum
from typing import Optional, List, Dict, Tuple, Union
from dataclasses import dataclass, field
import random


# =============================================================================
# ENUMERATIONS AND METADATA CLASSES
# =============================================================================

class WordType(Enum):
    """
    Enumeration of grammatical word types for vocabulary classification.

    Used to categorize vocabulary items by their grammatical function,
    which helps in organizing learning materials and creating appropriate
    quiz questions.
    """
    NOP = 0  # No specific type / not classified
    VERB = 1  # Action words (govoriti, biti, delati)
    SENTENCE = 2  # Complete phrases or sentences
    ADVERB = 3  # Words modifying verbs/adjectives (zelo, dobro)
    PRONOUN = 4  # Pronouns (jaz, ti, kdo, kaj)
    CONJUNCTION = 5  # Connecting words (in, ampak, ker)
    NUMBER = 6  # Numerical values (ena, dve, tri)
    NOUN = 7  # Objects, people, concepts (hiša, človek) [sostantivo]
    ADJECTIVE = 8  # Descriptive words (lep, velik, dober)


class SentenceCategory(Enum):
    NOP = 0,
    INTERROGATIVE = 1,
    SENTENCE = 2,


class Level(Enum):
    """
    Difficulty levels for vocabulary items.

    Used to categorize vocabulary by learning difficulty,
    allowing for progressive learning paths and appropriate
    quiz difficulty scaling.
    """
    NOP = 0  # No difficulty assigned
    EASY = 1  # Basic, high-frequency words
    MEDIUM = 2  # Intermediate vocabulary
    DIFFICULT = 3  # Advanced or specialized terms


class Gender(Enum):
    """
    Grammatical gender classification for nouns.

    Important for Slovenian grammar, where noun gender affects
    adjective agreement and case declension patterns.
    """
    NEUTRAL = 0  # Neutral gender (srednji spol)
    MALE = 1  # Masculine gender (moški spol)
    FEMALE = 2  # Feminine gender (ženski spol)


# =============================================================================
# METADATA AND REFERENCE CLASSES
# =============================================================================

@dataclass
class QuestionGroup:
    """
    group together (loosely) Items so that when building questions, these can be choosen together
    """
    id: str


@dataclass
class WordNote:
    """
    Additional textual notes about a vocabulary item.

    Used for grammar notes, usage examples, or contextual information
    that helps learners understand proper word usage.

    Attributes:
        text: The explanatory note text
    """
    text: str


@dataclass
class PronNote:
    """
    Pronunciation guidance for vocabulary items.

    Provides phonetic transcriptions or pronunciation hints,
    particularly useful for words with non-obvious pronunciation.

    Attributes:
        text: Pronunciation guide or phonetic transcription
    """
    text: str


@dataclass
class ImageUrl:
    """
    Reference to visual learning materials.

    Links vocabulary items to images for visual learning support,
    particularly effective for concrete nouns and visual concepts.

    Attributes:
        url: Web URL or local path to the image resource
    """
    url: str


@dataclass
class BookPage:
    """
    Reference to textbook or learning material pages.

    Associates vocabulary items with specific pages in learning
    materials, enabling cross-referencing with physical resources.

    Attributes:
        page: Page number in the reference material
    """
    page: int


@dataclass
class WebLink:
    """
    External web resources for additional learning.

    Provides links to online dictionaries, grammar references,
    or other educational resources for deeper learning.

    Attributes:
        url: Web URL to the external resource
    """
    url: str

    def __str__(self) -> str:
        return f"url={self.url}"


@dataclass
class AudioLink:
    """
    Audio pronunciation resources.

    Links to audio files or online pronunciation tools,
    crucial for correct pronunciation learning.

    Attributes:
        url: Web URL or local path to audio resource
    """
    url: str

    def __str__(self) -> str:
        return f"url={self.url}"


# =============================================================================
# CORE VOCABULARY ITEM CLASS
# =============================================================================

@dataclass
class Item:
    """
    Core vocabulary learning item with Slovenian and Italian translations.

    This class represents a single vocabulary entry in the language learning
    system, containing the source and target language texts along with
    comprehensive metadata for learning optimization.

    The class automatically processes text to extract linguistic features
    like word count, question detection, and case normalization.

    Attributes:
        slovensko: Slovenian text (source language)
        italiansko: Italian text (target language)  
        category: Thematic category (e.g., "family", "food")
        bookpage: Reference page in learning materials
        wordtype: Grammatical classification
        level: Difficulty level for progressive learning
        gender: Grammatical gender (important for Slovenian)
        weblink: External reference link
        slo_multiple_words: Auto-computed flag for multi-word expressions
        ita_multiple_words: Auto-computed flag for Italian multi-word expressions
        is_question: Auto-detected flag for question sentences
        slovensko_num_words: Auto-computed word count for Slovenian
        italiansko_num_words: Auto-computed word count for Italian

    Example:
        >>> item = Item(slovensko="kako si", italiansko="come stai", 
        ...             wordtype=WordType.SENTENCE, level=Level.EASY)
        >>> print(item.is_question)  # False
        >>> print(item.slo_multiple_words)  # True (2 words)
    """
    # Class variables for tracking and organizing items
    _next_id = 1
    _all_instances = []
    _all_question_groups = {}


    # Unique identifier (not passed to constructor, assigned automatically)
    id: int = field(init=False)

    # Core translation data
    slovensko: Optional[str] = None
    italiansko: Optional[str] = None

    # Organizational metadata  
    category: Optional[str] = None
    bookpage: Optional[int] = None

    # Linguistic metadata
    wordtype: Optional[WordType] = None
    sentence_category: Optional[SentenceCategory] = None
    level: Optional[Level] = None
    gender: Optional[Gender] = None

    # Reference links
    weblink: Optional[WebLink] = None

    # Auto-computed linguistic features (not set via constructor)
    slo_multiple_words: bool = field(init=False, default=False)
    ita_multiple_words: bool = field(init=False, default=False)
    is_question: bool = field(init=False, default=False)
    slovensko_num_words: int = field(init=False, default=0)
    italiansko_num_words: int = field(init=False, default=0)
    ends_with_ite: bool = field(init=False, default=False)

    question_groups: Optional[list] = field(init=True, default_factory=list)

    def __post_init__(self):
        """
        Post-initialization processing to compute linguistic features.

        This method is automatically called after object creation to:
        - Normalize text case (convert to lowercase)
        - Count words in both languages
        - Detect multi-word expressions
        - Identify questions (sentences ending with '?')

        The computed features are used for quiz logic, difficulty assessment,
        and appropriate answer matching.
        """
        # Assign the next available ID and increment the counter
        self.id = Item._next_id
        Item._next_id += 1

        # Process Slovenian text
        if self.slovensko:
            self.slovensko = self.slovensko.lower()
            self.slovensko_num_words = len(self.slovensko.split())
            self.slo_multiple_words = self.slovensko_num_words > 1
            self.is_question = self.slovensko.endswith("?")
            self.ends_with_ite = True if self.slovensko.endswith("ite") else False

        # Process Italian text  
        if self.italiansko:
            self.italiansko = self.italiansko.lower()
            self.italiansko_num_words = len(self.italiansko.split())
            self.ita_multiple_words = self.italiansko_num_words > 1

        if self.is_question and self.sentence_category is None:
            self.sentence_category = SentenceCategory.INTERROGATIVE

        # Register this instance for class-level tracking
        Item._all_instances.append(self)

        # print(self.question_groups)
        for gp in self.question_groups:
            if gp.id not in Item._all_question_groups:
                Item._all_question_groups[gp.id] = []
            Item._all_question_groups[gp.id].append(self)

    @classmethod
    def get_all_questions(cls) -> List['Item']:
        """
        Return all Item instances where is_question is True.

        This method searches through all created Item instances and returns
        only those that have been identified as questions (sentences ending with '?').

        Returns:
            List of Item objects where is_question is True

        Example:
            >>> item1 = Item(slovensko="kako si?", italiansko="come stai?")
            >>> item2 = Item(slovensko="zdravo", italiansko="ciao")
            >>> questions = Item.get_all_questions()
            >>> print(len(questions))  # 1
            >>> print(questions[0].slovensko)  # kako si?
        """
        return [item for item in cls._all_instances if item.is_question]

    @classmethod
    def from_row(cls, row: Tuple, category: str) -> 'Item':
        """
        Factory method to create Item from structured tuple data.

        This method processes the tuple format used in the vocabulary
        data files (enota1.py, enota2.py, etc.) and creates properly
        initialized Item objects.

        Args:
            row: Tuple containing (slovensko, italiansko, metadata...)
                 where metadata can include WordType, Level, Gender, 
                 BookPage, WebLink, AudioLink objects
            category: Thematic category string for the vocabulary item

        Returns:
            New Item instance with all metadata properly assigned

        Example:
            >>> row = ("zdravo", "ciao", WordType.SENTENCE, Level.EASY)
            >>> item = Item.from_row(row, "greetings")
            >>> print(item.wordtype)  # WordType.SENTENCE
        """
        # Initialize with category
        kwargs = {'category': category, 'question_groups': []}

        # Process each element in the tuple
        for count, val in enumerate(row):
            if count == 0:
                # First element is always Slovenian text
                kwargs['slovensko'] = val
            elif count == 1:
                # Second element is always Italian text  
                kwargs['italiansko'] = val
            elif isinstance(val, BookPage):
                # Extract page number from BookPage object
                kwargs['bookpage'] = val.page
            elif isinstance(val, WordType):
                # Direct assignment of grammatical type
                kwargs['wordtype'] = val
            elif isinstance(val, SentenceCategory):
                kwargs['sentence_category'] = val
            elif isinstance(val, Level):
                # Direct assignment of difficulty level
                kwargs['level'] = val
            elif isinstance(val, Gender):
                # Direct assignment of grammatical gender
                kwargs['gender'] = val
            elif isinstance(val, WebLink):
                # Direct assignment of web reference
                kwargs['weblink'] = val
            elif isinstance(val, QuestionGroup):
                kwargs['question_groups'].append(val)
            # Note: AudioLink, WordNote, PronNote could be added here
            # as additional metadata fields if needed

        return cls(**kwargs)

    def __str__(self) -> str:
        """
        Human-readable string representation of the vocabulary item.

        Displays the core translation pair plus any assigned metadata,
        useful for debugging and logging purposes.

        Returns:
            Formatted string showing slovensko/italiansko plus metadata
        """
        result = f"slovensko='{self.slovensko}' italiano='{self.italiansko}'"

        # Add optional metadata if present
        optional_attrs = ['bookpage', 'wordtype', 'sentence_category', 'level', 'gender', 'weblink']
        for attr in optional_attrs:
            value = getattr(self, attr, None)
            if value is not None:
                result += f" {attr}={value}"

        return result


# =============================================================================
# DICTIONARY PROCESSING FUNCTIONS  
# =============================================================================

def process_dictionary(
        my_dict: Dict[str, List[Tuple]],
        dict_slo: Optional[Dict[str, List[Item]]] = None,
        dict_ita: Optional[Dict[str, List[Item]]] = None
) -> Tuple[Dict[str, List[Item]], Dict[str, List[Item]]]:
    """
    Process structured vocabulary data into searchable dictionaries.

    This function transforms the raw vocabulary data format used in lesson
    files (enota1.py, etc.) into two indexed dictionaries for efficient
    lookup during quiz generation and vocabulary searches.

    The function handles complex data structures including:
    - Multiple translation variants (tuples/lists)
    - Empty entries (skipped automatically)
    - Metadata objects (WordType, Level, etc.)
    - Error recovery for malformed data

    Args:
        my_dict: Source dictionary with format:
                 {category: [(slovensko, italiansko, metadata...), ...]}
        dict_slo: Optional existing Slovenian->Item dictionary to extend
        dict_ita: Optional existing Italian->Item dictionary to extend

    Returns:
        Tuple of (slovenian_dict, italian_dict) where:
        - slovenian_dict: {slovenian_text: [Item, ...]}
        - italian_dict: {italian_text: [Item, ...]}

    Raises:
        ValueError: If both slovensko and italiansko are collections

    Example:
        >>> vocab_data = {
        ...     "greetings": [
        ...         ("zdravo", "ciao", Level.EASY),
        ...         ("dober dan", ("buongiorno", "buona giornata"))
        ...     ]
        ... }
        >>> slo_dict, ita_dict = process_dictionary(vocab_data)
        >>> print(len(slo_dict["zdravo"]))  # 1
        >>> print(len(ita_dict["buongiorno"]))  # 1
    """
    # Initialize dictionaries if not provided
    if dict_slo is None:
        dict_slo = {}
    if dict_ita is None:
        dict_ita = {}

    def append_to_dict(d: Dict[str, List[Item]], key: str, item: Item) -> None:
        """
        Helper function to safely append items to dictionary lists.

        Creates new list if key doesn't exist, otherwise appends to existing list.
        This allows multiple Items to share the same translation text.

        Args:
            d: Target dictionary to modify
            key: Dictionary key (translation text)
            item: Item object to append
        """
        if key not in d:
            d[key] = [item]
        else:
            d[key].append(item)

    def process_row_variants(row: Tuple, category: str) -> List[Item]:
        """
        Process a single data row that may contain multiple translation variants.

        Handles the complex data structures found in vocabulary files:
        - Simple pairs: ("word", "translation")  
        - Slovenian variants: (("word1", "word2"), "translation")
        - Italian variants: ("word", ("trans1", "trans2"))
        - Mixed with metadata: ("word", "trans", WordType.VERB, Level.EASY)

        Args:
            row: Tuple containing vocabulary data
            category: Thematic category for the items

        Returns:
            List of Item objects (multiple if variants present)

        Raises:
            ValueError: If both positions contain collections
        """
        items = []

        # Validate data structure - both can't be collections
        if (isinstance(row[0], (tuple, list)) and
                isinstance(row[1], (tuple, list))):
            raise ValueError(
                f"Both slovensko and italiano cannot be collections in row: {row}"
            )

        # Handle Slovenian variants: multiple Slovenian words -> one Italian
        if isinstance(row[0], (tuple, list)):
            for slo_variant in row[0]:
                if slo_variant:  # Skip empty strings
                    # Create new row with single Slovenian variant
                    new_row = list(row)
                    new_row[0] = slo_variant
                    items.append(Item.from_row(tuple(new_row), category))

        # Handle Italian variants: one Slovenian word -> multiple Italian
        elif isinstance(row[1], (tuple, list)):
            for ita_variant in row[1]:
                if ita_variant:  # Skip empty strings
                    # Create new row with single Italian variant
                    new_row = list(row)
                    new_row[1] = ita_variant
                    items.append(Item.from_row(tuple(new_row), category))

        # Handle simple case: direct slovensko -> italiansko mapping
        else:
            if row[0]:  # Skip entries with empty Slovenian text
                items.append(Item.from_row(row, category))

        return items

    # Main processing loop - iterate through all categories
    for category, rows in my_dict.items():
        print(f"Processing category: {category}")

        # Process each vocabulary entry in the category
        for row in rows:
            try:
                # Generate Item objects (may be multiple due to variants)
                items = process_row_variants(row, category)

                # Index each item in both dictionaries
                for item in items:
                    append_to_dict(dict_slo, item.slovensko, item)
                    append_to_dict(dict_ita, item.italiansko, item)

            except Exception as e:
                # Log errors but continue processing other entries
                print(f"Error processing row {row} in category {category}: {e}")
                continue

    return dict_slo, dict_ita


# =============================================================================
# QUIZ GENERATION FUNCTIONS
# =============================================================================

def find_random_answers(
        dict_lang: Dict[str, List[Item]],
        current_question: str,
        current_answer: Item,
        number_of_answers: int = 5,
        slo2ita: bool = True,
        max_attempts: int = 1000
) -> List[Item]:
    """
    Generate a list of plausible wrong answers plus the correct answer.

    This function creates multiple-choice quiz options by selecting
    incorrect answers that are similar in structure to the correct answer,
    making the quiz challenging but fair.

    The selection algorithm prioritizes:
    - Similar word count (single words vs phrases)
    - Different translations (no duplicates)
    - Variety in incorrect options

    Args:
        dict_lang: Dictionary to select answers from
        current_question: The question text (to exclude from wrong answers)
        current_answer: The correct Item object
        number_of_answers: Total answers to return (including correct)
        slo2ita: True for Slovenian->Italian quiz, False for Italian->Slovenian
        max_attempts: Maximum tries to find suitable wrong answers

    Returns:
        List of Item objects with correct answer and wrong answers

    """
    # Start with correct answer
    answers = [current_answer]

    # Get all possible questions except current one
    available_keys = [key for key in dict_lang.keys() if key != current_question]

    attempts = 0
    while len(answers) < number_of_answers and attempts < max_attempts:
        attempts += 1

        random_answer = None

        try:

            if current_answer.question_groups and attempts*2 < max_attempts:
                # try to choose other (wrong) answers from the same question group(s) to which the correct answer belongs

                qg = random.choice(current_answer.question_groups)

                # for qg in current_answer.question_groups:
                question_group = qg.id

                random_answer = random.choice(Item._all_question_groups[question_group])
                if random_answer.id == current_answer.id:
                    continue

            else:

                # Select random question and random answer for that question
                random_key = random.choice(available_keys)
                random_answer = random.choice(dict_lang[random_key])

                # find other questions
                if current_answer.is_question:
                    if not random_answer.is_question and attempts < max_attempts/5:
                        continue

                if current_answer.ends_with_ite:
                    if not random_answer.ends_with_ite and attempts < max_attempts/3:
                        continue

                # find other non questions
                if not current_answer.is_question:
                    if random_answer.is_question and attempts < max_attempts/5:
                        continue

                # Ensure structural similarity (word count matching)
                # This makes single-word questions have single-word wrong answers
                if not current_answer.is_question:
                    if not slo2ita:
                        if random_answer.slo_multiple_words != current_answer.slo_multiple_words and attempts < max_attempts/5:
                            continue
                    else:
                        if random_answer.ita_multiple_words != current_answer.ita_multiple_words and attempts < max_attempts/5:
                            continue

            # Skip if this answer is already selected
            if random_answer in answers:
                continue

            # Check for duplicate translations based on quiz direction
            if slo2ita:
                # For Slo->Ita quiz, check Italian translations
                if any(item.italiansko == random_answer.italiansko for item in answers):
                    continue
            else:
                # For Ita->Slo quiz, check Slovenian translations  
                if any(item.slovensko == random_answer.slovensko for item in answers):
                    continue

            # Add this answer to our collection
            answers.append(random_answer)

        except (IndexError, ValueError):
            # Handle edge cases where random selection fails
            continue

    # Warn if we couldn't find enough answers
    if len(answers) < number_of_answers:
        print(f"Warning: Could only find {len(answers)} answers out of "
              f"{number_of_answers} requested for question '{current_question}'")

    return answers


# =============================================================================
# QUIZ INTERFACE CLASS
# =============================================================================

class LanguageQuiz:
    """
    Modern interactive quiz system for language learning.

    This class provides a complete quiz interface with:
    - Question preparation and randomization
    - Interactive user input with validation
    - Score tracking and detailed results
    - Flexible quiz parameters (direction, length, options)

    The quiz supports both translation directions (Slovenian->Italian and
    Italian->Slovenian) and provides detailed feedback on performance.

    Attributes:
        dict_lang: Vocabulary dictionary for quiz generation
        seed: Random seed for reproducible quiz sequences
        wrong_answers: List of incorrectly answered items
        number_of_questions: Count of questions attempted
        correct_answers: Count of correct responses
    """

    def __init__(self, dict_lang: Dict[str, List[Item]], seed: int = 0):
        """
        Initialize quiz system with vocabulary dictionary.

        Args:
            dict_lang: Dictionary mapping text to Item lists
            seed: Random seed (0 for random, >0 for reproducible sequences)
        """
        self.dict_lang = dict_lang
        self.seed = seed
        self.reset_stats()

        # Set random seed for reproducible quiz sequences
        if seed != 0:
            random.seed(seed)
        else:
            random.seed()

    def reset_stats(self) -> None:
        """Reset quiz statistics for new quiz session."""
        self.wrong_answers = []
        self.number_of_questions = 0
        self.correct_answers = 0

    def prepare_questions(
            self,
            slo2ita: bool = True,
            max_questions: int = 0,
            number_of_answers: int = 5
    ) -> List[Tuple[str, Item, List[Item]]]:
        """
        Prepare randomized quiz questions with multiple choice answers.

        This method generates a complete quiz by:
        1. Selecting random vocabulary items from the dictionary
        2. Finding appropriate wrong answers for each question
        3. Shuffling answer options to randomize positions

        Args:
            slo2ita: True for Slovenian->Italian, False for Italian->Slovenian
            max_questions: Maximum questions (0 for all available)
            number_of_answers: Number of multiple choice options

        Returns:
            List of tuples: (question_text, correct_answer, all_possible_answers)
        """
        # Determine quiz length
        if max_questions == 0:
            max_questions = len(self.dict_lang)

        # Create list of available questions (copy to avoid modifying original)
        dict_keys = list(self.dict_lang.keys())
        questions_and_answers = []

        # Generate questions until we reach the limit or run out of vocabulary
        while dict_keys and len(questions_and_answers) < max_questions:
            # Select random question and remove it from available pool
            current_question = random.choice(dict_keys)
            dict_keys.remove(current_question)

            # Select random correct answer for this question
            # (some questions may have multiple correct answers)
            correct_answer = random.choice(self.dict_lang[current_question])

            # Generate multiple choice options including the correct answer
            possible_answers = find_random_answers(
                self.dict_lang,
                current_question,
                correct_answer,
                number_of_answers,
                slo2ita
            )

            # Randomize answer order so correct answer isn't always in same position
            random.shuffle(possible_answers)

            # Store complete question data
            questions_and_answers.append((current_question, correct_answer, possible_answers))

        return questions_and_answers

    def run_quiz(
            self,
            slo2ita: bool = True,
            max_questions: int = 0,
            number_of_answers: int = 5
    ) -> Dict[str, Union[int, float]]:
        """
        Execute the complete interactive quiz session.

        This method runs the full quiz experience:
        - Displays questions with multiple choice answers
        - Collects and validates user input
        - Provides immediate feedback on each answer
        - Tracks performance statistics
        - Shows final results with detailed breakdown

        Args:
            slo2ita: Translation direction (True: Slo->Ita, False: Ita->Slo)
            max_questions: Maximum questions to ask (0 for unlimited)
            number_of_answers: Number of multiple choice options

        Returns:
            Dictionary with quiz results:
            - total_questions: Number of questions attempted
            - correct_answers: Number of correct responses  
            - score_percentage: Success rate as percentage
        """
        # Prepare all quiz questions
        questions_and_answers = self.prepare_questions(slo2ita, max_questions, number_of_answers)
        self.reset_stats()

        # Execute quiz question by question
        for current_pos, (current_question, correct_answer, possible_answers) in enumerate(questions_and_answers, 1):
            print(f"\nQuiz #{current_pos} / {len(questions_and_answers)}")

            # Display question based on translation direction
            if slo2ita:
                print(f"Cosa significa '{current_question}' ?")
            else:
                print(f"Cosa significa '{current_question}' ?")

            # Display multiple choice options
            for counter, answer in enumerate(possible_answers):
                # Show appropriate language based on quiz direction
                display_text = answer.italiansko if slo2ita else answer.slovensko
                print(f"{chr(ord('a') + counter)}: {display_text}")

            # Get and validate user input
            user_answer = self._get_user_input(possible_answers)
            if user_answer is None:  # User chose to quit
                break

            self.number_of_questions += 1

            # Check answer and provide feedback
            if correct_answer == user_answer:
                print("✓ Corretto!")
                self.correct_answers += 1
                print(f"Risposta: {correct_answer}")
            else:
                print("✗ Sbagliato")
                print(f"Risposta corretta: {correct_answer}")
                self.wrong_answers.append(correct_answer)

        # Display final results
        return self._display_results()

    def _get_user_input(self, possible_answers: List[Item]) -> Optional[Item]:
        """
        Get and validate user answer selection.

        This method handles:
        - Input validation (must be valid option letter)
        - Quit command recognition ('q')
        - Error handling for invalid input
        - Graceful handling of EOF/keyboard interrupts

        Args:
            possible_answers: List of answer options

        Returns:
            Selected Item object, or None if user quits
        """
        while True:
            try:
                data = input("Risposta (q per uscire): ").strip().lower()

                # Skip empty input
                if not data:
                    continue

                # Handle quit command
                if data == "q":
                    return None

                # Validate answer selection
                if len(data) == 1 and 'a' <= data <= chr(ord('a') + len(possible_answers) - 1):
                    answer_pos = ord(data) - ord('a')
                    return possible_answers[answer_pos]
                else:
                    print("Input non valido. Per favore scegli un input valido (a, b, c, etc.).")

            except (EOFError, KeyboardInterrupt):
                # Handle Ctrl+C or EOF gracefully
                print("\nQuiz interrotto dall'utente.")
                return None

    def _display_results(self) -> Dict[str, Union[int, float]]:
        """
        Display comprehensive quiz results and return statistics.

        Shows:
        - Overall performance statistics
        - Success percentage
        - Detailed list of incorrect answers for review

        Returns:
            Dictionary with numerical results for programmatic use
        """
        print("\n" + "=" * 50)
        print("QUIZ COMPLETD!")
        print("=" * 50)

        if self.number_of_questions > 0:
            # Calculate and display performance metrics
            ratio = (self.correct_answers / self.number_of_questions) * 100
            print(f"Numero di quiz: {self.number_of_questions}")
            print(f"Risposte corrette: {self.correct_answers}")
            print(f"Punteggio: {ratio:.1f}%")

            # Show incorrect answers for review
            if self.wrong_answers:
                print(f"\nRisposte sbagliate ({len(self.wrong_answers)}):")
                for answer in self.wrong_answers:
                    print(f"  • {answer}")
        else:
            ratio = 0
            print("Nessuna risposta è stata data.")

        return {
            "total_questions": self.number_of_questions,
            "correct_answers": self.correct_answers,
            "score_percentage": ratio
        }


# =============================================================================
# LEGACY COMPATIBILITY FUNCTIONS
# =============================================================================

def start_tests(
        dict_lang: Dict[str, List[Item]],
        int_seed: int = 0,
        slo2ita: bool = True,
        max_questions: int = 0,
        number_of_answers: int = 5
) -> Dict[str, Union[int, float]]:
    """
    Legacy function for backward compatibility with existing code.

    This function maintains the original interface while using the
    improved LanguageQuiz class internally. Existing lesson files
    (enota1.py, etc.) can continue using this function without modification.

    Args:
        dict_lang: Vocabulary dictionary
        int_seed: Random seed for reproducible quizzes
        slo2ita: Translation direction (True: Slo->Ita, False: Ita->Slo)
        max_questions: Maximum questions to ask
        number_of_answers: Multiple choice options count

    Returns:
        Quiz results dictionary with statistics
    """
    quiz = LanguageQuiz(dict_lang, int_seed)
    return quiz.run_quiz(slo2ita, max_questions, number_of_answers)


def prepare_list_of_questions_and_answers(
        dict_lang: Dict[str, List[Item]],
        slo2ita: bool = True,
        max_questions: int = 0,
        number_of_answers: int = 5
) -> List[Tuple[str, Item, List[Item]]]:
    """
    Legacy function for preparing quiz questions without running the quiz.

    Maintained for backward compatibility with code that needs to prepare
    questions but handle the quiz interface differently.

    Args:
        dict_lang: Vocabulary dictionary
        slo2ita: Translation direction
        max_questions: Maximum questions to prepare
        number_of_answers: Multiple choice options count

    Returns:
        List of prepared question tuples
    """
    quiz = LanguageQuiz(dict_lang, 0)
    return quiz.prepare_questions(slo2ita, max_questions, number_of_answers)


def generic_run_me(enota_dict):
    dict_slo, dict_ita = process_dictionary(enota_dict)

    if Item._all_question_groups:
        print()
        print(f"Gruppi di domande (numero totale quiz: {len(Item._all_instances)}):")
        # print(Item._all_question_groups)
        for k,v in Item._all_question_groups.items():
            # print(f"{k}: {v}")
            # print(f"len: {len(v)}")
            print(f"'{k}': {len(v)} quiz")

        print()
    print(f"slo items: {len(dict_slo)}")
    print(f"ita items: {len(dict_ita)}")
    print()

    print("1 - test da sloveno a italiano")
    print("2 - test da italiano a sloveno")
    data = input("risposta (q per uscire, s per statistiche): ")
    if data is None or data == "q":
        return
    elif data == "1":
        start_tests(dict_slo)
    elif data == "2":
        start_tests(dict_ita, slo2ita=False)
    elif data == "s":
        print(f"numero di istanze di Item: {len(dict_slo)}")
        # how many questions are there?
        questions = Item.get_all_questions()

        print(f"numero di domande: {len(questions)}")
    else:
        print("risposta non valida")
