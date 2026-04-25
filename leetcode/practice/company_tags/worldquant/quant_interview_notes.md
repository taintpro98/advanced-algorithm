# Quant Interview Notes for Software Engineers

## Overview

Quantitative trading firms like WorldQuant, Jane Street, Hudson River Trading, Two Sigma, and Citadel have rigorous technical interviews that test both algorithmic problem-solving and systems thinking. This guide covers common patterns, expectations, and strategies for success.

---

## Common Problem-Solving Patterns

### 1. Efficiency-First Thinking

Quant firms deal with massive data streams and require sub-millisecond latency. Interviewers expect:

- **Optimal time complexity** as the baseline, not a stretch goal
- **Space-time tradeoffs** explained clearly (when to use O(n) space for O(1) time)
- **Cache-friendly solutions** - discuss memory access patterns when relevant

**Example reasoning:**
> "The naive O(n²) approach processes 1 million records in ~10 minutes. With the hash-based O(n) solution, we're down to ~10ms. For our tick data processing, this is the difference between real-time and delayed signals."

### 2. Mathematical Rigor

Expect to prove your solutions work:

- **Loop invariants** - what property holds at each iteration?
- **Recurrence relations** - how does DP state transition?
- **Amortized analysis** - why is dynamic array O(1) append?

### 3. Edge Case Awareness

Financial data is messy. Always consider:

- Empty inputs, single elements
- Integer overflow (stock prices × volumes)
- Floating-point precision issues
- Negative values, zeros
- Duplicates and ties
- Sorted vs unsorted assumptions

### 4. Problem Decomposition

Break complex problems into recognizable sub-problems:

```
"Find the maximum profit with at most k transactions"
   ↓ decompose
"State machine with buy/sell states" + "DP with transaction count"
```

---

## Core Algorithmic Patterns for Quant Interviews

### Pattern 1: Sliding Window / Two Pointers

**Why it matters:** Real-time data streams, moving averages, VWAP calculations

**Key problems:**
- Maximum subarray sum in window
- Minimum window substring
- Longest substring without repeating characters

**Template:**
```python
def sliding_window(arr, k):
    window = {}  # or deque, or running sum
    left = 0
    result = 0

    for right in range(len(arr)):
        # Expand window
        # Update window state

        while window_invalid():
            # Contract window
            # Update window state
            left += 1

        result = max(result, right - left + 1)  # or other metric

    return result
```

### Pattern 2: Heap / Priority Queue

**Why it matters:** Order book management, top-k queries, event scheduling

**Key operations:**
- Insert: O(log n)
- Extract min/max: O(log n)
- Peek: O(1)

**Common variations:**
- Two heaps for median
- Lazy deletion for dynamic data
- Custom comparators for multi-criteria sorting

### Pattern 3: Binary Search Variants

**Why it matters:** Price lookups, range queries, optimizing continuous functions

**Key insight:** Binary search works on any monotonic function, not just sorted arrays.

**Variants:**
- Lower bound / upper bound
- Search on answer space
- Ternary search for unimodal functions

### Pattern 4: Graph Algorithms

**Why it matters:** Dependency resolution, arbitrage detection, network analysis

**Essential algorithms:**
- BFS/DFS for traversal
- Dijkstra/Bellman-Ford for shortest paths
- Topological sort for DAGs
- Union-Find for dynamic connectivity

### Pattern 5: Dynamic Programming

**Why it matters:** Option pricing, portfolio optimization, sequence analysis

**State design principles:**
1. What decision am I making at each step?
2. What information do I need from previous steps?
3. What is the recurrence relation?

**Common patterns:**
- Linear DP: O(n) states
- Interval DP: O(n²) states over ranges
- State compression: O(2^k × n) for small k
- Probability DP: expected values over random processes

### Pattern 6: Advanced Data Structures

**Segment Tree / Fenwick Tree:**
- Range queries with updates
- Time: O(log n) per operation

**Union-Find:**
- Dynamic connectivity
- Near O(1) amortized with path compression

**Trie:**
- Prefix matching
- Autocomplete systems

---

