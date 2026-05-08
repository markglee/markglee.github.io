import unittest

SMALL_WORD_LIST = "words.txt"

def anagrams_from_file (file):
   try:
      file_handle = open (file)
      word_list = []
      for word in file_handle :
         word_list.append(word.strip())
      for word in word_list:
         all_permutations = generate_permutations (word)

         # if permutation is a word in the word list
         # add to anagrams
         print(list_overlap(all_permutations, word_list))
         
   finally : file_handle.close()

def list_overlap(list1, list2):
   # refactor to change variable name!
   overlap_list = []
   for item in list1 :
      if item in list2 :
         overlap_list.append(item)
   return overlap_list
         
   
 

def generate_permutations (word):
   if len(word) == 1 : return [word]
   else :
      first = word[0]
      rest = word[1:]
      subword_list = generate_permutations (rest)
      word_list = []
      for subword in subword_list :
         for position in range(len(subword)+1) :
            new_word = subword[:position] + first + subword[position:]
            word_list.append(new_word)
      return word_list



class file_test_cases (unittest.TestCase) :
   def test_file_exists (self) :
        file = open (SMALL_WORD_LIST, 'r')
        try:
            file.read()
        finally : file.close()

   def test_first_word (self) :
      file = open (SMALL_WORD_LIST, 'r')
      try:
         self.assertEqual(file.readline().strip(), 'artist')
      finally : file.close()

   def test_read_all_words (self) :
      file = open (SMALL_WORD_LIST, 'r')
      try:
         list_ = []
         for word in file :
            list_.append(word.strip())
         self.assertEqual(len(list_), 30)
      finally : file.close()



class anagram_test_cases(unittest.TestCase) :
   def test_permutations_of_a(self) :
      
        self.assertEqual(generate_permutations('a'), ['a'])
        
   def test_permutations_of_ab(self) :
        self.assertEqual(generate_permutations('ab'), ['ab', 'ba'])

   def test_permutations_of_abc(self) :
        self.assertEqual(generate_permutations('abc'), ['abc', 'bac', 'bca',
                                                        'acb','cab', 'cba'])

   def test_list_overlap_include (self) :
      self.assertEqual(list_overlap(['ab','ba'],['ab','ba']), ['ab','ba'])

   def test_list_overlap_dont_include (self) :
      self.assertEqual(list_overlap(['ab','ba'],['ab']), ['ab'])        



unittest.main()
