from DataLoader import DataLoader
from keras.models import load_model
from  Model import Model
import numpy as np
import csv

class ClassificationTrain:

    def __init__(self,dataPath,extract_data,model_path):
        self.data_loader = DataLoader(dataPath,extract_data)
        self.model_path = model_path

    def train(self,epochs,batch_size,lr):
        '''

        :param epochs: epochs
        :param batch_size: batch Size
        :param lr : learningRate
        :return:
        '''
        data_list, label_list, _ = self.data_loader.data_loader()

        model = Model()
        model.train_model(lr,len(data_list[0]))
        model = model.model
        train_history = model.fit(data_list, label_list, epochs=epochs, batch_size=batch_size,verbose=1)
        train_history_detail = train_history.history
        model.save(self.model_path)

    def test(self,output_path):
        data_list, label_list, passinger_id = self.data_loader.data_loader()
        model = load_model(self.model_path)

        yhat = model.predict_classes(np.array(data_list))
        collect_count = 0
        collect_detail = [0,0]
        f = open(output_path,"w",encoding="utf-8",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow(["PassengerId","Survived"])
        for inex, label in enumerate(label_list):
            csv_writer.writerow([passinger_id[inex], yhat[inex][0]])
            if float(label) == yhat[inex]:
                collect_count += 1
                if yhat[inex] == 0:
                    collect_detail[0] += 1
                elif yhat[inex] == 1:
                    collect_detail[1] += 1
            print(label ,"   " , yhat[inex])
        f.close()
        print("collect_count : ",collect_count)
        print("collect_detail : ",collect_detail)
        print("acc : ",collect_count/len(yhat))

if __name__ == "__main__":
    mode = "test"
    extract_data = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked","Name","PassengerId"]
    model_path = "../data/model"
    if mode == "test":
        dataPath = "../data/test.csv"
        train = ClassificationTrain(dataPath,extract_data,model_path)
        train.test("../data/submission.csv")
    elif mode == "train":
        dataPath = "../data/train.csv"
        train = ClassificationTrain(dataPath,extract_data,model_path)
        epoch = 100
        batch_size = 10
        lr = 0.01
        train.train(epoch,batch_size,lr)