class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 長さが違えば即終了 (Early Return)
        if len(s) != len(t):
            return False
            
        count = {}
        
        # sの文字をカウントアップ
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # tの文字をカウントダウン
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            # 回数がマイナスになったら、文字の出現頻度が合わないということ
            if count[char] < 0:
                return False
                
        # 最終的にすべての値が0になっているはず（長さが同じなので、負の値がなければ0になる）
        return True