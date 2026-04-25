# Brainteasers & Quant Puzzles

## How to Approach

1. **Restate** the problem in your own words
2. **Identify** the probability space and what's being asked
3. **Look for symmetry** — often simplifies dramatically
4. **Use indicator variables** for counting expectations
5. **Sanity check** answer with extreme cases (n=1, p=0, p=1)

## Problem Template

**Problem:**
(statement)

**Key insight:**
(the non-obvious observation that cracks it)

**Solution:**
(reasoning)

**Answer:**
(final result)

---

## Problems

<!-- Add problems as you encounter them, using the template above -->

### Example: Flipping until two heads in a row

**Problem:** Flip a fair coin until you get HH. What is the expected number of flips?

**Key insight:** Set up a recurrence based on states (start, got one H, done).

**Solution:**
Let E = expected flips from start, E₁ = expected flips after one H.
- E = 1 + (1/2)·E₁ + (1/2)·E        → after T, back to start
- E₁ = 1 + (1/2)·0 + (1/2)·E        → after H done; after T back to start
Solving: E₁ = 1 + E/2, E = 1 + E₁/2 + E/2 → E = 6

**Answer:** 6 flips
