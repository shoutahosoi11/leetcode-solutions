class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1set = set()
        ansset = set()
        for num1 in nums1:
            nums1set.add(num1)
        for num2 in nums2:
            if num2 in nums1set:
                ansset.add(num2)
        anslist = [*ansset]
        return anslist
        