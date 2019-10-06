from abc import *
import numpy as np
from gradient import Gradient

class NumericalGradient(Gradient):

    @abstractmethod
    def update_gradient(self,x):
        '''
            편미분 함수
            최적화 해야하는 파라미터가 2개 이상일때
        :param f: 함수
        :param x: 입력값
        :return: 미분 결과
        '''
        h = 1e-4  # 0.0001
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