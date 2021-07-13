import pandas
import numpy
import matplotlib.pyplot as plt

def scatter_plot(dataframe, dimension_x, dimension_y):
    colors = {'pos': 'r', 'neg': 'g'}
    for idx, row in dataframe.groupby('diabetes'):
        plt.scatter(row[dimension_x], row[dimension_y], color=[colors[r] for r in row['diabetes']], label=idx)
    plt.legend()
    plt.show()

def read_datasets(dataset_name):
    data = pandas.read_csv(dataset_name, sep = ',')
    data = data.dropna()
    training_set, validation_set = numpy.split(data, [int(.8 * len(data))])
    return data, training_set, validation_set

if __name__ == "__main__":
    data, training_set, validation_set = read_datasets('diabetes.csv')
    scatter_plot(data, "age", "pregnant")
