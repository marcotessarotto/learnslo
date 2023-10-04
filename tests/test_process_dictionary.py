import unittest
import contextlib
from enum import Enum

from utilities import BookPage, WordType, Level, Gender, WebLink, process_dictionary, Item


# Your provided class implementations here

class TestProcessDictionary(unittest.TestCase):

    def test_process_dictionary(self):
        my_dict = {
            'category1': [
                ['slo1', 'ita1', WordType.VERB, Level.EASY, Gender.MALE, WebLink('http://example.com')],
                # Add other rows as needed
            ],
            # Add other categories as needed
        }

        dict_slo, dict_ita = process_dictionary(my_dict)

        # Check if the dictionaries are not empty
        self.assertTrue(dict_slo)
        self.assertTrue(dict_ita)

        # print(dict_slo)
        # print(dict_ita)

        # Check the contents of the dictionaries
        for key, item in dict_slo.items():
            self.assertEqual(item[0].slovensko, key)
            self.assertTrue(isinstance(item[0], Item))
            # Add more assertions based on the expected attributes of the item

            # print(item)

        for key, item in dict_ita.items():
            self.assertEqual(item[0].italiansko, key)
            self.assertTrue(isinstance(item[0], Item))
            # Add more assertions based on the expected attributes of the item

            # print(item)

    def test_multiterms_dictionary(self):
        my_dict = {
            'category1': (
                ('slo1', ('ita1', 'ita2')),
                # Add other rows as needed
            ),
            # Add other categories as needed
        }

        dict_slo, dict_ita = process_dictionary(my_dict)

        # Check if the dictionaries are not empty
        self.assertTrue(dict_slo)
        self.assertTrue(dict_ita)

        # print(dict_slo)
        # print(dict_ita)
        # print()

        for key, item in dict_slo.items():
            self.assertEqual(item[0].slovensko, key)
            self.assertTrue(isinstance(item[0], Item))
            # Add more assertions based on the expected attributes of the item

            # print(item)



if __name__ == '__main__':
    unittest.main()
