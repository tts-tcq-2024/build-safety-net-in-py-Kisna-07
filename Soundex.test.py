import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_all_vowels(self):
        self.assertEqual(generate_soundex("AEIOU"), "A000")

    def test_name_with_same_sound_codes(self):
        self.assertEqual(generate_soundex("Tymczak"), "T522")
        self.assertEqual(generate_soundex("Pfister"), "P236")

    def test_name_with_different_cases(self):
        self.assertEqual(generate_soundex("Jackson"), "J250")
        self.assertEqual(generate_soundex("jackson"), "J250")

    def test_name_with_h_and_w(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Ashcroft"), "A261")

    def test_name_with_zeros(self):
        self.assertEqual(generate_soundex("Smythe"), "S530")

    def test_longer_name(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")

    def test_names_that_should_produce_same_soundex(self):
        self.assertEqual(generate_soundex("Smith"), "S530")
        self.assertEqual(generate_soundex("Smyth"), "S530")
        self.assertEqual(generate_soundex("Smythe"), "S530")

if __name__ == '__main__':
    unittest.main()
