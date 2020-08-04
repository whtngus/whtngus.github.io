# one_hot_list = ["MSSubClass", "MSZoning", "Street", "Alley", "LotShape", "LandContour","LotConfig","LandSlope","Neighborhood"
# ,"Condition1","Condition2","BldgType","HouseStyle","OverallQual","OverallCond","RoofStyle","RoofMatl","Exterior1st"
#                 ,"Exterior2nd", "MasVMSSubClasnrType","ExterQual","ExterCond","Foundation","BsmtQual","BsmtCond","BsmtExposure",
#                 "BsmtFinType1","BsmtFinType2","BsmtFinSF2","BsmtUnfSF","Heating","HeatingQC","CentralAir","Electrical",
#                 "KitchenQual","Functional","FireplaceQu","GarageType","GarageFinish","GarageQual","GarageCond","PavedDrive",
#                 "PoolQC","Fence","MiscFeature","SaleType","SaleCondition"
#                 ]
# OverallQual
sqrt_list = ["YearRemodAdd", "MasVnrArea", "TotalBsmtSF", "LowQualFinSF", "GrLivArea", "FullBath", "GarageYrBlt"]
# sqrt_list = ["LotFrontage","YearRemodAdd","MasVnrArea","BsmtFinSF1","BsmtUnfSF","TotalBsmtSF","1stFlrSF","2ndFlrSF",
#              "LowQualFinSF","GrLivArea","BsmtFullBath","BsmtHalfBath","FullBath","HalfBath","GarageYrBlt","GarageArea"
#              ,"WoodDeckSF","OpenPorchSF","EnclosedPorch","YrSold"
#              ]

# target_list = ["ConstructionAge","YearBuilt","YearRemodAdd","YrSold","TotRmsAbvGrd","Fireplaces","GarageCars","3SsnPorch",
#                "ScreenPorch","PoolArea","MiscVal","MoSold"]
target_list = ["YearBuilt", "Fireplaces", "GarageCars"]


MSSubClass = ["20","30","40","45","50","60","70","75","80","85","90","120","150","160","180","190"]
Neighborhood = ["Blueste","BrDale","BrkSide","ClearCr","CollgCr","Crawfor","Edwards","Gilbert","IDOTRR",
                "MeadowV","Mitchel","Names","NoRidge","NPkVill","NridgHt","NWAmes",
                "OldTown","SWISU","Sawyer","SawyerW","Somerst","StoneBr","Timber","Veenker"]
OverallQual = ["10","9","8","7","6","5","4","3","2","1"]
ExterQual = ["Ex","Gd","TA","Fa","Po"]
Foundation = ["BrkTil","CBlock","PConc","Slab","Stone","Wood"]
BsmtQual = ["Ex","Gd","TA","Fa","Po","NA"]
KitchenQual = ["Ex","Gd","TA","Fa","Po"]
GarageFinish = ["Fin","RFn","Unf","NA"]

one_hot_list = {"MSSubClass" : MSSubClass,
                "Neighborhood" : Neighborhood,
                "OverallQual" : OverallQual,
                "ExterQual" : ExterQual,
                "Foundation" : Foundation,
                "BsmtQual" : BsmtQual,
                "KitchenQual" : KitchenQual,
                "GarageFinish" : GarageFinish}