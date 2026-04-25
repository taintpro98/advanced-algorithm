# Probability Problems and Brainteasers for Quant Interviews

This file contains classic probability puzzles and logic brainteasers commonly asked at quantitative trading firms.

---

## Table of Contents

1. [Probability Problems](#probability-problems)
2. [Expected Value Problems](#expected-value-problems)
3. [Logic Puzzles](#logic-puzzles)
4. [Market/Trading Puzzles](#markettrading-puzzles)
5. [Quick Mental Math](#quick-mental-math)

---

## Probability Problems

### Problem 1: The Birthday Problem

**Problem:**
In a room of n people, what is the probability that at least two people share a birthday? How many people are needed for this probability to exceed 50%?

**Reasoning:**
It's easier to calculate the complement: probability that NO two people share a birthday.

For n people:
- Person 1: any birthday (365/365)
- Person 2: different from person 1 (364/365)
- Person 3: different from both (363/365)
- ...and so on

**Final Answer:**
P(at least one shared birthday) = 1 - (365/365) × (364/365) × (363/365) × ... × ((366-n)/365)

For 50% threshold: **n = 23 people**

**Explanation:**
This is counterintuitive because we're not asking "who shares YOUR birthday" but "does ANY pair share a birthday." With 23 people, there are C(23,2) = 253 pairs, each with 1/365 chance of matching.

---

### Problem 2: Monty Hall Problem

**Problem:**
You're on a game show with 3 doors. Behind one door is a car; behind the others, goats. You pick door 1. The host, who knows what's behind each door, opens door 3 to reveal a goat. Should you switch to door 2?

**Reasoning:**
- Initial probability of car behind door 1: 1/3
- Initial probability of car behind doors 2 or 3: 2/3
- After host reveals door 3 is a goat, the 2/3 probability concentrates on door 2

**Final Answer:**
**Yes, switch.** Switching wins 2/3 of the time; staying wins 1/3.

**Explanation:**
The host's action is not random - he MUST open a door with a goat. This gives you information. If you initially picked wrong (2/3 chance), switching wins. If you initially picked right (1/3 chance), switching loses.

---

### Problem 3: Two Envelopes Problem

**Problem:**
Two envelopes contain money. One has twice as much as the other. You pick one and see $100. Should you switch?

**Reasoning:**
The naive argument says: "The other envelope has either $50 or $200 with equal probability, so expected value of switching is (50 + 200)/2 = $125 > $100."

But this reasoning is flawed! The two cases (other envelope = $50 vs $200) are NOT equally likely given that you see $100.

**Final Answer:**
**No advantage to switching** (in the standard formulation). The expected value is the same.

**Explanation:**
The paradox arises from improper conditioning. If the amounts are ($50, $100), probability of seeing $100 is 1/2. If amounts are ($100, $200), probability of seeing $100 is also 1/2. Given you see $100, both underlying distributions are equally likely, and switching has EV = $100.

---

### Problem 4: Dice Sum Problem

**Problem:**
You roll two fair dice. Given that the sum is greater than 7, what is the probability that at least one die shows a 6?

**Reasoning:**
Sum > 7 means sum ∈ {8, 9, 10, 11, 12}.

Count outcomes with sum > 7:
- Sum 8: (2,6), (3,5), (4,4), (5,3), (6,2) = 5 ways
- Sum 9: (3,6), (4,5), (5,4), (6,3) = 4 ways
- Sum 10: (4,6), (5,5), (6,4) = 3 ways
- Sum 11: (5,6), (6,5) = 2 ways
- Sum 12: (6,6) = 1 way

Total: 15 outcomes

Outcomes with sum > 7 AND at least one 6:
(2,6), (6,2), (3,6), (6,3), (4,6), (6,4), (5,6), (6,5), (6,6) = 9 outcomes

**Final Answer:**
P(at least one 6 | sum > 7) = **9/15 = 3/5 = 0.6**

---

### Problem 5: Coin Flip Sequences

**Problem:**
You flip a fair coin repeatedly. On average, how many flips until you see HH (two heads in a row)?

**Reasoning:**
Let E[HH] = expected flips to see HH.

Define states:
- Start: no progress
- H: just saw one H
- HH: done

From Start: flip coin
- H (prob 1/2): move to state H
- T (prob 1/2): stay at Start

From H: flip coin
- H (prob 1/2): done (HH achieved)
- T (prob 1/2): back to Start

Let E[S] = expected flips from Start, E[H] = expected flips from state H.

E[S] = 1 + (1/2)E[H] + (1/2)E[S]
E[H] = 1 + (1/2)(0) + (1/2)E[S]

Solving: E[H] = 1 + (1/2)E[S]
Substituting: E[S] = 1 + (1/2)(1 + (1/2)E[S]) + (1/2)E[S]
E[S] = 1 + 1/2 + (1/4)E[S] + (1/2)E[S]
E[S] = 3/2 + (3/4)E[S]
(1/4)E[S] = 3/2
E[S] = 6

**Final Answer:**
**6 flips** on average to see HH

**Explanation:**
Compare: expected flips for HT is only 4. HH requires "momentum" that can be broken, while HT progress is never wasted (T after H still gets you the T you need).

---

### Problem 6: Stick Breaking

**Problem:**
A stick of length 1 is broken at two random points. What is the probability the three pieces can form a triangle?

**Reasoning:**
Let the break points be at positions X and Y where X < Y. The pieces have lengths X, Y-X, and 1-Y.

Triangle inequality requires ALL of:
- X + (Y-X) > 1-Y → Y > 1/2
- X + (1-Y) > Y-X → X + 1 - Y > Y - X → 2X + 1 > 2Y → X > Y - 1/2
- (Y-X) + (1-Y) > X → 1 - X > X → X < 1/2

Conditions: X < 1/2, Y > 1/2, and X > Y - 1/2

**Final Answer:**
**P = 1/4**

**Explanation:**
The valid region in the unit square (X, Y) where X < Y forms a triangle with area 1/4 of the total region.

---

## Expected Value Problems

### Problem 7: Dice Game - Stop or Continue

**Problem:**
You roll a die. You can either take the value shown as your payout, or pay $1 to roll again (and repeat). What's your optimal strategy and expected value?

**Reasoning:**
Let E = expected value under optimal strategy.

If you roll k, you should continue if E - 1 > k, i.e., if k < E - 1.

E = (1/6) × [max(1, E-1) + max(2, E-1) + max(3, E-1) + max(4, E-1) + max(5, E-1) + max(6, E-1)]

Guess E ≈ 4.5:
- Continue if k < 3.5, so continue on 1, 2, 3; stop on 4, 5, 6
- E = (1/6)[3(E-1) + 4 + 5 + 6] = (1/6)[3E - 3 + 15] = (1/6)(3E + 12) = E/2 + 2
- E/2 = 2 → E = 4

Check with E = 4:
- Continue if k < 3, so continue on 1, 2; stop on 3, 4, 5, 6
- E = (1/6)[2(4-1) + 3 + 4 + 5 + 6] = (1/6)[6 + 18] = 4 ✓

**Final Answer:**
**Strategy:** Roll again if you get 1 or 2; stop on 3, 4, 5, or 6.
**Expected value:** $4

---

### Problem 8: Collecting Coupons

**Problem:**
A cereal box contains one of n different coupons (each equally likely). How many boxes must you buy on average to collect all n coupons?

**Reasoning:**
Divide into phases. Phase i: you have i-1 coupons and need to get a new one.

In phase i, probability of new coupon = (n - i + 1)/n

Expected boxes in phase i = n/(n - i + 1) (geometric distribution)

Total expected boxes = Σ(i=1 to n) n/(n - i + 1) = n × Σ(j=1 to n) 1/j = n × H_n

**Final Answer:**
**E[boxes] = n × H_n ≈ n × (ln(n) + 0.577)**

where H_n is the n-th harmonic number.

**Explanation:**
For n = 10: E ≈ 10 × 2.93 ≈ 29 boxes
For n = 100: E ≈ 100 × 5.19 ≈ 519 boxes

---

### Problem 9: Random Walk Hitting Time

**Problem:**
A drunk starts at position 0 and takes random steps: +1 with probability 1/2, -1 with probability 1/2. What is the expected number of steps to reach position +1?

**Reasoning:**
Let E_k = expected steps to reach +1 starting from position k (for k ≤ 0).

E_0 = 1 + (1/2)E_1 + (1/2)E_{-1}
E_1 = 0 (already at target)
E_{-1} = 1 + (1/2)E_0 + (1/2)E_{-2}

By symmetry, E_{-k} = E_0 + 2k for k > 0 (need to get back to 0, then reach 1).

From E_0 = 1 + (1/2)(0) + (1/2)E_{-1}:
E_0 = 1 + (1/2)E_{-1} = 1 + (1/2)(E_0 + 2)
E_0 = 1 + E_0/2 + 1
E_0/2 = 2
E_0 = ???

Actually, this recurrence doesn't converge nicely. The answer is **infinite**!

**Final Answer:**
**E = ∞ (infinite)**

**Explanation:**
A 1D random walk is recurrent (will return to any position infinitely often) but the expected hitting time for any specific position is infinite. The drunk will eventually reach +1 with probability 1, but the expected time is unbounded.

---

### Problem 10: Geometric Distribution Memorylessness

**Problem:**
You flip a biased coin with P(heads) = p until you get heads. Given that you didn't get heads in the first 10 flips, what's the expected additional flips needed?

**Reasoning:**
The geometric distribution is memoryless. Knowing that the first k flips were tails doesn't change the expected number of remaining flips.

**Final Answer:**
**E[additional flips] = 1/p** (same as starting fresh)

**Explanation:**
P(X > 10 + k | X > 10) = P(X > k). The past failures provide no information about future success probability.

---

## Logic Puzzles

### Problem 11: 100 Prisoners and Light Bulb

**Problem:**
100 prisoners, a room with a light bulb (initially off). Each day, one random prisoner visits the room and can toggle the light. At any time, a prisoner can claim "all 100 prisoners have visited." If correct, all go free; if wrong, all die. Design a strategy.

**Reasoning:**
Designate one "counter" prisoner. Rules:
- If you're not the counter and find the light OFF, and you've never turned it ON before, turn it ON.
- If you're not the counter and find the light ON (or you've turned it on before), do nothing.
- If you're the counter and find the light ON, turn it OFF and increment your count.
- When counter reaches 99, claim success.

**Final Answer:**
Counter counts to 99 (each other prisoner turns on the light exactly once, counter counts by turning it off). Takes ~27 years on average.

**Explanation:**
Each non-counter prisoner contributes exactly one "signal" by turning the light on for the first time. The counter aggregates these signals.

---

### Problem 12: Blue Eyes Island

**Problem:**
On an island, 100 people have blue eyes and know everyone else's eye color but not their own. A visitor announces "At least one person has blue eyes." Anyone who can deduce their own eye color must leave that midnight. What happens?

**Reasoning:**
This is about common knowledge.

- If 1 blue-eyed person: sees 0 blue eyes, knows they must be the one, leaves night 1.
- If 2 blue-eyed people: each sees 1 blue, expects that person to leave night 1 if they're the only one. When they don't, both deduce they also have blue eyes, leave night 2.
- Induction: with k blue-eyed people, all leave on night k.

**Final Answer:**
**All 100 blue-eyed people leave on night 100.**

**Explanation:**
The visitor's statement creates common knowledge that "everyone knows everyone knows... at least one blue" to arbitrary depth. This wasn't true before (even though everyone could SEE blue-eyed people).

---

### Problem 13: Pirate Game

**Problem:**
5 pirates (A, B, C, D, E in decreasing seniority) divide 100 gold coins. A proposes, and majority vote decides (proposer's vote counts). If rejected, A is thrown overboard, and B proposes. Pirates are rational, greedy, and prefer others die when indifferent. What does A propose?

**Reasoning:**
Work backwards:

**2 pirates (D, E):** D proposes 100-0, votes yes (majority of 1), wins.

**3 pirates (C, D, E):** E knows if C dies, D gets everything. So E accepts any offer > 0. C proposes 99-0-1, E votes yes, passes.

**4 pirates (B, C, D, E):** D knows if B dies, he gets 0. So D accepts any offer > 0. B proposes 99-0-1-0, D votes yes, passes.

**5 pirates (A, B, C, D, E):** C and E get 0 if A dies. They accept any offer > 0. A proposes 98-0-1-0-1, C and E vote yes, passes.

**Final Answer:**
**A proposes (98, 0, 1, 0, 1)** - giving 1 coin each to C and E.

---

### Problem 14: Weighing Problem

**Problem:**
You have 12 balls, one is defective (either heavier or lighter). Using a balance scale exactly 3 times, find the defective ball AND whether it's heavier or lighter.

**Reasoning:**
Each weighing has 3 outcomes: left heavy, balanced, right heavy.
3 weighings → 3³ = 27 possible outcome sequences.
We need to distinguish 12 × 2 = 24 cases (12 balls × heavier or lighter).

**Strategy:**
1. Weigh 4 vs 4, keeping 4 aside.
2. Based on result, narrow down suspects.
3. Final weighing identifies the ball and its nature.

**Final Answer:**
See detailed solution in interview prep books. Key insight: 27 > 24, so information-theoretically possible. The solution involves careful tracking of "could be heavy" vs "could be light" for each ball.

---

### Problem 15: Burning Ropes

**Problem:**
You have two ropes that each take exactly 1 hour to burn, but burn at non-uniform rates. How do you measure exactly 45 minutes?

**Reasoning:**
- Light rope 1 from both ends AND rope 2 from one end simultaneously.
- Rope 1 burns out in 30 minutes (both ends meeting).
- At that moment, light rope 2's other end.
- Rope 2 has 30 minutes of burn time left, but now burns from both ends, so takes 15 more minutes.
- Total: 30 + 15 = 45 minutes.

**Final Answer:**
Light rope 1 from both ends and rope 2 from one end. When rope 1 is done (30 min), light rope 2's other end. When rope 2 is done, 45 minutes have passed.

---

## Market/Trading Puzzles

### Problem 16: Market Making

**Problem:**
I'm thinking of a number between 1 and 100. You must quote a bid and ask (buy and sell price). I'll either sell to your bid or buy at your ask. How do you set your prices?

**Reasoning:**
If my number is X and you quote bid B and ask A:
- If X < B, I sell to you at B (you lose B - X)
- If X > A, I buy from you at A (you lose X - A)
- If B ≤ X ≤ A, I do nothing

Expected loss = (1/100) × [Σ(X=1 to B-1)(B-X) + Σ(X=A+1 to 100)(X-A)]

To minimize loss, balance the two tails. Optimal: bid around 25-26, ask around 75-76 (spread of ~50).

**Final Answer:**
Quote bid ~26 and ask ~75 (or similar symmetric spread around 50). Your expected loss is about 12-13.

**Explanation:**
This illustrates market making under adverse selection. The wider the spread, the safer but fewer trades. The tighter the spread, more trades but more risk.

---

### Problem 17: Arbitrage Detection

**Problem:**
USD/EUR = 0.9, EUR/GBP = 0.85, GBP/USD = 1.25. Is there an arbitrage opportunity?

**Reasoning:**
Start with 1 USD:
- Convert to EUR: 1 × 0.9 = 0.9 EUR
- Convert to GBP: 0.9 × 0.85 = 0.765 GBP
- Convert back to USD: 0.765 × 1.25 = 0.956 USD

Product of rates: 0.9 × 0.85 × 1.25 = 0.956

**Final Answer:**
**No arbitrage in USD→EUR→GBP→USD direction** (you lose money).
**Check reverse:** USD→GBP→EUR→USD: (1/1.25) × (1/0.85) × (1/0.9) = 1.046
**Yes, arbitrage exists** in the reverse direction: ~4.6% profit.

---

### Problem 18: Option Pricing Intuition

**Problem:**
A stock is at $100. In one period it goes to either $110 or $90 with equal probability. Risk-free rate is 0. What's the fair price of a call option with strike $100?

**Reasoning:**
Payoffs: Call pays max(S - 100, 0) = $10 if stock goes up, $0 if down.

**Risk-neutral pricing:** Find probability p such that expected stock return = risk-free rate.
p × 110 + (1-p) × 90 = 100 × (1 + 0) = 100
110p + 90 - 90p = 100
20p = 10
p = 0.5 (happens to equal real probability here)

Option price = p × 10 + (1-p) × 0 = 0.5 × 10 = $5

**Final Answer:**
**Fair price = $5**

**Explanation:**
Note: real probability doesn't matter for pricing! Only risk-neutral probability (determined by no-arbitrage) matters. This is the foundation of Black-Scholes.

---

## Quick Mental Math

### Problem 19: Estimation

**Problem:**
Estimate 2^10, 2^20, and e^3 quickly.

**Final Answer:**
- 2^10 = 1,024 ≈ **1,000**
- 2^20 = (2^10)² ≈ **1,000,000** (exactly 1,048,576)
- e^3 ≈ 2.718³ ≈ **20** (exactly 20.09)

Useful: e ≈ 2.718, e² ≈ 7.39, e³ ≈ 20.1

---

### Problem 20: Probability Sanity Checks

**Problem:**
Without calculating, estimate: if you flip 100 fair coins, what's the probability of getting exactly 50 heads?

**Final Answer:**
Approximately **8%** (exact: 7.96%)

**Reasoning:**
By CLT, distribution is approximately N(50, 25). The standard deviation is 5. P(X = 50) for discrete ≈ 1/(σ√(2π)) = 1/(5 × 2.5) = 1/12.5 ≈ 0.08.

---

## Additional Practice Problems

1. **Expected value of max(X, Y)** where X, Y are independent uniform on [0,1]. Answer: 2/3

2. **Probability that a random chord is longer than the radius** of the circle. Answer: Depends on how "random" is defined (Bertrand paradox)!

3. **Secretary problem:** Interview n candidates sequentially, must decide immediately. Optimal strategy? Reject first n/e candidates, then pick next one better than all previous. Success probability → 1/e ≈ 37%.

4. **Gambler's ruin:** Start with $k, win/lose $1 with prob 1/2 each. Probability of reaching $n before going broke? Answer: k/n

5. **St. Petersburg paradox:** Flip until heads, win 2^n dollars. What's fair price? E[X] = ∞, but no one pays infinite amount. (Utility theory resolution)

---

## Tips for Probability Interviews

1. **Always define your random variables clearly**
2. **Check edge cases:** n=0, n=1, probability = 0 or 1
3. **Use complementary counting** when "at least one" is involved
4. **Draw pictures** for geometric probability
5. **Sanity check** your answers (probabilities in [0,1], expectations reasonable)
6. **Know your distributions:** Binomial, Geometric, Poisson, Exponential, Normal
7. **State assumptions** (independence, identical distribution, etc.)

Good luck!
