import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, make_scorer
import pickle


def fit_eval_model(model, train_features, y_train, test_features, y_test):
    results = {}
    # Train the model
    model.fit(train_features, y_train)
    # Test the model
    train_predicted = model.predict(train_features)
    test_predicted = model.predict(test_features)
    score = metrics.accuracy_score(y_test, test_predicted)

    # Classification report and Confusion Matrix
    results['classification_report'] = classification_report(y_test, test_predicted)
    results['confusion_matrix'] = confusion_matrix(y_test, test_predicted)
    results['accuracy score'] = score
    print("Score", score)

    # Saving models as pickle files
    file = open(f"../machine_learning/saved_ml_models/ROS/{model.__class__.__name__}.pickle", "wb")
    pickle.dump(model, file)

    return results


def main_loop(X_train, X_test, y_train, y_test):
    # Initialize the models
    sv = SVC(random_state=1)
    rf = RandomForestClassifier(random_state=1)
    ab = AdaBoostClassifier(random_state=1)
    gb = GradientBoostingClassifier(random_state=1)
    nb = GaussianNB()

    # Fit and evaluate models
    results = {}
    for cls in [sv, rf, ab, gb, nb]:
        cls_name = cls.__class__.__name__
        results[cls_name] = {}
        results[cls_name] = fit_eval_model(cls, X_train, y_train, X_test, y_test)

    # Print classifiers results
    for result in results:
        print(result)
        print()
        for i in results[result]:
            print(i, ':')
            print(results[result][i])
            print()
        print('-----')
        print()


df = pd.read_csv('../machine_learning/data/data_ROS_2.csv')
df.head()

target = df['target']
features = df.drop(['target'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.1, random_state=42, shuffle=True)
main_loop(X_train, X_test, y_train, y_test)


