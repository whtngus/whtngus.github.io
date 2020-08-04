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
                passinger_id = []
                for line in lines:
                    passinger_id.append(line[targets["PassengerId"]])
                    make_data = []
                    label_list.append(float(line[targets["Survived"]]))
                    make_data.append(float(line[targets["Pclass"]]))
                    make_data.append(1.0 if line[targets["Sex"]] =="female" else 0.0)
                    make_data.append(float(0 if line[targets["Age"]] == "" else line[targets["Age"]]))
                    make_data.append(0 if len(line[targets["Ticket"]].split()) > 1 else 1)
                    make_data.append(0 if line[targets["Fare"]] =="" else float(line[targets["Fare"]]))
                    make_data.append(self.dataset_family(float(line[targets["SibSp"]]),float(line[targets["Parch"]]) ))
                    make_data = make_data + self.dataset_cabin(line[targets["Cabin"]])
                    make_data = make_data + self.dataset_title(line[targets["Name"]])
                    make_data = make_data + ([1,0,0] if line[targets["Embarked"]] == "S" else [1,0,0] if line[targets["Embarked"]] == "C" else [0,0,1])
                    data_list.append(make_data)
        except FileNotFoundError as e:
            print("해당 파일이 존재하지 않습니다.")
            sys.exit(1)
        data_list = np.array(data_list)
        label_list = np.array(label_list)
        return data_list, label_list, passinger_id

    def dataset_cabin(self,cabin):
        '''
         cabin의 시작 알파벳에 따라 생존 확률이 다름
        :param cabin:
        :return:
        '''
        one_hot = [0,0,0,0,0,0,0,0,0,0]
        if cabin == "":
            one_hot[-1] = 1
            return one_hot
        match = ['A','B','C','D','E','F','G','T']
        for i,v in  enumerate(match):
            if v == cabin[0]:
                one_hot[i] = 1
                return one_hot
        one_hot[-1] = 1
        return one_hot

    def dataset_family(self,sibsp,parch):
        '''
        같이 탑승한 가족단위 수 반환
        :param sibsp:
        :param parch:
        :return:
        '''
        return sibsp + parch + 1

    def dataset_title(self,name):
        '''
        Mr Mrs Miss Master 의경우 생존 확률이 높음 나머지는 비슷비슷해서 기타처리
        :param name: 대상 Name
        :return:
        '''
        name = name.split(",")[1].split(".")[0].strip()
        if name == "Mr":
            return [1,0,0,0,0]
        elif name == "Mrs":
            return [0,1,0,0,0]
        elif name == "Miss":
            return [0,0,1,0,0]
        elif name == "Master":
            return [0,0,0,1,0]
        else:
            return [0,0,0,0,1]


if __name__ == "__main__":
    dataPath = "../data/train.csv"
    extract_data = ["Survived","Pclass","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked","PassengerId"]
    dataLoader = DataLoader(dataPath,extract_data)
    train_input, train_label = dataLoader.data_loader()