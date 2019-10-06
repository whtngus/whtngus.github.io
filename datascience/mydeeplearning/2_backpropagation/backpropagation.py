import random


class Learner():
    def __init__(self,layer_shape,inout_shape, differential,w=[]):
        self.inout_shape = inout_shape
        self.layer_shape = layer_shape
        self.differential = differential
        self.w = w
        self.initialize()

    def initialize(self):
        pass

    def cal_decent(self,data_x,data_y,weights):
        common = -2.0 * (data_y - self.model_w3(data_x,weights))
        # w2 미분 : -2 * (y - f(x)) * x^2
        w2 = common * pow(data_x,2)
        # w1 미분 : -2 * (y - f(x)) * x
        w1 = common * data_x
        # w0 미분 : -2 * (y - f(x))
        w0 = common
        return w0, w1, w2

    def optimize(self,datas, epoch, lr):
        # w2 w1 w0
        weights = [random.random(),random.random(),random.random()]
        for i in range(epoch):
            w0_sum = 0.0
            w1_sum = 0.0
            w2_sum = 0.0
            for data in datas:
                w0_sum_t, w1_sum_t, w2_sum_t = self.cal_decent(data[0],data[1] , weights)
                w0_sum += w0_sum_t
                w1_sum += w1_sum_t
                w2_sum += w2_sum_t
            # weight update  w -  w' * lr
            weights[0] -= w2_sum * lr
            weights[1] -= w1_sum * lr
            weights[2] -= w0_sum * lr
            print("epoch : {}".format(i))
            print("입력\t예측\t정답")
            loss = 0
            for data in datas:
                predict =  self.model_w3(data[1],weights)
                print("{}\t{}\t{}".format(data[1],predict,data[1]))
                loss += pow(data[1] - predict,2)
            print("loss = {}".format(loss))

# def model_w3(data, weights):
#     return weights[0] * pow(data,2) + weights[1] * data + weights[2]
if __name__ == "__main__":
    differential = "numericla"
    layer_shape = [2,1]
    inout_shzpe = [2,1]
    data = [(1, 1), (1, 0), (0, 1), (0, 0)]
    label = [0,1,1,0]
    epoch = 500
    lr = 0.001
    learner = Learner(layer_shape,inout_shzpe,differential)
    weight_result = learner.optimize(data, label, epoch, lr)
    print()



