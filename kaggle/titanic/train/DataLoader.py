# -*- coding: utf_8 -*-
import sys
import csv
import numpy as np

class DataLoader:
    def __init__(self,data_path,extract_data):
        self.data_path = data_path
        self.extract_data = extract_data

    def data_loader(self):
        '''
        대상파일을 읽어들임
        @:param data_list 읽어들일 데이터
        @:param onehot_path sign onehot 매칭할 데이터
        return 읽어들인 data, label
        '''
        label_list = []
        data_list = []
        try:
            with open(self.data_path, "r", encoding="utf-8") as data:
                targets = {}
                # lines = data.readlines()
                lines = csv.reader(data)

                for line in lines:
                    for index, data in enumerate(line):
                        if data in self.extract_data:
                            targets[data] = index
                    break

                for line in lines:
                    make_data = []
                    label_list.append(float(line[targets["Survived"]]))
                    make_data.append(float(line[targets["Pclass"]]))
                    make_data.append(1.0 if line[targets["Sex"]] =="female" else 0.0)
                    make_data.append(float(0 if line[targets["Age"]] == "" else line[targets["Age"]]))
                    make_data.append(float(line[targets["SibSp"]]))
                    make_data.append(float(line[targets["Parch"]]))
                    make_data.append(0 if len(line[targets["Ticket"]].split()) > 1 else 1)
                    make_data.append(0 if line[targets["Fare"]] =="" else float(line[targets["Fare"]]))
                    make_data.append(1 if line[targets["Cabin"]] == "" else 0)
                    make_data = make_data + ([1.0,0.0,0.0] if line[targets["Embarked"]] == "S" else [1.0,0.0,0.0] if line[targets["Embarked"]] == "C" else [0.0,0.0,1.0])
                    data_list.append(make_data)
        except FileNotFoundError as e:
            print("해당 파일이 존재하지 않습니다.")
            sys.exit(1)
        data_list = np.array(data_list)
        label_list = np.array(label_list)
        return data_list, label_list


if __name__ == "__main__":
    dataPath = "../data/train.csv"
    extract_data = ["Survived","Pclass","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]
    dataLoader = DataLoader(dataPath,extract_data)
    train_input, train_label = dataLoader.data_loader()