import math
import random

# 1. Setup Data (XOR)
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

# 2. Activation functions
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 3. Initialize Weights (2 inputs -> 4 hidden -> 1 output)
random.seed(1)
w_input_hidden = [[random.uniform(-1, 1) for _ in range(4)] for _ in range(2)]
w_hidden_output = [random.uniform(-1, 1) for _ in range(4)]
lr = 0.5

# 4. Training Loop
for epoch in range(10000):
    for i in range(len(X)):
        # Forward Pass
        # Hidden Layer neurons
        hidden = []
        for j in range(4):
            activation = sum(X[i][k] * w_input_hidden[k][j] for k in range(2))
            hidden.append(sigmoid(activation))
        
        # Output Layer
        out_activation = sum(hidden[j] * w_hidden_output[j] for j in range(4))
        output = sigmoid(out_activation)
        
        # Backpropagation
        error = y[i] - output
        d_output = error * sigmoid_derivative(output)
        
        d_hidden = []
        for j in range(4):
            h_error = d_output * w_hidden_output[j]
            d_hidden.append(h_error * sigmoid_derivative(hidden[j]))
            
        # Update Weights
        for j in range(4):
            w_hidden_output[j] += hidden[j] * d_output * lr
            for k in range(2):
                w_input_hidden[k][j] += X[i][k] * d_hidden[j] * lr

# 5. Final Test
print("Final Results:")
for i in range(len(X)):
    hidden = [sigmoid(sum(X[i][k] * w_input_hidden[k][j] for k in range(2))) for j in range(4)]
    final = sigmoid(sum(hidden[j] * w_hidden_output[j] for j in range(4)))
    print(f"Input: {X[i]} Predicted: {final:.4f}")
