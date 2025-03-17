from typing import List
import unittest
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            # Creating count for 26 characters
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Use the tuple of counts as the key
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_example_case(self):
        # Example test case
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        result = self.sol.groupAnagrams(input_strs)

        # Sorting inner lists and the outer list for comparison, since order doesn't matter

        self.assertEqual(
                sorted([sorted(group) for group in result]),
                sorted([sorted(group) for group in expected])
                )

        def test_empty_list(self):
            # Test for an empty input list
            input_strs = []
            expected = []
            result = self.sol.groupAnagrams(input_strs)
            self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main()
