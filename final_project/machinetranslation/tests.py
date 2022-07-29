'''
Author: Naervern (Antonio Maximiano)
Done for IBM's Python Project for AI & App Dev course
'''

import unittest
from translator import french_to_english, english_to_french

class TestEn_Fr (unittest.TestCase):
    def test_english(self):
        self.assertIsNotNone(english_to_french(""))
        self.assertEqual(english_to_french(""), "Error: no input")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Yes"), "Oui")
        self.assertEqual(english_to_french("I speak Portuguese"), "Je parle portugais")
        self.assertNotEqual(english_to_french("Hello"), "Hello")
        self.assertNotEqual(english_to_french("Victory"), "Capitulation")

class TestFr_En (unittest.TestCase):
    def test_french(self):
        self.assertIsNotNone(french_to_english(""))
        self.assertEqual(french_to_english(""), "Error: no input")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Oui"), "Yes")
        self.assertEqual(french_to_english("Je parle portugais"), "I speak Portuguese")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        self.assertEqual(french_to_english("Capitulation"), "Victory")

unittest.main()