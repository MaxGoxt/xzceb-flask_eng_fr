""" Test module """
import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestTranslateEnToFr(unittest.TestCase):
    """Class to test the function english_to_french"""
    def test1(self):
        """
        Function to test the function english_to_french
        """
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french("Bonjour"),"Hello")

class TestTranslateFrToEn(unittest.TestCase):
    """Class to test the function french_to_english"""
    def test1(self):
        """
        Function to test the function french_to_english
        """
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english("Hello"),"Bonjour")

if __name__ == "__main__":
    unittest.main()
