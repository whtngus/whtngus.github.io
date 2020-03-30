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
        data_size = len(y)
        for i in range(epoch):
            weight, bias = self.neuralent.get_w()
            pred_y = self.neuralent.neural_out(x)
            w_d, b_d = self._update_gradient(weight, bias,y, pred_y, data_size)
            w_d = -lr*(w_d/data_size)
            b_d = -lr*(b_d/data_size)
            self.neuralent.update_subtraction(w_d,b_d)
            print("============== epoch : {} ====================".format(i))
            print("1,1 : {}".format(self.neuralent.neural_out([1,1])))
            print("1,0 : {}".format(self.neuralent.neural_out([1,0])))
            print("0,1 : {}".format(self.neuralent.neural_out([0,1])))
            print("0,0 : {}".format(self.neuralent.neural_out([0,0])))
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
            w_d.append(np.zeros_like(weight[i]))
            b_d.append(np.zeros_like(bias[i]))
        w_d = np.array(w_d)
        b_d = np.array(b_d)
        for data_index in range(data_size):
            chain_w = self.loss_d(y[data_index], y_pred[data_index]) * self.activation_d[-1](np.append(weight[-1],bias[-1]))
            w_d[-1] += chain_w[:-1]
            b_d[-1] += chain_w[-1]
            for layer_index in range(len(w_d)-2,-1,-1):
                sigmoid_layer_d = np.array([self.activation_d[layer_index](np.append(weight[layer_index][i],bias[layer_index][i])) for i in range(len(weight[layer_index]))])
                # befor_weight = np.transpose(np.array([np.append(weight[layer_index+1])]))
                befor_weight = np.hstack((weight[layer_index],bias[layer_index].reshape(-1,1)))
                befor_chain = np.array([chain_w[:-1]])
                chain_rule_d = np.array([])
                # if len(chain_w.shape) == 1:
                #     chain_rule_d = np.dot(befor_weight , befor_chain)
                # else:
                for i in np.transpose(befor_chain):
                    if len(chain_rule_d) == 0:
                        chain_rule_d = befor_weight * i
                        continue
                    chain_rule_d += befor_weight * i

                chain_w = sigmoid_layer_d * chain_rule_d
                w_d[layer_index] += chain_w[:,:-1]
                b_d[layer_index] += chain_w[:,-1]
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