import csv
from collections import Counter
import pandas as pd
import sklearn
from imblearn.over_sampling import ADASYN, RandomOverSampler


def preprocessing_columns(dataset_type):
    data = pd.read_csv(f'../machine_learning/data/{dataset_type}.csv')

    age = list(data['age'])
    sex = list(data['sex'])
    cp = list(data['cp'])
    trestbps = list(data['trestbps'])
    chol = list(data['chol'])
    fbs = list(data['fbs'])
    restecg = list(data['restecg'])
    thalach = list(data['thalach'])
    exang = list(data['exang'])
    oldpeak = list(data['oldpeak'])
    slope = list(data['slope'])
    ca = list(data['ca'])
    thal = list(data['thal'])
    target = list(data['target'])

    # Creating 'x' and 'y'
    x = list(zip(age, sex, cp, trestbps, chol, fbs, restecg,
                 thalach, exang, oldpeak, slope, ca, thal, target))
    y = list(target)

    return x, y


def write_data(x, y, dataset_type):
    headers = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope",
               "ca", "thal", "target"]
    rows = []

    for i in range(len(x)):
        row = list(x[i])
        row.append(int(y[i]))
        rows.append(dict(zip(headers, row)))

    filename = f"../data/{dataset_type}.csv"

    with open(filename, 'w', newline="") as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=headers)
        csvwriter.writeheader()
        csvwriter.writerows(rows)


def create_oversample():
    x, y = preprocessing_columns("data_ROS")

    # ADASYN
    dataset_type = "data_ADASYN_2"
    x_resampled, y_resampled = ADASYN().fit_resample(x, y)
    print(dataset_type, sorted(Counter(y_resampled).items()))
    write_data(x_resampled, y_resampled, dataset_type)

    # Random over sampler
    dataset_type = "data_ROS_2"
    ros = RandomOverSampler()
    x_resampled, y_resampled = ros.fit_resample(x, y)
    print(dataset_type, sorted(Counter(y_resampled).items()))
    write_data(x_resampled, y_resampled, dataset_type)


# create_oversample()
