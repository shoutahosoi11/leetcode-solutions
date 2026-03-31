class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and i-k <= dic[num]:#ここで２回アクセス
                return True
            dic[num] = i
        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, num in enumerate(nums):
            # get(num, -1) は「なければ -1 を返す」
            # これにより num in dic のチェックを省略できる
            prev_index = dic.get(num, -1)
            if prev_index != -1 and i - prev_index <= k:
                return True
            dic[num] = i
        return False