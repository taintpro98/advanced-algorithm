# Trie (Prefix Tree)

## What This Subtopic Is About

Trie is a tree structure for storing strings, enabling efficient prefix matching, autocomplete, and dictionary operations. This pattern extends to bit tries for XOR problems and suffix trees for advanced string matching.

## Typical Patterns & Invariants

- **Node structure**: Each node represents a character, children map to next characters
- **Prefix search**: Check if prefix exists in O(m) where m is prefix length
- **Word insertion/deletion**: Add/remove words in O(m) time
- **Bit trie**: Store binary representations for XOR maximization
- **Suffix tree/array**: Advanced pattern matching and substring queries

## How to Recognize This Type of Problem

- Autocomplete or prefix matching
- Dictionary operations (add, search, startsWith)
- Finding words with common prefix
- XOR maximization problems (bit trie)
- String matching and pattern search

## LeetCode Problems

- [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
- [1707. Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)
