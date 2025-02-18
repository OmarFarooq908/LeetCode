from typing import List
import unittest

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if (len(strs) > 1):
            pass

        return strs


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
