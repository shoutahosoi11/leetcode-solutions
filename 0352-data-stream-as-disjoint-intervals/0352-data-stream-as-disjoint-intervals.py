from typing import List


class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        arr = sorted(self.nums)
        if not arr:
            return []

        res = []
        start = arr[0]
        end = arr[0]

        for i in range(1, len(arr)):
            if arr[i] == end + 1:
                end = arr[i]
            else:
                res.append([start, end])
                start = arr[i]
                end = arr[i]

        res.append([start, end])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()