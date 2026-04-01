class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans

 # 片方が極端に短い時は２分探索
def intersect_binary_search(nums1, nums2):
    # nums1を短い方、nums2を長い方（かつソート済み）とする
    nums1.sort()
    nums2.sort()
    if len(nums1) > len(nums2):
        return intersect_binary_search(nums2, nums1)
    
    result = []
    # nums2を探索する際の、左側の境界線（重複して同じ要素を取らないため）
    left_bound = 0 
    
    for num in nums1:
        # nums2の中から num を二分探索で探す
        left = left_bound
        right = len(nums2) - 1
        found_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums2[mid] == num:
                # 見つかった場合でも、一番左側（最小インデックス）の重複要素を見つけるために右端を狭める
                found_index = mid
                right = mid - 1
            elif nums2[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
                
        # 見つかった場合、結果に追加し、次回以降はその次から探索する
        if found_index != -1:
            result.append(num)
            left_bound = found_index + 1
            
    return result
