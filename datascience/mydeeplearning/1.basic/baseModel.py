import random
import matplotlib.pyplot as plt
import numpy as np
'''
𝑓 𝑥;𝑤0,𝑤1,𝑤2 = 𝑤2𝑥2 + 𝑤1𝑥 + 𝑤0
'''
class BasicModel():

    def __init__(self):
        self.weight = [random.random() for _ in range(3)]
        self.fx = lambda weights, x : weights[0]*x**2 + weights[1]*x + weights[2]

    def fit(self,datas,learning_late,epoch,plot_iter = False):
        '''
        데이터 학습
        :param datas: 학습 데이터
        :param learning_late: 학습률
        :param epoch: epoch
        :param plot_iter: plot 출력 epoch 주기
        :return:
        '''
        for i in range(epoch):
            error = [0] * 3
            for data in datas:
                predict = self.fx(self.weight,data[0])
                common_error = -2*(data[1]-predict)
                error[0] += common_error * (data[0] ** 2)
                error[1] += common_error * data[0]
                error[2] += common_error
            self.weight[0] -= error[0] * learning_late
            self.weight[1] -= error[1] * learning_late
            self.weight[2] -= error[2] * learning_late
            if i % 10 == 0:
                print("=== epoch : {} ===".format(i))
                if type(plot_iter) == int:
                    self._display(datas,i%plot_iter==0)
                else:
                    self._display(datas,False)

    def _display(self,datas,plot):
        '''
        트레이닝 상황 출력
        :param datas: 데이터
        :param plot: plot 출력 여부 
        :return:
        '''
        error = 0
        for data in datas:
            x = data[0]
            predict = self.fx(self.weight,data[0])
            y = data[1]
            error += (y-predict)**2
            print("data : {}, predict : {}, label : {}".format(x,predict,y))
            print("weight : {}".format(self.weight))
        print("error : ", error)
        if plot:
            datas = np.array(datas)
            x = np.linspace(-5, 5, 100)
            y = [self.fx(self.weight, x_data) for x_data in x]
            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            ax.spines['left'].set_position('center')
            ax.spines['bottom'].set_position('zero')
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            plt.ylim(-5, 5)
            # plot the function
            plt.plot(x, y, 'r')
            # plot the data
            plt.scatter(np.array(datas)[:,0], np.array(datas)[:,1])
            # show the plot
            plt.show()


if __name__ == "__main__":
    data = [(0.0,0.0),(1.0,1.0),(1.0,2.0),(2.0,1.0)]
    learning_late = 0.01
    epoch = 10000
    plot_iter =  100
    # plot_iter =  False
    model = BasicModel()
    model.fit(data,learning_late,epoch,plot_iter)

