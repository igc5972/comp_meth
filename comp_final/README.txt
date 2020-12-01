**NOTE: Many of the mechanics described here were explained in the writeup.pdf


===============================================================================
CODE #1: sim_data.py
===============================================================================

This code creates simulated color-mass data to use. Output data is formatted as:
|feature_1|feature_2|label| where the features as the mass and magnitude


===============================================================================
CODE #2: log_reg.py
===============================================================================

The code is numbered with comments [1] - [3], and I will use that convention to
refer to parts of the code throughout.


[1]
Here I define all of the functions that I will call as part of the main code 
later on. I define a sigmoid function, which accepts a single value and
calculates the corresponding functional value. I also define the cost function
and a function for the gradient, which were described in the writeup. I also define
a function that accepts finalized theta values to cast classification predictions
for each galaxy. And finally, I define functions to plot the data with the
decision boundary and to output a formatted confusion matrix.


[2]
This is the main body of the code. First we construct some basics:

X = features (this is a 2d array) y = labels
m = number of points
k = number of features


Before we can run our code, we need to clarify what our theta parameters are.
We need one for each feature, and then we need an third additional one for the
y-intercept. To represent that, I appended a third column to the features
array initialized of all “1s” to go through the crank.

To determine the final weights (thetas), we go through many iterations, and T
for each step, we first calculate a value, z = transpose(theta)*X . Then, we
calculate the functional value with our predictor function (the sigmoid
function), for each z value. Finally, we compute the gradient for this step and
then adjust all the theta values which are decreased by a pre-determined learning
rate times the gradient.

The last part of this step, once many iterations have occurred, we assume the
theta values are settled and run a function call to the make predictions
described in point 2. The accepted parameters for this main function include the
features, labels, and some optional parameters, such as the number of iterations
to run (default = 100,000) the learning rate (default = 0.1) and some Boolean
flags for the user to decide if they want to periodically print the cost
(to ensuring it is decreasing still) and output the plot and confusion matrix.


[3]
This is where the user would setup their data and actual call the main
function with their data and optionally decide what visualizations to 
output.
