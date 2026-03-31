class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        prev = 0
        for i in range(len(s)):
            index = len(s)-1-i
            
            sindex = dic[s[index]]
            if 0 < i and sindex < prev:
                total -= sindex
            else:
                total += sindex
            prev = sindex
        return total
#１の位から見ていくことで下がったら（＜）ーすることを利用する
#下がって上がったところだとむずい