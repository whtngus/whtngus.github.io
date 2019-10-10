import random
import numpy as np
import sys
sys.path.insert(1, './network/')
sys.path.insert(2, './optimize/')
from neuralnet import NeuralNet
from numericalGradient import NumericalGradient
from partialGradient import PartialGradient

class Learner():
    def __init__(self,inout_shape,activations,neural_shape,differential,loss,w = None,f=None):
        if w:
            neural_net = NeuralNet(inout_shape,activations,neural_shape,w)
        else:
            neural_net = NeuralNet(inout_shape,activations,neural_shape)
        self._initialize(differential,f,neural_net, loss)

    def _initialize(self,differential,f,neural_net,loss):
        if differential == "numerical":
            # f initialize
            if not f:
                f = neural_net.neural_out
            self.differential = NumericalGradient(f)
        else:
            # default : PartialGradient
            self.differential = PartialGradient(neural_net,loss)

    def train(self,data, label, epoch, lr):
        neural_net = self.differential.optimize(data, label, lr, epoch)

        print()


if __name__ == "__main__":
    differential = "partial"
    loss = "mse"
    layer_shape = [3,2]
    inout_shzpe = [2,1]
    activations = ["sigmoid","sigmoid","sigmoid"]
    data = [(1, 1), (1, 0), (0, 1), (0, 0)]
    label = [0,1,1,0]
    epoch = 500
    lr = 0.005
    learner = Learner(inout_shzpe,activations,layer_shape,differential,loss)
    weight_result = learner.train(data, label, epoch, lr)
    print()

