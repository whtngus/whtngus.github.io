import numpy as np

class Activation():

    def get_activation(self,activation):
        if activation == "sigmoid":
            return self.sigmoid
        elif activation == "relu":
            return self.relu
        elif activation == "softmax":
            return self.softmax
        elif activation == "tanh":
            return self.tanh
        elif activation == "swish":
            return self.swish
        elif activation == "dswish":
            return self.dswish
        else:
            #default
            return self.default

    def default(self,x):
        return x

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def softmax(self, x):
        x_max = np.max(x)
        x_exp = np.exp(x - x_max)
        return x_exp / np.sum(x_exp)

    def tanh(self, x):
        return np.tanh(x)

    def swish(self, x):
        return x * self.sigmoid(x)

    def dswish(self, x):
        return self.swish(x) + self.sigmoid(x) * (1 - self.swish(x))