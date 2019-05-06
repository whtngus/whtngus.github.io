from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Concatenate
from keras.models import Model
from keras.layers.convolutional import MaxPooling2D, Conv2D
from keras import optimizers
from keras import losses

class Model:
    def train_model(self,lr,input_dim):
        self.model = Sequential()

        self.model.add(Dense(output_dim=input_dim*2,activation='relu',input_dim=input_dim))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(output_dim=input_dim*2,activation='relu'))
        self.model.add(Dropout(0.3))
        self.model.add(Dense(output_dim=1,activation='sigmoid'))
        self.model.add(Dropout(0.3))


        adam = optimizers.Adam(lr=lr, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
        self.model.compile(loss=losses.mean_squared_error, optimizer=adam, metrics=['accuracy'])
        self.model.summary()