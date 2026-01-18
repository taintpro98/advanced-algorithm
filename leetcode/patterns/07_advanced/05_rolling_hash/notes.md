# Rolling Hash (Rabin-Karp)

## What This Subtopic Is About

Rolling hash enables efficient string matching and comparison using polynomial hashing. This pattern computes hash values incrementally as a window slides, supporting O(1) hash updates and substring matching in linear time.

## Typical Patterns & Invariants

- **Polynomial hash**: hash(s) = (s[0] × p⁰ + s[1] × p¹ + ... + s[n-1] × p^(n-1)) mod m
- **Rolling property**: Update hash when sliding window by one character
- **Collision handling**: Use multiple hash functions or verify matches
- **Double hashing**: Combine two hash functions to reduce collision probability
- **Suffix hashing**: Precompute hashes for all suffixes

## How to Recognize This Type of Problem

- Substring matching or pattern search
- Finding duplicate substrings
- Longest common substring/subsequence
- String comparison in O(1) after preprocessing
- Problems requiring efficient substring hash

## LeetCode Problems

- [1044. Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)
- [1923. Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath/)
- [718. Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)
