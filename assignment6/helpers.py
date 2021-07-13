"""
Small helpers for code that is not shown in the notebooks
Modified from https://github.com/UiO-IN3110/UiO-IN3110.github.io/blob/master/lectures/12_scikit_learn/fig_code/helpers.py?fbclid=IwAR2JIcwFwdNfpbxeCDVejuqHdC1HpPnD3zFFRT5LFFZQoBBwrETxA8D4LK4
"""

from sklearn import neighbors, datasets, linear_model
import pylab as pl
import numpy as np
from matplotlib.colors import ListedColormap

# Create color maps for 3-class classification problem, as with iris
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00'])

def plot_dataset(classifier, dataset, target, features):
    # Assumes classifier is fitted
    X = dataset[features].values
    y = dataset[target].values

    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.figure()
    pl.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    pl.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    pl.xlabel(features[0])
    pl.ylabel(features[1])
