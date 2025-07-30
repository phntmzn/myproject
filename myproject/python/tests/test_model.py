import unittest
import torch
from myproject.model import Net

class TestNetModel(unittest.TestCase):
    def test_output_shape(self):
        model = Net()
        input_tensor = torch.randn(5, 10)  # Batch of 5
        output = model(input_tensor)
        self.assertEqual(output.shape, (5, 1))

    def test_forward_pass_runs(self):
        model = Net()
        input_tensor = torch.randn(1, 10)
        try:
            _ = model(input_tensor)
        except Exception as e:
            self.fail(f"Forward pass raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
