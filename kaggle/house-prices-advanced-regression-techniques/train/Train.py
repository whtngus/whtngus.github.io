from utils.DataLoader import DataLoader
from keras.models import load_model
from  Model import Model
import numpy as np
from tensorflow.python.keras.callbacks import TensorBoard, ModelCheckpoint, EarlyStopping
import csv
from time import time
import math
import matplotlib.pyplot as plt

class ClassificationTrain:

    def __init__(self,model_path):
        self.dataLoader = DataLoader()
        self.model_path = model_path

    def train(self,epochs,batch_size,lr,train_path,train_rate):
        '''

        :param epochs: epochs
        :param batch_size: batch Size
        :param lr : learningRate
        :return:
        '''
        train, label, train_dev, label, label_dev = self.dataLoader.train_loader(train_path, train_rate)

        model = Model()
        model.train_model(lr,len(train[0]))
        model = model.model

        MODEL_SAVE_FOLDER_PATH = "../data/model/"
        model_path = MODEL_SAVE_FOLDER_PATH + '{epoch:02d}-{val_loss:.4f}.hdf5'
        cb_checkpoint = ModelCheckpoint(filepath=model_path, monitor='val_loss', verbose=2, save_best_only=True)

        cb_early_stopping = EarlyStopping(monitor='val_loss', patience=100)
        # tb_hist = TensorBoard(log_dir='../data/tensorboard/logs/{}'.format(time()), histogram_freq=0, write_graph=True,
        #                       write_images=True)

        tb_hist =  TensorBoard(log_dir='../data/tensorboard/logs/{}'.format(time()))

        history = model.fit(train, label, epochs=epochs, batch_size=batch_size,verbose=2,
                                  callbacks=[tb_hist,cb_checkpoint,cb_early_stopping], validation_data=(train_dev, label_dev))
        # train_history_detail = history.history
        # model.save(self.model_path) # 모델 저장
        plt.plot(history.history['mean_absolute_error'])
        plt.plot(history.history['val_mean_absolute_error'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()
        # summarize history for loss
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()

    def test(self,data_path, output_path):
        data_list, id_list = self.dataLoader.test_loader(data_path)

        model = load_model(self.model_path)
        yhat = model.predict(np.array(data_list))

        f = open(output_path,"w",encoding="utf-8",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Id","SalePrice"])
        for index, label in enumerate(yhat):
            if math.isnan(label[0]):
                print(" : nan id Name : ", id_list[index])
                label[0]= 180921.195890 # 평균값
            csv_writer.writerow([id_list[index], label[0]])

        f.close()

if __name__ == "__main__":
    mode = "train"
    model_path = "../data/model"
    if mode == "test":
        model_path = "../data/model/26-1785017941.3333.hdf5"
        dataPath = "../data/test.csv"
        train = ClassificationTrain(model_path)
        train.test(dataPath,"../data/submission.csv")
    elif mode == "train":

        train = ClassificationTrain(model_path)
        epoch = 100000
        batch_size = 5
        lr = 0.005
        train_rate = 95
        train_path = "../data/train.csv"

        train.train(epoch,batch_size,lr,train_path,train_rate)