## Interview Expectations at Quant Firms

### What Interviewers Look For

1. **Clean code** - readable, well-structured, no bugs
2. **Verbal clarity** - explain as you code
3. **Testing mindset** - propose test cases proactively
4. **Optimization awareness** - know when O(n) is good enough vs needs improvement
5. **System context** - how would this scale? What are bottlenecks?

### Communication During Interviews

**Starting the problem:**
```
"Let me make sure I understand the problem correctly. We have [input],
and we need to find [output]. Are there any constraints on [X]?"
```

**Thinking out loud:**
```
"My first thought is [approach]. This would be O(n²) because...
Let me see if we can do better by using [data structure/technique]."
```

**Handling stuck moments:**
```
"I'm not immediately seeing the optimal approach. Let me work through
a small example: [trace through]. Ah, I notice that [pattern]..."
```

**After coding:**
```
"Let me trace through with the example: [step by step].
Edge cases to consider: [list]. Let me verify [specific case]."
```

### Red Flags to Avoid

- Jumping to code without understanding the problem
- Silent coding for extended periods
- Ignoring edge cases
- Dismissing simpler solutions without analysis
- Over-engineering (premature optimization)
- Not testing your code

---

## Example Interview Reasoning

### Problem: Find the maximum profit from at most k stock transactions

**Initial analysis:**
> "This is a DP problem. The state needs to track: current day, number of transactions used, and whether we're holding stock. Let me define `dp[i][j][0/1]` as max profit on day i with j transactions and holding status."

**Optimization discussion:**
> "The naive state space is O(n × k × 2). For large k approaching n/2, we can optimize to unlimited transactions case. We can also reduce space to O(k) by noting we only need the previous day's states."

**Edge cases:**
> "If k = 0, answer is 0. If prices array is empty or length 1, answer is 0. If prices are strictly decreasing, answer is 0. Need to handle k >= n/2 as unlimited case to avoid TLE."

### Problem: Detect arbitrage in currency exchange

**Modeling:**
> "This is a graph problem. Each currency is a node, each exchange rate is an edge weight. Arbitrage exists if we can find a cycle with product of rates > 1."

**Algorithm choice:**
> "Taking log of rates converts multiplication to addition. Then we negate to convert 'product > 1' to 'sum of negatives < 0'. Now it's finding a negative cycle - Bellman-Ford!"

**Complexity:**
> "O(V × E) for Bellman-Ford, where V is number of currencies and E is number of exchange pairs. For 100 currencies with all pairs, about 10⁶ operations - very fast."

---

## Time Management Tips

1. **First 2-3 minutes:** Understand problem, ask clarifying questions
2. **Next 3-5 minutes:** Discuss approaches, settle on one
3. **Main coding:** 15-20 minutes with explanation
4. **Testing:** 5 minutes for examples and edge cases
5. **Follow-ups:** Be ready for "what if" variations

---

## Topics to Review Before Interviews

### Must-Know (expected to solve quickly)

- [ ] Two pointers / sliding window
- [ ] Hash table patterns
- [ ] Binary search variations
- [ ] BFS/DFS
- [ ] Basic DP (1D, 2D)
- [ ] Heap operations
- [ ] Stack problems (monotonic stack, parentheses)

### Should-Know (medium frequency)

- [ ] Union-Find with rank/compression
- [ ] Topological sort
- [ ] Dijkstra's algorithm
- [ ] Interval DP
- [ ] State compression DP
- [ ] Segment tree basics

### Good-to-Know (occasional, shows depth)

- [ ] Network flow
- [ ] Strongly connected components
- [ ] Advanced tree DP
- [ ] Fenwick tree
- [ ] String algorithms (KMP, rolling hash)
- [ ] Probability/expected value DP

---

## Final Advice

1. **Practice under time pressure** - use a timer during mock sessions
2. **Explain to a rubber duck** - verbalize your thought process
3. **Study solutions, not just problems** - understand multiple approaches
4. **Build intuition for complexity** - instant O(n) vs O(n log n) recognition
5. **Sleep well before interviews** - cognitive performance matters

Good luck with your quant interviews!
