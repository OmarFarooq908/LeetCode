import unittest
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for index,value in enumerate(nums):
            if value == val:
                last_index = -1
                while value == nums[last_index]:
                    last_index = last_index - 1
                    if last_index == -len(nums):
                        break
                temp = nums[last_index]
                nums[last_index] = value
                nums[index] = temp
                k = k - 1
        return k

class TestRemoveElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expectedNums = [2, 2]  # Order can be different
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertCountEqual(nums[:k], expectedNums)  # Check unordered match

    def test_case_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expectedNums = [0, 1, 3, 0, 4]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertCountEqual(nums[:k], expectedNums)

    def test_case_3(self):
        nums = [1, 1, 1, 1, 1]
        val = 1
        expectedNums = []
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertCountEqual(nums[:k], expectedNums)

    def test_case_4(self):
        nums = [4, 5, 6, 7, 8]
        val = 3
        expectedNums = [4, 5, 6, 7, 8]
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertCountEqual(nums[:k], expectedNums)

    def test_case_5(self):
        nums = []
        val = 1
        expectedNums = []
        k = self.solution.removeElement(nums, val)
        self.assertEqual(k, len(expectedNums))
        self.assertCountEqual(nums[:k], expectedNums)

if __name__ == '__main__':
    unittest.main()

