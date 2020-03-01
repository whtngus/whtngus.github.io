import numpy as np

class Loss():
    def __init__(self,loss):
        self.loss = loss

    def get_loss(self):
        if self.loss == "mse":
            return self.mean_squared_error()
        elif self.loss == "crossentropy":
            return self.cross_entropy_error()
        else:
            # default mse
            return self.mean_squared_error()

    def mean_squared_error(self, p, y):
        '''
        MSE 구하기
        :param p: 소프프맥수의 출력 값 (모델 결과값)
        :param y: 정답 값
        :return: MSE 결과
        '''
        return 0.5 * np.sum((y - p) ** 2)

    def cross_entropy_error(self, p, y):
        '''
            정답에 해당하는 출력만을 이용하여 교차 엔트로피 오차를 구함
            원핫 인코딩인 경우에 가능
            정답에 해당하는 교차 엔트로피 (그 경우에만 1) * log(y)
            -LOGe(y) -->  y가 0이면 무한 1이면 0에 가까워짐(정답과 떨어질수록 로스 무한대)
        :param p: 신경망의 출력
        :param y: 정답 레이블
        :return:
        '''
        if y.ndim == 1:
            p = p.reshpae(1, p.size)
            y = y.reshape(1, y.size)

        batch_size = y.shape(0)
        # 1e-7 미세한 근사값
        return -np.sum(y * np.log(p + 1e-7)) / batch_size