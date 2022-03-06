import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import plot_confusion_matrix, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


def run_voting_classifier():
    # Loading the dataset with a Pandas and the returned data frame is caught by data variable
    df = pd.read_csv('../machine_learning/data/data_ROS_2.csv')
    df.head()

    target = df['target']
    features = df.drop(['target'], axis=1)

    estimators = []
    for root, directories, files in os.walk(f"../machine_learning/saved_ml_models/ROS", topdown=False):
        for name in files:
            print(name)
            model = pickle.load(open(os.path.join(root, name), "rb"))
            estimators.append((name, model))
    print(estimators)
    voting_classifier(features, target, estimators)


def voting_classifier(x, y, estimators):
    results = {}
    for i in range(10):
        # Splitting the data into testing data and training data with the testing size of 0.3
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42, shuffle=True)
        vc_model = VotingClassifier(estimators=estimators, voting='hard', )
        vc_model.fit(X_train, y_train)

        # The accuracy score of the model
        score = vc_model.score(X_test, y_test)

        train_predicted = vc_model.predict(X_train)
        test_predicted = vc_model.predict(X_test)

        results['classification_report'] = classification_report(y_test, test_predicted)
        results['confusion_matrix'] = confusion_matrix(y_test, test_predicted)
        results['accuracy score'] = score

        # Saving models as pickle files
        file = open(f"../machine_learning/saved_ml_models/voting_classifier.pickle", "wb")
        pickle.dump(vc_model, file)

        print(score)


run_voting_classifier()
