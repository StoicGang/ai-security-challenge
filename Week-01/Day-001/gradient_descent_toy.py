import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# 1. Create a toy dataset
# -------------------------

np.random.seed(42)

x = np.arange(1, 21)
y = 3 * x + 5 + np.random.randn(20)

# -------------------------
# 2. Initialize parameters
# -------------------------

w = 0.0
b = 0.0

learning_rate = 0.01
epochs = 500

loss_history = []

n = len(x)

# -------------------------
# 3. Gradient Descent
# -------------------------

for epoch in range(epochs):

    # Predictions
    y_pred = w * x + b

    # Mean Squared Error
    loss = np.mean((y - y_pred) ** 2)
    loss_history.append(loss)

    # Compute gradients
    dw = (-2 / n) * np.sum(x * (y - y_pred))
    db = (-2 / n) * np.sum(y - y_pred)

    # Update parameters
    w = w - learning_rate * dw
    b = b - learning_rate * db

# -------------------------
# 4. Results
# -------------------------

print(f"Learned weight (w): {w:.3f}")
print(f"Learned bias (b): {b:.3f}")
print(f"Final loss: {loss_history[-1]:.3f}")

# -------------------------
# 5. Plot Loss
# -------------------------

plt.plot(loss_history)
plt.title("Gradient Descent Loss")
plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.savefig("loss_plot.png")
plt.show()