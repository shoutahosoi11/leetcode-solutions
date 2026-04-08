from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        diff = Counter(ransomNote) - Counter(magazine)

        if diff:
            return False
        else:
            return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for ch in magazine:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True
