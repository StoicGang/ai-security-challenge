## Query 1
`Query:` what is fgsm

```Top 2 Results:

Result 1
ID: chunk_6
Distance: 0.8649
er the step, the model’s behaviour has shifted and the direction that was optimal at the start may no longer be optimal at the landing point.

This is why FGSM sometimes fails against models with adversarial defences. The one-step shortcut, which makes it fast, also makes it imprecise.

The attacks ...
------------------------------------------------------------
Result 2
ID: chunk_4
Distance: 1.2599
acker’s stealth dial.
Putting It Together:One Step, Done

Put all four parts back together:

x_adv = x + ε · sign( ∇ₓ J(θ, x, y) )

In plain English: take the original input, ask the model which direction every pixel should move to cause maximum loss, keep only the direction (not the magnitude), sca...
------------------------------------------------------------
```

## Query 2
`Query:` what is the formula 

```
Top 2 Results:

Result 1
ID: chunk_1
Distance: 1.5015
e formula describes what gets added to it.
Part 2:∇ₓ J(θ, x, y), The Gradient

This is the compass.

J(θ, x, y) is the loss function the score that measures how wrong the model's prediction is. During normal training, the model computes this loss and asks: "How should I change my weights to reduce i...
------------------------------------------------------------
Result 2
ID: chunk_0
Distance: 1.5581
One line of math. Four moving parts. A model that breaks in a single step.

In the last article, we established what Fast Gradient Sign Method (FGSM) is and why it exists.

Now we go inside it.

By the end of this article, you should be able to look at the FGSM formula, point at each piece, and expl...
------------------------------------------------------------
```

## Query 3
`Query:` Gradient descent

```
Top 2 Results:

Result 1
ID: chunk_0
Distance: 1.0352
One line of math. Four moving parts. A model that breaks in a single step.

In the last article, we established what Fast Gradient Sign Method (FGSM) is and why it exists.

Now we go inside it.

By the end of this article, you should be able to look at the FGSM formula, point at each piece, and expl...
------------------------------------------------------------
Result 2
ID: chunk_1
Distance: 1.0664
e formula describes what gets added to it.
Part 2:∇ₓ J(θ, x, y), The Gradient

This is the compass.

J(θ, x, y) is the loss function the score that measures how wrong the model's prediction is. During normal training, the model computes this loss and asks: "How should I change my weights to reduce i...
------------------------------------------------------------
```

## Query 4
`Query:`Cybersecurity Attack 

```
Top 2 Results:

Result 1
ID: chunk_3
Distance: 1.4955
n to the human eye. The attack is distributed too evenly to see.
Part 4 ε (Epsilon), The Budget

ε is a small number. Typically between 0.01 and 0.3.

It controls how far each pixel is allowed to move. Think of it as the attacker’s budget. Spend more, the attack succeeds more reliably. Spend too muc...
------------------------------------------------------------
Result 2
ID: chunk_4
Distance: 1.5526
acker’s stealth dial.
Putting It Together:One Step, Done

Put all four parts back together:

x_adv = x + ε · sign( ∇ₓ J(θ, x, y) )

In plain English: take the original input, ask the model which direction every pixel should move to cause maximum loss, keep only the direction (not the magnitude), sca...
------------------------------------------------------------
```