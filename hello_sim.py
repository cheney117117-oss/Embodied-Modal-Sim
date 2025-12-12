import numpy as np
import torch
print("=== Sim-to-Real Environment Check ===")
print(f"Numpy Version:inp.__version__")
print(f"PyTorch Version: {torch.__version__}")
if torch.cuda.is_available():
    print(" GPU is ready:"+ torch.cuda.get_device_name(0))
else:
    print(" GPU not found! Check NVIDIA Driver.")