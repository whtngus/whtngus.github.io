# -*- coding: utf_8 -*-
import sys
import csv
import numpy as np
import pandas as pd
import os
from utils.Utils import Utils

class DataLoader:
    def train_loader(self,train_path,train_rate):
        # 모든 데이터 붙이기
        train = pd.read_csv(train_path)
        utils = Utils(train)
        data_list = utils.run()
        label_list = train["SalePrice"].values

        train_len = int((len(data_list) / 100) * train_rate)

        train = data_list[:train_len]
        train_dev = data_list[train_len:]
        label = label_list[:train_len]
        label_dev = label_list[train_len:]

        return train, label, train_dev, label, label_dev

    def test_loader(self,test_path):
        # 모든 데이터 붙이기
        test = pd.read_csv(test_path)
        utils = Utils(test)
        data_list = utils.run()
        id_list = test["Id"].values
        return data_list, id_list


if __name__ == "__main__":
    dataLoader = DataLoader()
    train_path = "../../data/train.csv"
    train_rate = 99
    train_input, train_label = dataLoader.train_loader(train_path,train_rate)