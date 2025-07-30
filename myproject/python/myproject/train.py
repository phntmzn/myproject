

import torch
import torch.nn as nn
import torch.optim as optim
from model import Net

def generate_dummy_data(num_samples=1000):
    x = torch.randn(num_samples, 10)
    y = torch.sum(x, dim=1, keepdim=True)  # Example target
    return x, y

def train_model(model, data, targets, epochs=10, lr=0.001):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(data)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

if __name__ == "__main__":
    model = Net()
    x, y = generate_dummy_data()
    train_model(model, x, y)
    torch.save(model.state_dict(), "models/model.pt")
    print("✅ Model saved to models/model.pt")