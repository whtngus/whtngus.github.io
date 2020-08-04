import numpy as np
from matplotlib import pyplot as plt

class XorModel():
    def __init__(self, input_shape = [4,2], w=None,output_sigmoid=True):
        '''

        :param input_shape: [Hidden node net size,input data size]
        :param w: input weights
        :param output_sigmoid: use output activation?
        '''
        input_shape[1] += 1
        self.input_shape = input_shape
        self.output_sigmoid = output_sigmoid
        if w == None:
            self._w1 = np.random.uniform(low=-0.1, high=0.1, size=input_shape)
            self._w2 = np.random.uniform(low=-0.1, high=0.1, size=input_shape[0]+1)
        else:
            self._w1 = w[0]
            self._w2 = w[1]

    def _sigmoid(self, x):
        '''
         sigmoid
        :param x: sigmoid target data
        :return:
        '''
        return 1 / (1 + np.exp(-x))

    def _neural_net(self, x, weight):
        '''
        :param x: input data
        :param weight: matrix weight
        :return:
        '''
        # bias
        x = np.append(x, 1)
        return np.dot(weight, x)

    def predict(self, x, training=False):
        '''
         predict
        :param x: input data
        :param training: training mode
        :return:
        '''
        # layer 1
        l1 = self._neural_net(x, self._w1)
        # sigmoid
        l1_active = self._sigmoid(l1)
        # layer 2
        l2 = self._neural_net(l1_active, self._w2)
        # sigmoid
        if self.output_sigmoid:
            l2_active = self._sigmoid(l2)
        else:
            l2_active = l2
        if training:
            return l1_active, l2_active
        return l2_active

    def _cal_decent(self, x, label, l1_active, l2_active):
        '''
        백프로파게이션 계산
        :param x: input data
        :param label: target
        :param l1_active: layer 1 output
        :param l2_active: layer 2 output
        :return:
        '''
        # bias
        x = np.append(x, 1)
        # backpropagation
        if self.output_sigmoid:
            # common : -(t - o) * o * (1 - o)
            backpropagation = -(label - l2_active) * l2_active * (1 - l2_active)
        else:
            # common : -(t - o)
            backpropagation = -(label - l2_active)
        #  common * (h + bias)
        backpropagation_l2 = backpropagation * np.append(l1_active, 1)
        # common * (1 - h) * h * weights_layer2 * x
        backpropagation_l1 = ((1 - l1_active) * l1_active * self._w2[:-1]).reshape(self.input_shape[0], 1) * x.reshape(1, self.input_shape[1]) * backpropagation
        return backpropagation_l1, backpropagation_l2

    def optimize(self, datas, labels, epoch, lr):
        '''
        학습
        :param datas: input data
        :param labels: target
        :param epoch: epoch
        :param lr: learning late
        :return:
        '''
        self.loss_log = []
        for epoch_number in range(epoch):
            l1_active, l2_active = self.predict(datas[0], True)
            loss = (l2_active - labels[0]) ** 2
            differential_l1, differential_l2 = self._cal_decent(datas[0], labels[0], l1_active, l2_active)
            for data, label in zip(datas[1:], labels[1:]):
                l1_active, predict = self.predict(data, True)
                temp_l1, temp_l2 = self._cal_decent(data, label, l1_active, predict)
                differential_l1 += temp_l1
                differential_l2 += temp_l2
                loss += (predict - label) ** 2
            self.loss_log.append(loss)
            # weight update  w -  w' * lr
            # self.w1 -= np.transpose(differential_l1) * lr
            self._w1 -= differential_l1 * lr
            self._w2 -= differential_l2 * lr

            if epoch_number % 1000 == 0:
                print("epoch : {}".format(epoch_number))
                print("입력\t예측\t정답")
                for data, label in zip(datas[:4], labels[:4]):
                    predict = self.predict(data)
                    print("{0}\t{1:.4f}\t{2}".format(data, predict, label))
                # print("l1 : {}".format(self._w1))
                # print("l2 : {}".format(self._w2))
                print("loss = {}".format(loss))

    def show_loss_graph(self):
        '''
        epoch별 에러 그래프 출력
        :return:
        '''
        plt.plot(range(len(self.loss_log)), self.loss_log)
        plt.show()

    def show_predict_graph(self,datas,labels_x,labels):
        '''
        예측 데이터 출력
        :param datas: predict data
        :param labels_x: label input data
        :param labels: label target data
        :return:
        '''
        datas = np.array(datas)
        labels_x = np.array(labels_x)
        predict_x = [self.predict(data) for data in datas]
        fig, ax = plt.subplots()
        # datas : [x, x^2]
        # ax.plot(datas[:,0],predict_x,marker='o',linestyle='',label="predict")
        # ax.plot(labels_x[:,0],labels,marker='o',linestyle='',label="label")
        # datas : [x]
        ax.plot(datas,predict_x,marker='o',linestyle='',label="predict")
        ax.plot(labels_x,labels,marker='o',linestyle='',label="label")

        ax.legend(fontsize=12, loc='lower left')  # legend position
        plt.title('Scatter Plot of input data predict', fontsize=20)
        plt.xlabel('input x', fontsize=14)
        plt.ylabel('predict', fontsize=14)
        plt.show()




if __name__ == "__main__":
    # 문제 1
    epoch = 20000
    lr = 0.5
    w1 = np.array(([-0.089, 0.028, 0.092], [0.098, -0.07, -0.01]))
    w2 = np.array([0.056, 0.067, 0.016])
    # use initialize ppt weights
    # xor_model = XorModel(input_shape=[2,2],w=[w1, w2])
    # use random initialize weights
    xor_model = XorModel(input_shape=[2,2])
    data = np.array(([0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]))
    label = np.array((0.0, 1.0, 1.0, 0.0))
    xor_model.optimize(data, label, epoch, lr)
    xor_model.show_loss_graph()

    # 문제2
    epoch = 5000
    lr = 0.02
    x = np.arange(-1,2,0.1)
    # 0.2 단위 짝수번째 인덱스만 추출하여 학습
    data = lambda input : [[x,x**2] for x in input]
    label = lambda input : [4*x*(1-x) for x in input]
    input_x = x[::2]
    input_y = label(input_x)
    # datas : [x, x^2]
    # input_x = data(input_x)
    xor_model = XorModel(input_shape=[5,1],output_sigmoid=False)
    xor_model.optimize(input_x,input_y,epoch,lr)
    # datas : [x, x^2]
    # xor_model.show_predict_graph(data(x),input_x,input_y)
    # datas : [x]
    xor_model.show_predict_graph(x,input_x,input_y)
    xor_model.show_loss_graph()
