# Day 1 - Gradient Descent from Scratch

## Objective

Learn how gradient descent trains a simple linear regression model by minimizing prediction error.

---

## What I Learned

Gradient descent is an optimization algorithm that helps a machine learning model improve its predictions. The model first makes a prediction using its current parameters. A loss function measures how far those predictions are from the actual values. The gradient tells us how changing each parameter affects the loss. By moving the parameters a small step in the opposite direction of the gradient, the model gradually reduces its error. Repeating this process many times allows the model to learn the best values for its parameters.

---

## Key Concepts

- **Model:** A mathematical equation used to make predictions.
- **Parameter:** Values (such as weight and bias) that the model learns.
- **Prediction:** The output produced by the model.
- **Loss Function:** Measures how wrong the predictions are.
- **Gradient:** Indicates the direction in which the loss increases the most.
- **Learning Rate:** Controls how large each update step is.

---

## Self Assessment

**Can I explain today's concept in 90 seconds?**
 Yes

Gap:
I understand how to calculate gradients, but I still need a better understanding of why the derivative points toward the steepest increase in the loss function.

---

## Reflection

The most interesting part of today's exercise was seeing the loss decrease after every iteration. Writing the algorithm from scratch made it much easier to understand what machine learning libraries do behind the scenes.