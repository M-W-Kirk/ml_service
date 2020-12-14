
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
        for column in [
            'FIPS',
            'MaxPrecipitation',
            'WindSwathRadii',
        ]:
            categorical_convert = self.encoders[column]
            input_data[column] = categorical_convert.transform(input_data[column])
        return input_data

    def predict(self, input_data):
        return self.model.predict_proba(input_data)

    def postprocessing(self, input_data):
        label = 'No'
        if input_data[1] > 0.5:
            label = 'Yes'
        return {"probability": input_data[1], 'label': label, 'status': 'OK'}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0] # ONLY 1 SAMPLE!!!
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {'status': 'Error', 'message': str(e)}

        return prediction



#---END------------------------------------------