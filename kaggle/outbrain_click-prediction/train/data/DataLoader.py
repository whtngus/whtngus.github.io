# -*- coding: utf_8 -*-
import sys
import csv
import numpy as np
import pandas as pd
import os

class DataLoader:
    def __init__(self,events_path,promoted_content_path):
        self.promoted_content, self.events = self.default_data_set(promoted_content_path,events_path)

    def default_data_set(self,promoted_content_path,events_path):
        promoted_content = pd.read_csv(promoted_content_path)
        events  = pd.read_csv(events_path)
        return promoted_content, events

    def train_loader(self,clicks_train_path):
        data_list = []
        label_list = []

        # 모든 데이터 붙이기
        train = pd.read_csv(clicks_train_path,nrows=1000)
        train = pd.merge(train,self.promoted_content,on="ad_id")
        train = pd.merge(train,self.events,on="display_id")
        label_list = train["clicked"].values
        # 'display_id', 'ad_id', 'clicked', 'document_id_x', 'campaign_id',
        #        'advertiser_id', 'uuid', 'document_id_y', 'timestamp', 'platform',
        #        'geo_location'
        # 뽑아낼 수 있는 데이터 : timestamp, platform , geo_location
        train = train[["geo_location","platform","geo_location"]]

        print()


        data_list = np.array(data_list)
        return data_list, label_list



if __name__ == "__main__":
    events_path = "../data/events.csv"
    promoted_content_path = "../data/promoted_content.csv"
    dataLoader = DataLoader(events_path,promoted_content_path)
    clicks_train_path = "../data/clicks_train.csv"
    train_input, train_label = dataLoader.train_loader(clicks_train_path)