import matplotlib.pyplot as plt
from fitting import fit
from fitting import create_classifier
from data import read_datasets
from helpers import plot_dataset

def visualize(classifier, training_set, dataset, target, features):
    classifier = fit(training_set, classifier, ["age", "pregnant"], "diabetes")
    plot_dataset(classifier, dataset, target, features)

if __name__ == '__main__':
    classifier = create_classifier("svc")
    data, training_set, validation_set = read_datasets("diabetes.csv")
    data.replace(["pos", "neg"], [1, 0], inplace=True)
    training_set.replace(["pos", "neg"], [1, 0], inplace=True)
    validation_set.replace(["pos", "neg"], [1, 0], inplace=True)
    classifier = create_classifier("svc")
    visualize(classifier, training_set, data, "diabetes", ["age", "pregnant"])
    plt.show()
