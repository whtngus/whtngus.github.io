import pandas as pd
import numpy as np

class Utils:
    def __init__(self,data):
        self.data = data

    def run(self):
        one_hot_list = ["MSSubClass", "MSZoning", "Street", "Alley", "LotShape", "LandContour","LotConfig","LandSlope","Neighborhood"
            ,"Condition1","Condition2","BldgType","HouseStyle","OverallQual","OverallCond","RoofStyle","RoofMatl","Exterior1st"
                        ,"Exterior2nd", "MasVnrType","ExterQual","ExterCond","Foundation","BsmtQual","BsmtCond","BsmtExposure",
                        "BsmtFinType1","BsmtFinType2","BsmtFinSF2","BsmtUnfSF","Heating","HeatingQC","CentralAir","Electrical",
                        "KitchenQual","Functional","FireplaceQu","GarageType","GarageFinish","GarageQual","GarageCond","PavedDrive",
                        "PoolQC","Fence","MiscFeature","SaleType","SaleCondition"
                        ]
        sqrt_list = ["LotFrontage","YearRemodAdd","MasVnrArea","BsmtFinSF1","BsmtUnfSF","TotalBsmtSF","1stFlrSF","2ndFlrSF",
                     "LowQualFinSF","GrLivArea","BsmtFullBath","BsmtHalfBath","FullBath","HalfBath","GarageYrBlt","GarageArea"
                     ,"WoodDeckSF","OpenPorchSF","EnclosedPorch","YrSold"
                     ]
        self.set_onehots(one_hot_list)
        # self.set_sqrt(sqrt_list)
        self.set_normals(sqrt_list)
        self.set_ConstructionAge()

        target_list = ["ConstructionAge","YearBuilt","YearRemodAdd","YrSold","TotRmsAbvGrd","Fireplaces","GarageCars","3SsnPorch",
                       "ScreenPorch","PoolArea","MiscVal","MoSold"]

        target_list = target_list + one_hot_list + sqrt_list
        return self.data[target_list].values

    def set_ConstructionAge(self):
        self.data["ConstructionAge"] = self.data['YrSold'] - self.data['YearBuilt']

    def set_remove(self,remove_list):
        '''
         해당 컬럼들 제거
        :param remove_list: 제거해야할 컬럼 리스트
        '''
        self.data = self.data.drop(remove_list,axis=1)

    def set_onehots(self,one_hot_list):
        '''
         onehot 으로 교체
         :param one_hot_list : one_hot_encoding으로 변경할 리스트 목록
        :return:
        '''
        for lists in one_hot_list:
            self.data = self.one_hot(self.data,lists)

    def set_sqrt(self,sqrt_list):
        '''
         제곱근으로 변경
        :param sqrt_list: 변경대상 컬럼 리스트
        :return:
        '''
        for lists in sqrt_list:
            self.data = self.sqrt(self.data,lists)

    def set_normals(self,sqrt_list):
        '''
         제곱근으로 변경
        :param sqrt_list: 변경대상 컬럼 리스트
        :return:
        '''
        for lists in sqrt_list:
            self.data = self.normal(self.data,lists)


    def sqrt(self,data,columns):
        '''
         행당 컬럼을 제곱근 형식으로 변경
        :param data: pandas 형 데이터
        :param columns: 대상 컬럼명
        :return:
        '''
        data[columns] = np.sqrt(data[columns]).fillna(0.0)
        return data

    def normal(self,data,columns):
        '''
        해당 컬럼을 정규화
        :param data:
        :param columns:
        :return:
        '''
        # 0으로 값 채우기
        data[columns] = data[columns].fillna(0.0)
        # 평균으로 값 채우기
        # data[columns].fillna(data[columns].mean(), inplace=True)
        data[columns] = (data[columns] - data[columns].mean())/data[columns].std()
        return data

    def one_hot(self,data,columns):
        '''
            onehot으로 변경
        :param data: pandas 형 데이터
        :param columns: 대상 컬럼명
        :return:
        '''
        data[columns] =  pd.get_dummies(data[columns])
        return data

