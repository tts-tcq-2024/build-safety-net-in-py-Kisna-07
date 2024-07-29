import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")

    def test_basic_functionality(self):
        self.assertEqual(generate_soundex("Robert"), "R163")
        self.assertEqual(generate_soundex("Rupert"), "R163")
        self.assertEqual(generate_soundex("Rubin"), "R150")

    def test_adjacent_same_code(self):
        self.assertEqual(generate_soundex("Pfister"), "P236")

    def test_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("R2obert"), "R163")
        self.assertEqual(generate_soundex("Ru@pe#rt"), "R163")
        self.assertEqual(generate_soundex("Rub1in"), "R150")

    def test_special_characters_h_w(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Ashcroft"), "A261")

    def test_padding_with_zeros(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("AB"), "A100")
        self.assertEqual(generate_soundex("ABC"), "A120")
        self.assertEqual(generate_soundex("ABCD"), "A123")

    def test_complex_cases(self):
        self.assertEqual(generate_soundex("Gutierrez"), "G362")
        self.assertEqual(generate_soundex("VanBuren"), "V516")
        self.assertEqual(generate_soundex("Deutsche"), "D320")

if __name__ == '__main__':
    unittest.main()
