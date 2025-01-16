import unittest
from Welsh_Dictionary_Sorting_Solution import sortWelsh

class TestWelshDictionarySorting(unittest.TestCase):
    def test_cases(self):
        with open('technichal-interview/Welsh-Dictionary-String/Welsh-Dictionary-Sorting-Testcases.txt', 'r') as file:
            lines = file.readlines()
        
        t = int(lines[0].strip())
        index = 1
        for _ in range(t):
            while not lines[index].strip():
                index += 1
            n = int(lines[index].strip())
            index += 1
            while not lines[index].strip():
                index += 1
            words = lines[index].strip().split()
            index += 1
            while not lines[index].strip():
                index += 1
            expected_output = lines[index].strip().replace("Expected Output: ", "").split()
            index += 1
            
            sorted_words = sortWelsh(words)
            self.assertEqual(sorted_words, expected_output)

if __name__ == '__main__':
    unittest.main()