import unittest
from random_words_genrator.words import generate_random_words

class TestWords(unittest.TestCase):
   def test_generate_random_words(self):
      words = generate_random_words()
      self.assertEqual(len(words), 8)
      for word in words:
         self.assertIsInstance(word, str)
         
   def test_generate_random_words_with_specific_number(self):
      """Teste que la fonction génère le nombre spécifié de mots."""
      num_words = 5
      words = generate_random_words(num_words)
      self.assertEqual(len(words), num_words)

   def test_generate_random_words_with_zero(self):
      """Teste que la fonction gère correctement un nombre de mots de 0."""
      num_words = 0
      words = generate_random_words(num_words)
      self.assertEqual(len(words), 0)

if __name__ == '__main__':
    unittest.main()
