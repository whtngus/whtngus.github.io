from abc import *
import numpy as np

class NumericalGradient():
    def __init__(self,f):
        self.f = f

    def update_gradient(self,x, h = 1e-4):
        '''
            편미분 함수
            최적화 해야하는 파라미터가 2개 이상일때
        :param f: 함수
        :param h: default 1e-4  # 0.0001
        :param x: 입력값
        :return: 미분 결과
        '''
        grad = np.zeros_like(x)  # x와 형상이 같은 배열을 생성
        for idx in range(x.size):
            tmp_val = x[idx]
            # f(x+h) 계산
            x[idx] = tmp_val + h
            fxh1 = self.f(x)
            # f(x-h) 계산
            x[idx] = tmp_val - h
            fxh2 = self.f(x)

            grad[idx] = (fxh1 - fxh2) / (2 * h)
            x[idx] = tmp_val  # 값 복원
        return grad

