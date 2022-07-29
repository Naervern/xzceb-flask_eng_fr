## Author: Naervern (Antonio Maximiano)
## Done for IBM's Python Project for AI & App Dev course

import unittest
from translator import frenchToEnglish, englishToFrench

class TestEn_Fr (unittest.TestCase):
    def test_english(self):
        self.assertIsNotNone(englishToFrench(""))
	self.assertEqual(englishToFrench(""), "Error: no input")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
	self.assertEqual(englishToFrench("Yes"), "Oui")
	self.assertEqual(englishToFrench("I speak Portuguese"), "Je parle portugais")
	self.assertNotEqual(englishToFrench("Hello"), "Hello")
	self.assertNotEqual(englishToFrench("Victory"), "Capitulation")

class TestFr_En (unittest.TestCase):
    def test_french(self):
	self.assertIsNotNone(frenchToEnglish(""))
        self.assertEqual(frenchToEnglish(""), "Error: no input")
	self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
	self.assertEqual(frenchToEnglish("Oui"), "Yes")
	self.assertEqual(frenchToEnglish("Je parle portugais"), "I speak Portuguese")
	self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")
	self.assertEqual(frenchToEnglish("Capitulation"), "Victory")
