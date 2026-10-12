# Probability Projects

A collection of small Python projects that explore probability through simulation.

## Projects

1. **Monte Carlo Pi Estimation** (`pi-estimation/`) - estimates the value of pi using random points, and studies how the estimate converges.
2. **Birthday Paradox** (`birthday-paradox/`) - compares the exact formula with a simulation to show that 23 people give about a 50% chance of a shared birthday.
3. **Central Limit Theorem with Dice** (`clt-dice/`) - rolls 1, 2, 5 and 30 dice 10,000 times each to show that averages form a bell curve, and that the spread shrinks by about 1/√n as dice are added.
4. **Bayes' Rule: Medical Test** (`bayes-medical-test/`) - shows by counting, simulation and formula that a positive result from a 90% accurate test means only about a 9% chance of being sick when the disease is rare, and plots how that chance changes with the disease rate.
5. **Monte Carlo Stock Simulation** (`monte-carlo-stock/`) - simulates 1,000 possible years of a stock with random daily returns, estimates about a 12% chance of losing 10% or more, and shows why final prices are skewed but their logarithm is a bell curve.

## Concepts covered

- Law of large numbers
- Complement rule
- Monte Carlo simulation
- Central Limit Theorem
- Standard deviation
- Conditional probability
- Bayes' rule
- Normal distribution
- Random walk and compounding returns
- Lognormal distribution

## Tools

Python, NumPy, Matplotlib, Jupyter Notebook