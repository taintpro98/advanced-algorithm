# WorldQuant Interview Preparation

This directory contains curated algorithm problems and study materials for software engineering interviews at quantitative trading firms like WorldQuant, Jane Street, Hudson River Trading, Two Sigma, and Citadel.

## Directory Structure

```
worldquant/
├── README.md                          # This file
├── quant_interview_notes.md           # Interview strategies and patterns
├── probability_and_brainteasers.md    # Logic puzzles and probability
└── problems/
    ├── 01_hashing_sliding_window/     # Hash tables and sliding window
    ├── 02_heap_priority_queue/        # Heaps and priority queues
    ├── 03_binary_search/              # Binary search variations
    ├── 04_graph_algorithms/           # Graph traversal and algorithms
    ├── 05_dynamic_programming/        # DP patterns
    ├── 06_advanced_structures/        # Union-Find, Segment Tree, etc.
    └── 07_greedy/                     # Greedy algorithms
```

## Problem Index

### 01. Hashing & Sliding Window (7 problems)

| # | Problem | Difficulty | Key Pattern |
|---|---------|------------|-------------|
| 1 | [Two Sum](problems/01_hashing_sliding_window/001_two_sum.md) | Easy | Hash Table |
| 2 | [Longest Substring Without Repeating](problems/01_hashing_sliding_window/002_longest_substring_without_repeating.md) | Medium | Sliding Window |
| 3 | [Minimum Window Substring](problems/01_hashing_sliding_window/003_minimum_window_substring.md) | Hard | Sliding Window + Hash |
| 4 | [Subarray Sum Equals K](problems/01_hashing_sliding_window/004_subarray_sum_equals_k.md) | Medium | Prefix Sum + Hash |
| 5 | [Sliding Window Maximum](problems/01_hashing_sliding_window/005_sliding_window_maximum.md) | Hard | Monotonic Deque |
| 6 | [LRU Cache](problems/01_hashing_sliding_window/006_lru_cache.md) | Medium | Hash + Linked List |
| 7 | [Group Anagrams](problems/01_hashing_sliding_window/007_group_anagrams.md) | Medium | Hash with Custom Key |

### 02. Heap & Priority Queue (6 problems)

| # | Problem | Difficulty | Key Pattern |
|---|---------|------------|-------------|
| 1 | [Find Median from Data Stream](problems/02_heap_priority_queue/001_find_median_data_stream.md) | Hard | Two Heaps |
| 2 | [Merge K Sorted Lists](problems/02_heap_priority_queue/002_merge_k_sorted_lists.md) | Hard | Min Heap |
| 3 | [Top K Frequent Elements](problems/02_heap_priority_queue/003_top_k_frequent_elements.md) | Medium | Heap / Bucket Sort |
| 4 | [Meeting Rooms II](problems/02_heap_priority_queue/004_meeting_rooms_ii.md) | Medium | Interval + Heap |
| 5 | [Task Scheduler](problems/02_heap_priority_queue/005_task_scheduler.md) | Medium | Greedy + Heap |
| 6 | [The Skyline Problem](problems/02_heap_priority_queue/006_skyline_problem.md) | Hard | Line Sweep + Heap |

### 03. Binary Search (5 problems)

| # | Problem | Difficulty | Key Pattern |
|---|---------|------------|-------------|
| 1 | [Search in Rotated Sorted Array](problems/03_binary_search/001_search_rotated_array.md) | Medium | Modified Binary Search |
| 2 | [Koko Eating Bananas](problems/03_binary_search/002_koko_eating_bananas.md) | Medium | Binary Search on Answer |
| 3 | [Median of Two Sorted Arrays](problems/03_binary_search/003_median_two_sorted_arrays.md) | Hard | Binary Search on Partition |
| 4 | [Find First and Last Position](problems/03_binary_search/004_find_first_last_position.md) | Medium | Lower/Upper Bound |
| 5 | [Split Array Largest Sum](problems/03_binary_search/005_split_array_largest_sum.md) | Hard | Binary Search on Answer |

### 04. Graph Algorithms (5 problems)

