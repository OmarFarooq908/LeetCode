from typing import List
import unittest
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for index, x in enumerate(strs):
            sorted_string = ''.join(sorted(x))
            my_dict[sorted_string].append(index)

        anagram_list = []
        for key, value in my_dict.items():
            group = [strs[x] for x in value]
            anagram_list.append(group)

        return anagram_list


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
