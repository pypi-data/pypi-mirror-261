import joblib

class PredictState:
    def __init__(self):
        self.model = joblib.load('models/my_trained_model.pkl')

    def predict_state(self, input_features):
        return self.model.predict(input_features)