| # | Problem | Difficulty | Key Pattern |
|---|---------|------------|-------------|
| 1 | [Course Schedule](problems/04_graph_algorithms/001_course_schedule.md) | Medium | Topological Sort |
| 2 | [Number of Islands](problems/04_graph_algorithms/002_number_of_islands.md) | Medium | BFS/DFS |
| 3 | [Network Delay Time](problems/04_graph_algorithms/003_network_delay_time.md) | Medium | Dijkstra |
| 4 | [Clone Graph](problems/04_graph_algorithms/004_clone_graph.md) | Medium | DFS + Hash |
| 5 | [Word Ladder](problems/04_graph_algorithms/005_word_ladder.md) | Hard | BFS on Implicit Graph |

### 05. Dynamic Programming (6 problems)

| # | Problem | Difficulty | Key Pattern |
|---|---------|------------|-------------|
| 1 | [Best Time to Buy and Sell Stock Series](problems/05_dynamic_programming/001_best_time_stock.md) | E/M/H | State Machine DP |
| 2 | [Longest Increasing Subsequence](problems/05_dynamic_programming/002_longest_increasing_subsequence.md) | Medium | DP + Binary Search |
| 3 | [Coin Change](problems/05_dynamic_programming/003_coin_change.md) | Medium | Unbounded Knapsack |
| 4 | [Word Break](problems/05_dynamic_programming/004_word_break.md) | Medium | String DP |
| 5 | [House Robber Series](problems/05_dynamic_programming/005_house_robber.md) | Medium | Linear/Tree DP |
| 6 | [Edit Distance](problems/05_dynamic_programming/006_edit_distance.md) | Medium | 2D String DP |

### 06. Advanced Data Structures (3 problems)

| # | Problem | Difficulty | Key Pattern |
|---|---------|------------|-------------|
| 1 | [Accounts Merge](problems/06_advanced_structures/001_accounts_merge.md) | Medium | Union-Find |
| 2 | [Range Sum Query - Mutable](problems/06_advanced_structures/002_range_sum_query_mutable.md) | Medium | Segment Tree / BIT |
| 3 | [Count of Smaller Numbers After Self](problems/06_advanced_structures/003_count_smaller_after_self.md) | Hard | Merge Sort / BIT |

### 07. Greedy (2 problems)

| # | Problem | Difficulty | Key Pattern |
|---|---------|------------|-------------|
| 1 | [Jump Game Series](problems/07_greedy/001_jump_game.md) | Medium | Greedy |
| 2 | [Non-overlapping Intervals](problems/07_greedy/002_non_overlapping_intervals.md) | Medium | Interval Scheduling |

## Study Materials

### Core Documents

1. **[Quant Interview Notes](quant_interview_notes.md)**
   - Common problem-solving patterns
   - Interview expectations
   - Communication strategies
   - Example reasoning

2. **[Probability & Brainteasers](probability_and_brainteasers.md)**
   - Classic probability problems
   - Expected value calculations
   - Logic puzzles
   - Market/trading puzzles

## Recommended Study Order

### Week 1-2: Foundations
- [ ] Hash Table and Sliding Window problems
- [ ] Binary Search variations
- [ ] Review probability basics

### Week 3-4: Core Algorithms
- [ ] Heap and Priority Queue
- [ ] Graph algorithms (BFS, DFS, Dijkstra)
- [ ] Basic DP patterns

### Week 5-6: Advanced Topics
- [ ] Advanced DP (state machine, optimization)
- [ ] Union-Find and Segment Tree
- [ ] Greedy algorithms with proofs

### Week 7-8: Integration & Practice
- [ ] Mixed problem practice
- [ ] Probability and brainteasers
- [ ] Mock interviews

## Problem Difficulty Distribution

- Easy: 1 problem
- Medium: 24 problems
- Hard: 9 problems

**Total: 34 core problems** (with series counting as single entries)

## Tips for Quant Interviews

1. **Speed matters** - Practice solving mediums in 15-20 minutes
2. **Explain as you code** - Verbalize your thought process
3. **Optimize first** - Don't settle for brute force
4. **Know your complexities** - Instant recognition of O(n) vs O(n log n)
5. **Handle edge cases** - Financial data is messy
6. **Mathematical rigor** - Be ready to prove correctness

## Contributing

When adding new problems, follow this template:
- Problem name and LeetCode link
- Difficulty and pattern category
- Why it's important for quant interviews
- Solution with explanation
- Complexity analysis
- Edge cases
- Related problems

Good luck with your interviews!
