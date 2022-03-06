import pickle
import numpy as np

model = pickle.load(open('saved_ml_models/ROS/voting_classifier.pickle', 'rb'))  # Load ML model


def list_to_dict(keys, values):
    """
    Convert lists to dictionary
    :param keys: list of keys
    :param values: list of values as floats
    :return: dictionary
    """

    res = {}
    for key in keys:
        for value in values:
            res[key] = value
            values.remove(value)
            break

    return res


def predict(features):
    """
    :param features: list of values as floats
    :return: result
    """

    array_features = [np.array(features)]  # Convert features to array
    prediction = model.predict(array_features)  # Predict features
    output = prediction

    if output == 1:
        res = {
            "result": 1,
            "message": 'The patient is not likely to have heart disease!'
        }
        return res, 200
    else:
        res = {
            "result": 2,
            "message": 'The patient is likely to have heart disease!'
        }
        return res, 200
