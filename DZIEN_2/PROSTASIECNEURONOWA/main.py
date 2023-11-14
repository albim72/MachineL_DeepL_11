import numpy as np
from simplene import SimpleNeuralNetwork

network = SimpleNeuralNetwork()
print(network.weights)

train_inputs = np.array(
    [[1,1,0],[1,1,1],[1,1,0],[1,0,0],[0,1,1],[0,1,0],[0,0,0],[0,0,0]]
)

train_outputs = np.array([[0,1,0,0,1,0,0,0]]).T

train_iteration = 50000

network.train(train_inputs,train_outputs,train_iteration)
print(network.weights)

print('Testowanie danych')
test_data = np.array([[1,1,1],[1,0,0],[0,1,1],[0,1,0],[0,0,0],])

for data in test_data:
    print(f"Wynik dla {data}: {network.propagation(data)}")
