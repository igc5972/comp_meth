### PURPOSE: ASTP 720 (Computational Methods) Final Project
### Logistic Regression for Color Bi-Modality of SDSS Galaxies
### [Isabella Cox, Nov. 2020]

################################################################################
#Import Statements
################################################################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #used for displaying confusion matrix


##############################################################################
#For Pretty Plotting later on
##############################################################################
params = {'font.family':  'serif',
         'legend.fontsize': 23,
         'figure.figsize': (10.5, 8.2),
         'axes.labelsize': 29,
         'axes.titlesize':29,
         'xtick.labelsize':25,
         'ytick.labelsize':25}

plt.rcParams.update(params)



################################################################################
# [1] Define Functions to Use (Sigmoid, Cost, Optimization, etc.)
################################################################################
def sigmoid(z):
    '''
    Accepts:
    z -- value or array (list) of values

    Returns:
    y -- functional values of sigmoid
    '''

    y = 1 / (1 + np.exp(-z))
    return y


def cost_function(h, y, m):
    '''
    Accepts:
    h -- y-predictions (hypothesis) for each value
    y -- actual labels for each data point

    Returns:
    l -- cost function (optimization objection)
    '''

    l = np.sum((-y * np.log(h)) - ((1-y) * np.log(1-h)))/m
    return l


def gradient(X, h, y, m):
    '''
    Accepts:
    X -- 2d array of x,y [features] values for all data points
    h -- y-predictions for each value
    y -- actual labels for each data points

    Returns:
    gradient of cost function
    '''

    return ((h - y) @ X)/m


def make_predictions(X, theta):
    '''
    Predicts a label (0 or 1) for each data point

    Accepts:
    X     -- 2d array of x,y [features] values for all data points
    theta -- model parameters

    Returns:
    prediction for each data point in list form
    '''

    preds = []
    z = X @ theta.T
    s = sigmoid(z)

    for i in range(len(X)):
        if s[i] >= 0.5:
            preds.append(1) #predicted elliptical
        else:
            preds.append(0) #predicted spiral

    return preds



def plot_boundary(features, labels, xs, ys):
    '''
    Accepts:
    features -- 2d array of features
    labels   -- actual labels for each data point
    xs       -- x-values over which to draw the decision boundary
    ys       -- y-values of the decision Boundary

    Returns:
    nothing --> but plots the points and the decision boundary
    '''

    clump1 = features[labels == 0.]
    clump2 = features[labels == 1.]

    plt.scatter(clump1[:, 0], clump1[:, 1], color = 'blue', label = 'Spiral')
    plt.scatter(clump2[:, 0], clump2[:, 1], color = 'red', label = 'Elliptical')

    plt.plot(xs,ys,color="k", lw = 5, label="Decision Boundary")
    plt.title('Color-Mass Diagram with Decision Boundary')
    plt.xlabel(r'$log(Stellar Mass[M\odot])$')
    plt.ylabel('u - r color')

    plt.legend()
    plt.show()



def confusion_matrix(y, k, m, predictions):
    '''
    Accepts:
    y           --  actual labels for each data point
    k           -- number of features
    m           -- number of original data points
    predictions -- prediction (0/1) for each datapoint

    Make confusion matrix:
     values in "a" squares are correctly predicted, "b" squares are wrong

      |   | 0 | 1 |
        _   _   _
      | 0 | a | b |
        _   _   _
      | 1 | b | a |
    '''

    actual = np.array(y).astype(int)
    predicted = np.array(predictions).astype(int)

    confusion_matrix = np.zeros((k, k))

    for i, j in zip(predicted, actual):
        confusion_matrix[i][j] += 1

    count = 0
    for i, j in zip(predicted, actual):
        if i == 1 and j == 0:
            count += 1

    #Percentage correctly predicted
    correct = (actual == predicted).sum() / float(m)

    labels = ['0', '1']
    print(" ")
    print("Confusion Matrix: ")
    print(" ")
    df = pd.DataFrame(confusion_matrix, index=labels, columns=labels)
    print(df)



################################################################################
# [2] Main body function
################################################################################
def main(features, labels, iterations = 100000, rate = 0.1, \
         print_cost = False, plot = True, show_matrix = True):
    '''
    Main body of code to call of the functions I wrote in the right place

    Accepts:
    features    -- 2d array of x,y [features] values for all data points
    labels      -- actual labels for each data points
    iterations  -- number of iterations
    rate        -- learning rate
    print_cost  -- user decides if to print out cost at intervals

    Returns:
    nothing --> makes various visualizations based on arguments passed by user
    '''

    X = features
    y = labels

    m = X.shape[0]  #number of points
    n = X.shape     #shape of feature array: (# of points, # of features)
    k = X.shape[1]  #number of features

    intercept = np.ones((m, 1))
    X = np.concatenate((intercept, X), axis=1)

    theta = np.zeros(1+k)  #weights

    count = 0
    for i in range(iterations):
        z = X @ theta.T
        h = sigmoid(z) #hypothesis
        grad = gradient(X, h, y, m)
        theta -= rate * grad

        if print_cost == True and i % 1000 == 0: #periodically print out cost
            if count == 0: #only print header on first loop
                print("Cost at regular intervals: ")
            count += 1
            cost = cost_function(h, y, m)
            print(cost)

    predictions = make_predictions(X, theta)

    xs = np.linspace(6, 12, 50)
    ys = -(theta[0] + theta[1]*xs)/theta[2]

    if plot == True:
        plot_boundary(features, labels, xs, ys)

    if show_matrix == True:
        confusion_matrix(y, k, m, predictions)



################################################################################
# [3] **RUN ME HERE** Open the data and call the main function
################################################################################
feature_1, feature_2, labels = np.loadtxt('sim_data.txt', unpack = True)
features = np.column_stack([feature_1, feature_2])

main(features, labels, iterations = 100000, rate = 0.1, \
     print_cost = True, plot = True, show_matrix = True)
