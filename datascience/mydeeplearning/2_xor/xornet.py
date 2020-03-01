import random
import numpy as np


epoch = 10000000
lr = 0.7

class XorModel():
    def __init__(self,w=None):
        if w == None:
            # self._w1 = np.random.rand(3,2)
            # self._w2 = np.random.rand(3)
            self._w1 = np.random.uniform(low=-0.1,high=0.1,size=(3,2))
            self._w2 = np.random.uniform(low=-0.1,high=0.1,size=3)
        else:
            self._w1 = w[0]
            self._w2 = w[1]

    def _sigmoid(self, x, differential= False):
        '''
         sigmoid
        :param x: sigmoid target data
        :param differential: is differential?
        :return:
        '''
        if differential:
            return x * (1 - x)
        return 1 / (1 + np.exp(-x))


    def _layer1(self,x, differential= False,backpropagation = None,layer1=None):
        '''
        layer1
            2 neural network  + sigmoid
        :param x: input data
        :param differential: is differential?
        :param backpropagation: layer2 backpropagation
        :param layer1: layer1 output
        :return:
        '''
        if differential:
            # return np.dot(np.transpose([(1 - self.w2[:2]) * x[:2]]),np.array([backpropagation]))
            # return np.dot(np.transpose(np.array([backpropagation * (1-layer1)])),np.array([w2[:2]]) * x[:2])
            return np.dot(np.transpose([backpropagation * (1-layer1) * self._w2]),np.array([x[:2]]))
        return self._sigmoid(np.dot(x,self._w1))

    def _layer2(self,x, differential= False, y = None,predict = None,layer1 = None):
        '''
           1 neural network  + sigmoid
        :param x: layer1 output
        :param differential" is differential?
        :param y: label
        :param layer1: layer1 output
        :param predict: model predict
        :return:
        '''
        if differential:
            return -self._sigmoid(predict,True) * (y - predict) * layer1
        return self._sigmoid(np.dot(x,self._w2))

    def predict(self,x,training= False):
        '''
         predict
        :param x: input data
        :param training: training mode
        :return:
        '''
        # bias
        x = np.append(x,1)
        # layer 1
        layer1 = self._layer1(x)
        # bias
        layer1 = np.append(layer1, 1)
        # layer 2
        layer2 = self._layer2(layer1)
        if training:
            return layer1, layer2
        return layer2

    def _cal_decent(self, x, label, layer1, predict):
        x = np.append(x,1)
        # backpropagation
        backpropagation_l2 = self._layer2(x,True,label,predict,layer1)
        backpropagation_l1 = self._layer1(x,True,backpropagation_l2,layer1)
        return backpropagation_l1, backpropagation_l2


    def optimize(self, datas, labels, epoch, lr):
        for epoch_number in range(epoch):
            layer1, predict = self.predict(datas[0],True)
            differential_l1, differential_l2  = self._cal_decent(datas[0],labels[0], layer1, predict)
            for i, data in enumerate(datas[1:]):
                layer1, predict = self.predict(datas[0], True)
                temp_l1, temp_l2 = self._cal_decent(data,labels[i],layer1,predict)
                differential_l1 += temp_l1
                differential_l2 += temp_l2
            # weight update  w -  w' * lr
            # self.w1 -= np.transpose(differential_l1) * lr
            self._w1 -= differential_l1 * lr
            self._w2 -= differential_l2 * lr

            if epoch_number % 100 == 0:
                print("epoch : {}".format(epoch_number))
                print("입력\t예측\t정답")
                loss = 0
                for j, data in enumerate(datas):
                    predict =  self.predict(data)
                    print("{0}\t{1:.2f}\t{2}".format(data,predict,labels[j]))
                    loss += pow(data[1] - predict,2)
                print("loss = {}".format(loss))

if __name__ =="__main__":
    # w1 = np.array([[-0.089, 0.098], [0.028, -0.070], [0.092, -0.010]])
    # w2 = np.array([0.056, 0.067, 0.016])
    w1 =  np.ones((3,2))
    w2 = np.ones(3)
    # xor_model = XorModel([w1,w2])
    xor_model = XorModel()
    data = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    label = np.array([1.0, 0.0, 0.0, 1.0])
    result = xor_model.optimize(data, label,epoch, lr)