from abc import *

class Gradient(metaclass=ABCMeta):
    def __init__(self,differential_option,f):
        self.differential_option = differential_option
        self.f = f

    @abstractmethod
    def update_gradient(self,x):
        pass

