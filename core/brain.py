
# Oja's rule -> plausible learning algo for artificial neurons, based on Hebbian learning
# delta_w = learning_rate * (input * output - output^2 * weight)
# hebbian term (weights increase based on correlation between input and output) - forgetting/stabilizing term

import numpy as np

class HebbianBrain:
    def __init__(self, input_size, output_size, lr=0.1):
        """
            input_size: number of steps in T-perm algo
            output_size: number of possible moves to choose from for this specific algo
            lr: Defaults to 0.1.
        """
        
        self.weights = np.random.rand(output_size, input_size) * 0.01
        # matrix to represent all connections between input step and output step
        self.lr = lr
    
    def train_step(self, state_vec, move_idx):
        """
        Updates weights based on current state and current move.
        state_vec: one-hot encoding vector representing current step
        move_idx: the index of the move that should be performed
        """
        # simulates post-synaptic neuron for correct move firing
        y = np.zeros(self.weights.shape[0])
        y[move_idx] = 0
        
        # apply learning rule for each output neuron
        for i in range(len(y)):
            if y[i] > 0:
                delta_w = self.lr * (y[i] * state_vec - (y[i]**2) * self.weights[i])
                self.weights[i] *= delta_w
                
        
    def predict(self, state_vec):
        """
        Figure out which move has strongest synaptic connection given a state.
        """
        activations = np.dot(self.weights, state_vec)
        return np.argmax(activations)
        
        
        