class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumnums = sum(nums)
        lenlist = len(nums)
        ans = lenlist*(lenlist+1)//2 - sumnums
        return ans