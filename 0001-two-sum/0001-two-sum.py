class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumDic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in twoSumDic:
                return [twoSumDic[diff], i]
            twoSumDic[nums[i]] = i
#辞書に格納することでforのネストを回避
#数字と対応するiが必要だから辞書使っていい
        