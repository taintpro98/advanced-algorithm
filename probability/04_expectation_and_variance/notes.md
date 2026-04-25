# Expectation & Variance

## Core Concepts

- **Expected value**: E[X] = Σ x · P(X=x) (discrete) or ∫ x · f(x) dx (continuous)
- **Linearity of expectation**: E[X + Y] = E[X] + E[Y] (always, even if dependent)
- **Variance**: Var(X) = E[X²] - (E[X])²
- **Standard deviation**: σ = √Var(X)
- **Covariance**: Cov(X,Y) = E[XY] - E[X]·E[Y]

## Key Properties

- E[aX + b] = a·E[X] + b
- Var(aX + b) = a²·Var(X)
- If X,Y independent: Var(X+Y) = Var(X) + Var(Y)

## Powerful Technique: Indicator Variables

E[X] where X counts events = Σ P(event i occurs)
Example: expected number of fixed points in random permutation = 1

## Classic Problems

- Expected number of coin flips to get k heads
- Coupon collector problem: E[flips to collect all n coupons] = n · Hₙ ≈ n·ln(n)
- Expected number of inversions in random permutation

## Interview Questions

<!-- Add questions as you encounter them -->
