import numpy as np
import sys
sys.path.insert(1, '../activation/')
from activation import Activation

class NeuralNet():
    def __init__(self,inout_shape,activation,neural_shape,w = None):
        self.activations = activation
        self.activations = self._activate_initialize(activation)
        self._w = self._weight_initialize(inout_shape, neural_shape) if w is None else self.w = w

    def _activate_initialize(self,activations):
        act = Activation()
        activation_list = []
        for activation_name in activations:
            activation_list.append(act.get_activation(activation_name))
        return activation_list

    def _weight_initialize(self,inout_shape,neural_shape):
        weight = [np.random.randon([inout_shape[0], neural_shape[0]])]
        for index in (len(neural_shape) -1):
            weight.append(np.random.randn(neural_shape[index],[neural_shape[index + 1]]))
        weight.append([np.random.randon([neural_shape[-1], inout_shape[1]])])
        self._w = weight

    def update_subtraction(self,update_value):
        self._w -= update_value

    def neural_out(self,x):
        result = x
        for i, layer in enumerate(self._w):
            result = [self.activations(neural) for neural in np.dot(result, layer)]
        return result

    def get_w(self):
        return self._w