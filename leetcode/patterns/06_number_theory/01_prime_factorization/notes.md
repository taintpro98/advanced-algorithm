# Prime Factorization

## What This Subtopic Is About

Prime factorization decomposes numbers into prime factors, enabling efficient computation of GCD, LCM, divisor counts, and multiplicative properties. This pattern uses sieve algorithms, factorization techniques, and number-theoretic functions.

## Typical Patterns & Invariants

- **Sieve of Eratosthenes**: Precompute all primes up to n in O(n log log n)
- **Trial division**: Check divisibility by primes up to √n
- **Pollard's rho**: Advanced factorization for large numbers
- **GCD/LCM**: Euclidean algorithm, relationship via prime factorization
- **Divisor counting**: Multiply (exponent + 1) for each prime factor

## How to Recognize This Type of Problem

- Problems involving prime numbers or factorization
- GCD, LCM, or coprimality checks
- Counting divisors or finding nth divisor
- Modular arithmetic with prime modulus
- Problems reducible to prime properties

## LeetCode Problems

- [204. Count Primes](https://leetcode.com/problems/count-primes/)
- [952. Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/)
- [1808. Maximize Number of Nice Divisors](https://leetcode.com/problems/maximize-number-of-nice-divisors/)
