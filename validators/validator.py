
def patient_data_validator(features, values):
    """
    :param features: list of feature names
    :param values: list of values as float values
    :return list with boolean and message
    """
    keys = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
            'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

    if len(features) == 13 and len(values) == 13:
        for value in values:
            if isinstance(value, float) or isinstance(value, int):
                continue
            else:
                return [False, "Invalid data type for value. Must be a float or int."]
        for feature in features:
            if feature in keys:
                continue
            else:
                return [False, "Invalid key."]
        return [True, "validated"]
    else:
        return [False, "Missing required fields."]
