# Probability Distributions

## Discrete Distributions

| Distribution | Params | PMF | E[X] | Var(X) | Use case |
|---|---|---|---|---|---|
| Bernoulli | p | p^x (1-p)^(1-x) | p | p(1-p) | single trial |
| Binomial | n,p | C(n,k)p^k(1-p)^(n-k) | np | np(1-p) | k successes in n trials |
| Geometric | p | (1-p)^(k-1)p | 1/p | (1-p)/p² | trials until first success |
| Poisson | λ | e^(-λ)λ^k/k! | λ | λ | rare events in interval |

## Continuous Distributions

| Distribution | Params | E[X] | Var(X) | Use case |
|---|---|---|---|---|
| Uniform | a,b | (a+b)/2 | (b-a)²/12 | equal likelihood |
| Exponential | λ | 1/λ | 1/λ² | time between Poisson events |
| Normal | μ,σ² | μ | σ² | central limit theorem |

## Key Relationships

- Binomial(n,p) → Poisson(λ=np) as n→∞, p→0
- Sum of exponentials → Gamma distribution
- Central Limit Theorem: sum of iid → Normal

## Interview Questions

<!-- Add questions as you encounter them -->
