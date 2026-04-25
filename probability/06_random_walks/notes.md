# Random Walks & Markov Chains

## Random Walk

- Simple 1D: at each step move +1 or -1 with probability p and 1-p
- **Gambler's ruin**: starting at x, absorbing barriers at 0 and N
  - P(reach N before 0) = x/N if p = 1/2
  - P(reach N before 0) = (1-(q/p)^x) / (1-(q/p)^N) if p ≠ 1/2

## Markov Chains

- **Markov property**: P(Xₙ₊₁ | X₀,...,Xₙ) = P(Xₙ₊₁ | Xₙ)
- **Transition matrix** T: Tᵢⱼ = P(go from state i to state j)
- **Stationary distribution** π: πT = π, Σπᵢ = 1
- **Hitting time** hᵢ: expected steps to reach state i from state j

## Key Results

- For symmetric random walk on integers: expected return time to origin = ∞ (recurrent but null)
- Hitting time equations: hᵢ = 1 + Σⱼ Tᵢⱼ · hⱼ (solve as linear system)

## Classic Problems

- Expected steps for random walk to reach N
- Card shuffling mixing time
- PageRank as stationary distribution

## Interview Questions

<!-- Add questions as you encounter them -->
