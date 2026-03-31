# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        dic = set()
        while current is not None:
            if current in dic:
                return True
            dic.add(current)
            current = current.next
        return False
#連結リストはcurrent = headで初期値は0番目でcurrent.nextで次に行く
#setは重複なしだし辞書より重くない