from abc import *
import numpy as np
from gradient import Gradient

class NumericalGradient(Gradient):

    @abstractmethod
    def update_gradient(self,x):
        pass