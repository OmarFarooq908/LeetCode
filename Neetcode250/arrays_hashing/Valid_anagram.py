class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency_s = {}
        frequency_t = {}
        for value in s:
            frequency_s[value] = frequency_s.get(value, 0) + 1

        for value in t:
            frequency_t[value] = frequency_t.get(value, 0) + 1

        for key, value in frequency_s.items():
            if key not in frequency_t:
                return False
            if value != frequency_t.get(key):
                return False
        return True