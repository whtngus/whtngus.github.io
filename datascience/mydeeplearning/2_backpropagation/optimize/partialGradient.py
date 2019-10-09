from abc import *
import numpy as np
import sys
sys.path.insert(1, './network/')
from neuralnet import NeuralNet

class PartialGradient():
    def __init__(self,neuralnet,loss):
        self.neuralent = neuralnet
        self.loss_d, self.activation_d = self._loss_initialize(loss)

    def optimize(self,x,y,lr,epoch):
        x = np.array(x)
        y = np.array(y)
        weight, bias = self.neuralent.get_w()
        data_size = len(y)
        for i in range(epoch):
            pred_y = self.neuralent.neural_out(x)
            w_d, b_d = self._update_gradient(weight, bias,y, pred_y, data_size)
        return self.neuralent

    def _update_gradient(self,weight, bias, y, y_pred,data_size):
        # w, b와 형상이 같은 배열을 생성
        # w_d = [np.zeros_like(weight[0])]
        # b_d = [np.zeros_like(bias[0])]
        y = np.array(y)
        y_pred = np.transpose(y_pred)[0]
        w_d = []
        b_d = []
        for i in range(len(weight)):
            w_d.append([np.zeros_like(weight[i])])
            b_d.append([np.zeros_like(bias[i])])
        w_d = np.array(w_d)
        b_d = np.array(b_d)
        for data_index in range(data_size):
            chain_w = self.loss_d(y[data_index], y_pred[data_index]) * self.activation_d[-1](y_pred[data_index])
            backpropagation = w_d[-1] - chain_w
            b_d[-1] -= chain_w
            for layer_index in range(len(w_d)-2,-1,-1):
                # TODO : 모르겠음 ..
                chain_w *= self.activation_d[layer_index](w_d[layer_index + 1])
                w_d
                # w_d[layer_index] -=
                # b_d[layer_index] -=
        return  w_d,b_d

    def _loss_initialize(self,loss):
        loss_d = None
        activation_d = np.array([])
        for activation_name in self.neuralent.get_activation_names():
            if activation_name == "sigmoid":
                activation_d = np.append(activation_d,self._sigmoid_d)
            else:
                activation_d = np.append(activation_d,self._identity_d)

        if loss == "mse":
            loss_d = self._mse_d
        else:
            #cross entropy
            loss_d = self._cross_d
        return loss_d, activation_d

    def _make_bias(self,x):
        return np.hstack((np.array(x),np.ones(len(x)).reshape(-1,1)))

    def _sigmoid_d(self,x):
        # 이미 sigmoid 계산된 x임으로
        # cal_sigmoid = 1 / (1 + np.exp(-x))
        return x*(1-x)

    def _relu(self,x):
        return [1 if i else 0 for i in x > 0 ]

    def _identity_d(self,x):
        return x

    def _mse_d(self,y,pred_y):
        return -(y - pred_y) * pred_y

    def _cross_d(self,y,pred_y):
        return (pred_y-y) / (pred_y*(1-pred_y))