import numpy as np

class MultilayerNN():
    def __init__(self, num_inputs, hidden_layers=[3, 3]):
        self.num_inputs = num_inputs
        self.hidden_layers = hidden_layers
        self.num_outputs = num_inputs
        layers = [num_inputs] + hidden_layers + [num_inputs]
        weights = []
        for i in range(len(layers)-1):
            w = np.random.rand(layers[i], layers[i+1])
            weights.append(w)
        self.weights = weights

    def forward_propagate(self, inputs):
        activations = inputs
        for w in self.weights:
            net_inputs = np.dot(activations, w)
            activations = self.sigmoid(net_inputs)
        return activations

    def sigmoid(self, x):
        y = 1.0 / (1 + np.exp(-x))
        return y


num_inputs = int(input("Enter the number of inputs: "))
mlp = MultilayerNN(num_inputs)
inputs = np.random.rand(mlp.num_inputs)
output = mlp.forward_propagate(inputs)
for i, weight in enumerate(output):
    print(f"Generated Weight of input {i+1}: {weight}")
