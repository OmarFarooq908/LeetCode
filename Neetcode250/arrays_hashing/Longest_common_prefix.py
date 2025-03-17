from typing import List
import unittest

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_length = len(min(strs))
        dictionary = {index: value for index, value in enumerate(strs)}
        # Min element
        # Dictionary
        for i in range(min_length):
            temp = ""
            for index, word in enumerate(strs):
                if temp == "":
                    res += word[i]
                elif temp != word[i]:
                    if res != "":
                        res = res[:-1]
                    return res
                temp = word[i]
        return res
class TestLongestCommonPrefix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_standard_case(self):
        # Standard case with a common prefix
        strs = ["flower", "flow", "flight"]
        result = self.solution.longestCommonPrefix(strs)
        self.assertEqual(result, "fl")

    def test_no_common_prefix(self):
        # Case where there is no common prefix
        strs = ["dog", "racecar", "car"]
        result = self.solution.longestCommonPrefix(strs)
        self.assertEqual(result, "")

    def test_all_identical_strings(self):
        # Case where all strings are the same
        strs = ["test", "test", "test"]
        result = self.solution.longestCommonPrefix(strs)
        self.assertEqual(result, "test")

    def test_one_empty_string(self):
        # Case where one string is empty
        strs = ["", "b", "c"]
        result = self.solution.longestCommonPrefix(strs)
        self.assertEqual(result, "")

    def test_all_empty_strings(self):
        # Case where all strings are empty
        strs = ["", "", ""]
        result = self.solution.longestCommonPrefix(strs)
        self.assertEqual(result, "")

    def test_single_element(self):
        # Case with only one string in the list
        strs = ["alone"]
        result = self.solution.longestCommonPrefix(strs)
        self.assertEqual(result, "alone")

    def test_common_prefix_full_word(self):
        # Case where one word is a prefix of another
        strs = ["abc", "abcde", "abcdef"]
        result = self.solution.longestCommonPrefix(strs)
        self.assertEqual(result, "abc")

    def test_mixed_case(self):
        # Case-sensitive test
        strs = ["Hello", "helicopter", "hexagon"]
        result = self.solution.longestCommonPrefix(strs)
        self.assertEqual(result, "")

    def test_large_input(self):
        # Large input case
        strs = ["a" * 1000, "a" * 999, "a" * 998]
        result = self.solution.longestCommonPrefix(strs)
        self.assertEqual(result, "a" * 998)

if __name__ == '__main__':
    unittest.main()