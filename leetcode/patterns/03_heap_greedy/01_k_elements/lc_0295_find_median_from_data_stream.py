"""
LeetCode 295 - Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Pattern:
Two Heaps (Max Heap + Min Heap)
"""


class MedianFinder:

	def __init__(self):
		pass

	def addNum(self, num: int) -> None:
		pass

	def findMedian(self) -> float:
		pass


# Example 1: Output [null, null, null, 1.5, null, 2.0]
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())  # 1.5
mf.addNum(3)
print(mf.findMedian())  # 2.0
