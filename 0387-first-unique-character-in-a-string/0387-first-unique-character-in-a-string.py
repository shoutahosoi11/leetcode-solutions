class Solution:
    def firstUniqChar(self, s: str) -> int:
        sdic = {}
        sset = set()
        for i in range(len(s)):
            if s[i] not in sset:
                sset.add(s[i])
                sdic[s[i]] = i
            else:
                sdic.pop(s[i], None)
        if sdic == {}:
            return -1
        else:
            return min(sdic.values())