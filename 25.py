# Feed Forward Neural Network
import numpy as np
weights = np.random.rand(3, 3)
input_data = np.array([1, 0, 1])
output = np.dot(weights, input_data)
print("Neural Network Output:", output)
