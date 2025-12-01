# Mathematical & Statistical Concepts

This document explains the core probability and statistics concepts demonstrated by each paradox in the app.

## 1. Monty Hall Problem

### The Paradox
When given the choice to switch doors after Monty reveals a goat, intuition suggests a 50/50 chance. However, switching actually gives you a **2/3 probability** of winning.

### Mathematical Concepts

**Conditional Probability**
- The probability of an event given that another event has occurred
- Formula: P(A|B) = P(A ∩ B) / P(B)

**Bayes' Theorem**
- Updates probabilities based on new information
- Monty's action provides information that changes the probability distribution

**Key Insight:**
- Initial choice: 1/3 chance of car, 2/3 chance of goat
- Monty's constraint: Must reveal a goat, cannot reveal the car
- When you picked a goat (2/3 probability), Monty has only ONE door he can open
- Switching transfers the 2/3 probability to the remaining door

### Why Intuition Fails
Our brains see "two doors remaining" and assume equal probability, ignoring:
1. The prior probability (your initial 1/3 chance)
2. The constraint on Monty's choice (he can't reveal the car)
3. The information gained from Monty's action

---

## 2. Birthday Paradox

### The Paradox
Only **23 people** are needed for a >50% chance that two share a birthday. Most people guess 180+.

### Mathematical Concepts

**Combinatorics**
- Number of possible pairs in a group of n people: n(n-1)/2
- With 23 people: 23 × 22 / 2 = **253 pairs**

**Complement Probability**
- P(at least one match) = 1 - P(no matches)
- Easier to calculate the probability that NO one shares a birthday

**The Formula:**
```
P(no match) = (365/365) × (364/365) × (363/365) × ... × (365-n+1)/365
P(match) = 1 - P(no match)
```

For n=23:
```
P(no match) ≈ 0.493
P(match) ≈ 0.507 (50.7%)
```

### Why Intuition Fails
We think linearly: "23 out of 365 days is tiny!"

But we should think in **pairs**:
- 23 people = 253 possible pairs
- Each pair is a chance for a match
- Probability compounds rapidly

---

## 3. Two Envelopes Paradox

### The Paradox
You have two envelopes: one contains X, the other 2X. After picking one with $100, the expected value calculation suggests you should always switch. But this leads to infinite switching!

### Mathematical Concepts

**Expected Value**
- E(X) = Σ [x × P(x)]
- The average outcome if you repeat the experiment many times

**The Faulty Reasoning:**
```
E(other envelope) = 0.5 × ($50) + 0.5 × ($200) = $125
Since $125 > $100, switch!
```

**The Problem:**
This assumes a **uniform prior** over all possible values of X, which is impossible (infinite money doesn't exist).

**Correct Analysis:**
- There's a specific probability distribution for the envelope amounts
- Once you observe $100, you gain information about this distribution
- You cannot assume P(X=50) = P(X=100) = 0.5 without knowing the prior

### Why Intuition Fails
The reasoning *looks* mathematically sound but makes an impossible assumption about the probability distribution.

---

## 4. Sleeping Beauty Problem

### The Paradox
After being awakened, should Sleeping Beauty believe the coin was Heads with probability 1/2 or 1/3?

### Mathematical Concepts

**Self-Locating Belief**
- Probability when you don't know your position in time/space
- Different from objective probability

**Two Positions:**

**Halfers (1/2):**
- The coin is fair
- No new information about the coin toss is gained by waking up
- P(Heads) = 1/2

**Thirders (1/3):**
- Consider the frequency over many experiments
- Heads → 1 awakening
- Tails → 2 awakenings
- If you're awakened, you're twice as likely to be in a Tails-world
- P(Heads | Awakened) = 1/3

**Frequency Analysis:**
```
100 experiments:
- 50 Heads → 50 awakenings
- 50 Tails → 100 awakenings
- Total: 150 awakenings
- P(Heads | Awakening) = 50/150 = 1/3
```

### Why It's Debated
This touches on deep questions in probability theory:
- Subjective vs. objective probability
- How to update beliefs with self-locating uncertainty
- The role of indexical information

---

## 5. Simpson's Paradox

### The Paradox
A trend appears in separate groups but reverses when the groups are combined.

### Mathematical Concepts

**Confounding Variables**
- A variable that influences both the independent and dependent variables
- Creates spurious associations

**Weighted Averages**
- Overall rate ≠ simple average of group rates
- Depends on the size of each group

**Example:**
```
Department A (Easy):
- Male: 80/100 = 80%
- Female: 18/20 = 90%
- Female > Male ✓

Department B (Hard):
- Male: 10/20 = 50%
- Female: 60/100 = 60%
- Female > Male ✓

Overall:
- Male: 90/120 = 75%
- Female: 78/120 = 65%
- Male > Female ✗ (PARADOX!)
```

**Why This Happens:**
- Men applied mostly to the easy department (100 vs 20)
- Women applied mostly to the hard department (100 vs 20)
- The weighted average is pulled by where most applications went

### Why Intuition Fails
We expect aggregated data to preserve trends from subgroups, but:
- Different group sizes create different weights
- Hidden variables (department difficulty) matter
- Aggregation can hide or reverse trends

---

## Key Takeaways

### Common Themes

1. **Conditional Probability is Tricky**
   - New information changes probabilities in non-obvious ways
   - Prior probabilities matter

2. **Combinatorics Grows Fast**
   - Small numbers of items create surprisingly many combinations
   - Pairs, triplets, etc. grow quadratically or faster

3. **Assumptions Matter**
   - Uniform distributions aren't always valid
   - Hidden variables can reverse trends

4. **Our Intuition is Linear**
   - We think in simple proportions
   - Reality often involves compounding, weighting, or conditioning

### Why Study These Paradoxes?

- **Critical Thinking:** Question assumptions in statistical arguments
- **Data Literacy:** Understand how data can mislead
- **Decision Making:** Make better choices under uncertainty
- **Mathematical Beauty:** Appreciate the counterintuitive nature of probability

---

## Further Reading

- **Probability Theory:** Kolmogorov's axioms, Bayes' theorem
- **Statistical Inference:** Hypothesis testing, confidence intervals
- **Decision Theory:** Expected utility, risk assessment
- **Cognitive Biases:** Availability heuristic, base rate neglect
