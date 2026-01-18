# Probability Dynamic Programming

## What This Subtopic Is About

Probability DP computes expected values, probabilities, or game-theoretic optimal strategies using dynamic programming. This pattern handles stochastic processes by summing over all possible outcomes weighted by their probabilities.

## Typical Patterns & Invariants

- **Expected value**: E[state] = Σ P(outcome) × value(outcome)
- **Probability computation**: P[state] = Σ P(transition) × P[next_state]
- **Game theory**: Minimax with probabilities for optimal play
- **Markov chains**: Transition probabilities between states
- **Convergence**: Iterative refinement until probabilities stabilize

## How to Recognize This Type of Problem

- Computing probabilities or expected values
- Dice, cards, or random events
- "What is the probability that..."
- "Expected number of steps/moves/..."
- Game-theoretic scenarios with randomness

## LeetCode Problems

- [837. New 21 Game](https://leetcode.com/problems/new-21-game/)
- [808. Soup Servings](https://leetcode.com/problems/soup-servings/)
- [688. Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/)
