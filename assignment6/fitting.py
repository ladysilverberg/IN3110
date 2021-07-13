import pandas
import numpy
import argparse
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from data import read_datasets

def fit(training_set, classifier, features, target):
    X = training_set[features].values
    Y = training_set[target].values
    classifier.fit(X, Y)
    return classifier

def calculate_score(classifier, dataset, features, target):
    X = dataset[features].values
    Y = dataset[target].values
    pred = classifier.predict(X)
    score = accuracy_score(Y, pred)
    return score

def create_classifier(c_type):
    classifier = None
    if c_type == "svc":
        classifier = SVC(gamma="auto")
    elif c_type == "knn":
        classifier = KNeighborsClassifier()
    elif c_type == "gaussiannb":
        classifier = GaussianNB()
    return classifier

if __name__ == '__main__':
    # Parse Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-datafile", required=True, help="Dataset to use")
    parser.add_argument("-method", required=True, help="Classification Method")
    args = parser.parse_args()

    # Create Classifier
    classifier = create_classifier(args.method)

    # Read and fit data
    if classifier is not None:
        data, training_set, validation_set = read_datasets(args.datafile)
        data.replace(["pos", "neg"], [1, 0], inplace=True)
        training_set.replace(["pos", "neg"], [1, 0], inplace=True)
        validation_set.replace(["pos", "neg"], [1, 0], inplace=True)
        classifier = fit(training_set, classifier, ["age", "pregnant"], "diabetes")
        print("Score: " + str(calculate_score(classifier, validation_set, ["age", "pregnant"], "diabetes")))
    else:
        print("Invalid classification method!")
