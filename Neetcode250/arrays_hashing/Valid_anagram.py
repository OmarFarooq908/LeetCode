class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_s = set()
        char_t = set()
        for value in s:
            char_s.add(value)

        for value in t:
            char_t.add(value)
        
        for value in char_s:
            if value not in char_t:
                return False
        return True