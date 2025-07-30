

import torch
from model import Net  # Ensure model.py defines a class Net
import sys

def load_model(model_path="models/model.pt"):
    model = Net()
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()
    return model

def run_inference(model, input_tensor):
    with torch.no_grad():
        output = model(input_tensor)
    return output

if __name__ == "__main__":
    # Example usage
    model = load_model()

    # Replace this with real input
    dummy_input = torch.randn(1, 10)  # Match model input size
    result = run_inference(model, dummy_input)

    print("Inference result:", result)