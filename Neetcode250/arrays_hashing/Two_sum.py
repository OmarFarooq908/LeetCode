class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, value in enumerate(nums):
            dictionary[index] = value
        
        for key, value in dictionary.items():
            complement = target - value
            j = list(dictionary.keys())[list(dictionary.values()).index(complement)]
            if j:
                return key, j