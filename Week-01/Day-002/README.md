# Day 002 — Neural Networks — Perceptron to MLP

**Week 1** · ✅ Already Completed · [← Day 001](../Day-001/) · [🏠 Week 1](../README.md) · [📁 Root](../../README.md) · [Day 003 →](../Day-003/)

---

## Today's Task

**Read** (~45 min (already completed)): 3Blue1Brown 'Neural Networks' videos 3–4. Géron ch. 10 — MLP introduction section only.

**Build** (~45 min (already completed)): Build a 2-layer MLP classifier on `/sklearn.datasets.make_moons` using PyTorch. Log training loss per epoch.

**Note:** Already completed — write up the learning log below.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->


### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
- Neuron computes weighted sum + bias.
- Without an activation function a deep network is just one big linear model.
- Learning loop in machine learning is called as apoch. Each apoch should have 
    - Prediction 
    - Measure errors  
    - Computed gradients
    - updated weights

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Generated data.
2. Split it.
3. Converted to tensors.
4. Built an MLP.
5. Trained while monitoring loss.
6. Evaluated accuracy.

### Code Snippet 
<!-- 5–10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
X, y = make_moons(n_samples=200, noise=0.2, random_state=42) 

# 2. Split into training and testing dataset
# Use 80% for training and 20% for testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
- A neuron computes a weighted sum plus bias.
- Hidden neurons receive the same input but learn different features.
- Loss measures prediction error.
- Autograd computes gradients automatically.
- The optimizer updates weights.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
I realized that all hidden neurons receive the same input, but each learns something different because each has different weights. And that without activation functions, adding more layers doesn't make the network more powerful.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
- Visualize the dataset before training.
- Experiment with hidden layer sizes.
- Try different activation functions.
- Read more about Autograd.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
1. Why is ReLU often preferred over Sigmoid?

---

## Day Checklist
- [x] Reading done (within time box — don't let one resource eat the whole day)
- [x] Build complete
- [x] Learning Log fully written (all 8 sections — this .md file IS the deliverable)
- [x] Committed to GitHub

---

[← Day 001](../Day-001/) · [🏠 Week 1](../README.md) · [📁 Root](../../README.md) · [Day 003 →](../Day-003/)
