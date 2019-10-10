import numpy as np
import sys
sys.path.insert(1, './activation/')
from activation import Activation

class NeuralNet():
    def __init__(self,inout_shape,activations,neural_shape,w = None,b=None):
        self.activation_names = activations
        self.activations = self._activate_initialize(activations)
        if w == None:
            self._w, self._b = self._weight_initialize(inout_shape, neural_shape)
        else:
            self._w,self._b = w,b
        self._w = np.array(self._w)
        self._b = np.array(self._b)

    def _activate_initialize(self,activations):
        act = Activation()
        activation_list = []
        for activation_name in activations:
            activation_list.append(act.get_activation(activation_name))
        # 마지막 활성화 함수를 안쓴 경우를 위해
        activation_list.append(act.get_activation("default"))
        return activation_list

    def _weight_initialize(self,inout_shape,neural_shape):
        weight = [np.random.randn(neural_shape[0], inout_shape[0])]
        bias = [np.random.randn(neural_shape[0])]
        for index in range(len(neural_shape) -1):
            weight.append(np.random.randn(neural_shape[index + 1],neural_shape[index]))
            bias.append(np.random.randn(neural_shape[index+1]))
        weight.append(np.random.randn(inout_shape[1], neural_shape[-1]))
        bias.append(np.random.randn(inout_shape[1]))
        return weight, bias

    def update_subtraction(self,update_w,update_b):
        self._w += update_w
        self._b += update_b

    def neural_out(self,x):
        result_w = np.array(x)
        for i, layer in enumerate(self._w):
            b = self._b[i]
            matrix = np.dot(result_w, np.transpose(layer))
            result_w = [self.activations[i](neural + b) for neural in matrix]
        return np.array(result_w)

    def get_activation_names(self):
        return self.activation_names

    def get_w(self):
        return self._w ,self._b