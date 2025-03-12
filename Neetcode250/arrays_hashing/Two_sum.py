import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in dictionary:
                return [dictionary[complement], index]
            dictionary[value] = index
        
        return []

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_case(self):
        # Standard test case from the problem statement
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 1])
    
    def test_duplicate_elements(self):
        # Test with duplicate elements in the list
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 1])
    
    def test_negative_numbers(self):
        # Test with negative numbers
        nums = [-3, 4, 3, 90]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 2])
    
    def test_mixed_numbers(self):
        # Test with a mix of positive and negative numbers
        nums = [-1, 0, 1, 2, -1, -4]
        target = 0
        # One valid answer might be indices [0, 2] since -1 + 1 == 0.
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), [0, 2])
    
if __name__ == '__main__':
    unittest.main()