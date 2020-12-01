
#---START----------------------------------------
# file backend/server/apps/ml/income_classifier/random_forest.py
import joblib as jl 
import pandas as pd 

class RandomForestClassifier:
    def __init__(self):
        path_to_artifiacts = "../../research/"
        self.values_fill_missing = jl.load(path_to_artifiacts + "train_mode.joblib")
        self.encoders = jl.load(path_to_artifiacts + "encoders.joblib")
        self.model = jl.load(path_to_artifiacts + "random_forest.joblib") 

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame:
        input_data = pd.DataFrame(input_data, index = [0])
        # fill missing values:
        input_data.fillna(self.values_fill_missing)
        # convert categorical features:
        # for column in [] 


#---END------------------------------------------