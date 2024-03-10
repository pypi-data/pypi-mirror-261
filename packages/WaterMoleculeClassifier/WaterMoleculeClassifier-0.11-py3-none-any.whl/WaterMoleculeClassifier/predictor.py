import joblib

class StatePredictor:
    def __init__(self):
        self.model = joblib.load('models/rf_trained_model.joblib')

    def predict_state(self, input_features):
        return self.model.predict(input_features)
