# Modular Arithmetic

## What This Subtopic Is About

Modular arithmetic handles computation under modulo operations, essential for large number calculations and combinatorics. This pattern includes modular exponentiation, inverse, Chinese Remainder Theorem, and Fermat's Little Theorem applications.

## Typical Patterns & Invariants

- **Modular exponentiation**: Fast power using binary exponentiation, O(log n)
- **Modular inverse**: a⁻¹ mod p using Fermat's Little Theorem (when p is prime)
- **Chinese Remainder Theorem**: Solve simultaneous modular equations
- **Addition/multiplication**: (a + b) mod m = ((a mod m) + (b mod m)) mod m
- **Division**: a/b mod m = a × b⁻¹ mod m
- **Binary search on answer using inclusion–exclusion with LCM**: For counting problems involving multiples

## How to Recognize This Type of Problem

- "Answer modulo 10⁹ + 7" or similar large modulus
- Computing large powers or factorials
- Combinatorial counting with large numbers
- Problems involving remainders or cyclic patterns
- Matrix exponentiation for recurrence relations

## LeetCode Problems

- [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [372. Super Pow](https://leetcode.com/problems/super-pow/)
- [878. Nth Magical Number](https://leetcode.com/problems/nth-magical-number/)
- [1916. Count Ways to Build Rooms in an Ant Colony](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/)
