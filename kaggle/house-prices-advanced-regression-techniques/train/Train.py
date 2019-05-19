from utils.DataLoader import DataLoader
from keras.models import load_model
from  Model import Model
import numpy as np
from tensorflow.python.keras.callbacks import TensorBoard, ModelCheckpoint, EarlyStopping
import csv
from time import time

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

        train_history = model.fit(train, label, epochs=epochs, batch_size=batch_size,verbose=2,
                                  callbacks=[tb_hist,cb_checkpoint,cb_early_stopping], validation_data=(train_dev, label_dev))
        train_history_detail = train_history.history
        # model.save(self.model_path)

    def test(self,data_path, output_path):
        data_list, id_list = self.dataLoader.test_loader(data_path)

        model = load_model(self.model_path)
        yhat = model.predict_classes(np.array(data_list))

        collect_count = 0
        collect_detail = [0,0]
        f = open(output_path,"w",encoding="utf-8",newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Id","SalePrice"])
        for inex, label in enumerate(yhat):
            csv_writer.writerow([id_list[0], label])

        f.close()

if __name__ == "__main__":
    mode = "test"
    model_path = "../data/model"
    if mode == "test":
        model_path = "../data/model/02-31412421973.3333.hdf5"
        dataPath = "../data/test.csv"
        train = ClassificationTrain(model_path)
        train.test(dataPath,"../data/submission.csv")
    elif mode == "train":

        train = ClassificationTrain(model_path)
        epoch = 100000
        batch_size = 10
        lr = 0.01
        train_rate = 99
        train_path = "../data/train.csv"

        train.train(epoch,batch_size,lr,train_path,train_rate)