import joblib
from pkg_resources import resource_filename

class StatePredictor:
    def __init__(self):
        model_path = resource_filename(__name__, 'models/rf_trained_model.joblib')
        self.model = joblib.load(model_path)

    def predict_state(self, input_features):
        return self.model.predict(input_features)
