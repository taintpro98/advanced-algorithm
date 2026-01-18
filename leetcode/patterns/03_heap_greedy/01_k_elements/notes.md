# K Elements (Top K, Kth Largest/Smallest)

## What This Subtopic Is About

Finding K largest/smallest elements or the Kth element efficiently using heaps. This pattern leverages heap properties to maintain a dynamic set of top elements with O(log n) insertions, avoiding the O(n log n) cost of full sorting.

## Typical Patterns & Invariants

- **Min heap of size K**: Maintain K largest elements (root is Kth largest)
- **Max heap of size K**: Maintain K smallest elements (root is Kth smallest)
- **Two heaps**: Balance elements between min and max heaps for median finding
- **Lazy deletion**: Mark elements as deleted without immediately removing
- **Online algorithm**: Process stream of elements dynamically

## How to Recognize This Type of Problem

- "Find Kth largest/smallest element"
- "Top K frequent elements"
- "Median in data stream"
- Processing elements one at a time with partial ordering
- Avoiding full sort when only K elements needed

## LeetCode Problems

- [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
