# Advanced Algorithm Learning Repository

A comprehensive, pattern-driven repository for mastering algorithms and data structures using Python, organized for technical interviews (mid to senior level), competitive programming, and algorithmic research.

## Repository Structure

This repository is organized into three main sections:

### `patterns/` - Systematic Learning by Topic
Contains **7 main learning pillars**, each with carefully selected subtopics and representative LeetCode problems. This is your source of truth for understanding algorithmic patterns and building foundational knowledge. Each subtopic includes:
- `notes.md` - Theoretical overview, patterns, and recognition strategies
- 3 Python problem files - Each containing problem metadata (NO solutions)

### `practice/` - Problem Playlists & Interview Prep
Organized collections for focused interview preparation and systematic practice:
- `top_interview_150/` - LeetCode's Top Interview 150 curated problems
- `leetcode_75/` - Essential LeetCode 75 study plan
- `company_tags/` - Problems organized by company tags
- `free_style/` - Daily challenges, contests, and random practice

### `cheatsheets/` - Quick Reference Materials
Templates, algorithms, and quick reference guides for common patterns and techniques

## Learning Pillars

### 01. Core Data Structures & Invariants
Master fundamental techniques that form the foundation of algorithmic problem-solving.

- **Prefix Sum** - Cumulative array transformations for range queries
- **Two Pointers** - Efficient pair/subsequence finding with O(n) traversal
- **Sliding Window** - Dynamic window optimization for substring/subarray problems
- **Binary Search** - Logarithmic search in sorted spaces and answer optimization
- **Hash Table Invariants** - O(1) lookups for state tracking and complement finding

### 02. Stack / Queue & Monotonic Structures
Advanced stack and queue patterns for ordering and range problems.

- **Monotonic Stack** - Next greater/smaller element and histogram problems
- **Monotonic Queue** - Sliding window max/min with deque optimization
- **Expression Evaluation** - Calculator and parser implementation
- **Parentheses Matching** - Bracket validation and optimization

### 03. Heap & Greedy Algorithms
Priority-based selection and optimal choice strategies.

- **K Elements** - Top K and median finding with heap optimization
- **Interval Scheduling** - Meeting rooms and interval merging
- **Greedy Exchange Argument** - Provably optimal greedy strategies

### 04. Dynamic Programming (Pro Level)
Advanced DP patterns for competitive programming and senior interviews.

- **Interval DP** - Range-based optimization (burst balloons, palindromes)
- **Knapsack Variants** - Subset sum, coin change, and resource allocation
- **Digit DP** - Counting numbers with digit constraints
- **State Compression DP** - Bitmask DP for NP-hard problems (n ≤ 20)
- **Tree DP** - Subtree optimization and path problems
- **Probability DP** - Expected value and stochastic process computation

### 05. Graph Algorithms
Classical and advanced graph theory for network problems.

- **Shortest Path** - Dijkstra, Bellman-Ford, Floyd-Warshall
- **Minimum Spanning Tree** - Kruskal and Prim algorithms
- **Topological Sort** - Dependency resolution and cycle detection
- **Strongly Connected Components** - Tarjan and Kosaraju algorithms
- **Bipartite Matching** - Two-coloring and maximum matching
- **Network Flow** - Max-flow min-cut and flow-based optimization

### 06. Number Theory & Modular Arithmetic
Mathematical foundations for combinatorics and large number computation.

- **Prime Factorization** - Sieve, GCD/LCM, and divisor problems
- **Modular Arithmetic** - Fast exponentiation, modular inverse, CRT
- **Combinatorics** - Binomial coefficients, permutations, and counting

### 07. Advanced / Research-Oriented Topics
Specialized data structures for competitive programming and research.

- **Segment Tree** - Range queries with lazy propagation
- **Fenwick Tree (BIT)** - Efficient prefix sums and inversion counting
- **Trie** - Prefix matching and XOR optimization
- **Union-Find** - Disjoint set operations with path compression
- **Rolling Hash** - Rabin-Karp and efficient string matching

## How to Use This Repository

### For Pattern Learning (`patterns/`)
1. **Pattern Recognition Training**
   - Read `notes.md` in each subtopic to understand the pattern
   - Learn to recognize when a pattern applies to a problem
   - Focus on "How to Recognize This Type of Problem" sections

2. **Problem Solving Workflow**
   - Attempt each problem independently without looking at solutions
   - Use the pattern hints only after attempting the problem
   - Implement solutions from scratch to build muscle memory

3. **Progressive Difficulty**
   - Start with Core Data Structures (Pillar 01)
   - Build up to Advanced Topics (Pillar 07)
   - Revisit earlier patterns as you encounter them in harder problems

### For Interview Prep (`practice/`)
- Use `top_interview_150/` or `leetcode_75/` for structured interview preparation
- Track progress using the notes.md templates in each playlist
- Organize company-specific prep in `company_tags/`
- Use `free_style/` for daily challenges and contest practice

### For Quick Reference (`cheatsheets/`)
- Consult templates and patterns during problem-solving
- Review algorithm implementations and time complexities

## Repository Statistics

- **7 Learning Pillars**
- **28 Subtopics**
- **84 Curated LeetCode Problems**
- **Pattern-Driven Organization**
- **Zero Solutions (Learning-Focused)**

## Design Principles

This repository is built on the following principles:

- **Pattern Over Memorization** - Understand recurring patterns, not individual solutions
- **No Solutions Provided** - Forces active learning and prevents passive consumption
- **Conceptual Clarity** - Theory and recognition strategies in every `notes.md`
- **Scalable Structure** - Easily extend with more problems while maintaining organization
- **Pro-Level Focus** - Targets mid to senior engineers and competitive programmers

## Learning Philosophy

The absence of solutions is intentional. This repository trains you to:

- Recognize patterns independently
- Build solutions from first principles
- Develop algorithmic intuition
- Strengthen problem-solving muscles

## Contributing

This repository is designed to grow. When adding problems:

- Maintain the 3-problem limit per subtopic for focus
- Ensure problems are pattern-defining and interview-relevant
- Update `notes.md` if new pattern variants emerge
- Follow naming convention: `lc_<id>_<snake_case_name>.py`

## Next Steps

**For Pattern Learning:**
1. Start with `patterns/01_core_ds/01_prefix_sum/notes.md`
2. Attempt the three problems in that folder
3. Move systematically through subtopics
4. Track your progress and revisit challenging patterns

**For Interview Prep:**
1. Choose a playlist in `practice/` (Top Interview 150 or LeetCode 75)
2. Use the notes.md template to track your progress
3. Reference relevant patterns from `patterns/` as you solve problems
4. Maintain a review schedule for challenging problems

---

**Go pro in algorithms. Master patterns. Build intuition.**
