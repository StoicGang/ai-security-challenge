# imports 
import torch 
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

# 1. Generate dataset
# x-feature matrix, y-labels
X, y = make_moons(n_samples=200, noise=0.2, random_state=42) 

# 2. Split into training and testing dataset
# Use 80% for training and 20% for testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Convert to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.long)

# 4. Define 2-layer MLP
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(2,16),  # input features =2
            nn.ReLU(),
            nn.Linear(16,2)   # output classes =2
        )
    def forward(self, x):
        return self.layers(x)

model = MLP()

# 5. Loss and optimizing 
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 6. epoch
epoches = 10
for epoch in range(epoches):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()

    print(f"Epoach {epoch+1}/{epoches}, Loss: {loss.item():.4f}")

# 7. final output evalution 
with torch.no_grad():
    predictions = model(X_test).argmax(dim=1)
    accuracy = (predictions == y_test).float().mean()
    print(f"Test Accuracy: {accuracy:.2f}")