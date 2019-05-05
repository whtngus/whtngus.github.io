from DataLoader import DataLoader
from keras.models import load_model
from  Model import Model
import numpy as np

class ClassificationTrain:

    def __init__(self,dataPath,extract_data,input_dim,model_path):
        self.input_dim = input_dim
        self.data_loader = DataLoader(dataPath,extract_data)
        self.model_path = model_path

    def train(self,epochs,batch_size,lr):
        '''

        :param epochs: epochs
        :param batch_size: batch Size
        :param lr : learningRate
        :return:
        '''
        data_list, label_list = self.data_loader.data_loader()

        model = Model()
        model.train_model(lr,self.input_dim)
        model = model.model
        train_history = model.fit(data_list, label_list, epochs=epochs, batch_size=batch_size,verbose=1)
        train_history_detail = train_history.history
        model.save(self.model_path)

    def test(self):
        data_list, label_list = self.data_loader.data_loader()
        model = load_model(self.model_path)

        yhat = model.predict_classes(np.array(data_list))
        for inex, label in enumerate(label_list):
            print(label ,"   " , yhat[inex])

if __name__ == "__main__":
    mode = "test"
    input_dim = 11
    extract_data = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
    model_path = "../data/model"
    if mode == "test":
        dataPath = "../data/test.csv"
        train = ClassificationTrain(dataPath,extract_data,input_dim,model_path)
        train.test()
    elif mode == "train":
        dataPath = "../data/train.csv"
        train = ClassificationTrain(dataPath,extract_data,input_dim,model_path)
        epoch = 100
        batch_size = 10
        lr = 0.01
        train.train(epoch,batch_size,lr)