# Binary Search Cheat Sheet (Templates + Examples)

This cheat sheet summarizes the **three core binary search patterns** you must master:
- Find the smallest valid value
- Find the largest valid value
- Find an exact value

These patterns cover **90%+** of binary search problems in interviews and contests.

---

## 1. Find the **Smallest** Value That Satisfies a Condition
(Lower Bound)

### Problem Shape
We want the **minimum x** such that `check(x)` is true.

```
False False False True True True
```

### Template
```python
l, r = L, R  # r must be a valid answer

while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1

return l
```

### When to Use
- "minimum x such that ..."
- "smallest possible ..."
- "first position where ..."

### Representative Problems
- LeetCode 878 – Nth Magical Number  
  https://leetcode.com/problems/nth-magical-number/
- LeetCode 875 – Koko Eating Bananas  
  https://leetcode.com/problems/koko-eating-bananas/
- LeetCode 774 – Minimize Max Distance to Gas Station  
  https://leetcode.com/problems/minimize-max-distance-to-gas-station/

---

## 2. Find the **Largest** Value That Satisfies a Condition
(Upper Bound)

### Problem Shape
We want the **maximum x** such that `check(x)` is true.

```
True True True False False False
```

### Template
```python
l, r = L, R  # l must be a valid answer

while l < r:
    mid = (l + r + 1) // 2  # +1 prevents infinite loop
    if check(mid):
        l = mid
    else:
        r = mid - 1

return l
```

### When to Use
- "maximum x such that ..."
- "largest possible ..."
- "last position where ..."

### Representative Problems
- LeetCode 410 – Split Array Largest Sum  
  https://leetcode.com/problems/split-array-largest-sum/
- LeetCode 1011 – Capacity To Ship Packages Within D Days  
  https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
- LeetCode 1552 – Magnetic Force Between Two Balls  
  https://leetcode.com/problems/magnetic-force-between-two-balls/

---

## 3. Find an **Exact** Value in a Sorted Array
(Classic Binary Search)

### Requirement
- Array must be **sorted**

### Template
```python
l, r = 0, n - 1

while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1

return -1
```

### When to Use
- Search for an element
- Find index of a value in sorted data

### Representative Problems
- LeetCode 704 – Binary Search  
  https://leetcode.com/problems/binary-search/
- LeetCode 35 – Search Insert Position  
  https://leetcode.com/problems/search-insert-position/
- LeetCode 34 – Find First and Last Position of Element in Sorted Array  
  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

---

## Key Rules to Remember
- Binary search works on **monotonic conditions**, not just arrays
- Never apply modulo inside `check()`
- Decide clearly: **smallest**, **largest**, or **exact**
- Choose mid carefully (`+1` matters for upper bound)

---

## One-Line Summary
> Binary search is about exploiting monotonicity, not about searching arrays.
