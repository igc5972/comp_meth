### PURPOSE: ASTP 720 (Computational Methods) HW #6
### Task 1, 2

##############################################################################
## Import Statements
##############################################################################

import numpy as np
from matplotlib import pyplot as plt


##############################################################################
## For Pretty Plotting later on
##############################################################################

params = {'font.family':  'serif',
         'legend.fontsize': 'large',
         'figure.figsize': (10, 6),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}

plt.rcParams.update(params)



##############################################################################
## Import data from text file
##############################################################################

#for V-band
mv, P, ratio, excess, dist = np.loadtxt('cepheid_data.txt', unpack = True, skiprows = 1, \
                         delimiter = ',', usecols = (3, 1, 8, 7, 2))


##############################################################################
## Building the matrices and vectors for Least Squares
##############################################################################

#calculate the absolute magnitude
Av = [3.1 * e for e in excess]
Mv = [m - 5*np.log10(d) + 5 - a for m, d, a in zip(mv, dist, Av)]


#Equation: M = a + b * log10(P) + g * ratio

#Setup columns for design matrix
col1 = np.array([1 for i in range(len(P))])
col2 = np.array([np.log10(i) for i in P])
col3 = np.array([i for i in ratio])

#Setup y = X*theta
#theta = [alpha, beta, gamma]
x = np.column_stack([col1, col2, col3])
y = np.array([i for i in Mv]).reshape(len(Mv), 1)



##############################################################################
## Calculate values and uncertainties on parameters (Task 1)
##############################################################################

#calculate value of parameter vector
theta = np.dot(np.linalg.inv(np.dot(x.T, x)), np.dot(x.T, y))

theta_err = np.zeros((3, 1))  #initialize

#populate theta_err array with the errors on parameters
for i in range(len(theta_err)):
    theta_err[i] = np.linalg.inv(np.dot(x.T, x))[i][i]

#these hold the values and errors of the parameters
alpha = [theta[0], theta_err[0]]
beta =  [theta[1], theta_err[1]]
gamma = [theta[2], theta_err[2]]


##############################################################################
## Plot  the fit against the data (Task 2)
##############################################################################

#function for the fit line (exclude gamma component)
def fit(xvals, ratio = ratio, alpha = alpha[0][0], beta = beta[0][0]):
    y = alpha + beta * xvals
    return(y)

xvals = np.linspace(min(np.log10(P)), max(np.log10(P)), len(P))
yvals = fit(xvals)

plt.gca().invert_yaxis() #flip y-axis order bc of how magnitudes work

#scatter data
plt.scatter(np.log10(P), Mv, color = 'k', label = 'data')

#plot best-fit line
plt.plot(xvals, yvals, color = 'red', label = 'least squares fit')


#label plot
plt.xlabel('log(Period) [days]')
plt.ylabel(r'$M_V$')
plt.title('PLZ Relation of Cepheids')
plt.legend()
plt.show()
#plt.savefig('plz_relation.eps')
