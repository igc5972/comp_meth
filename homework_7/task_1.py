### PURPOSE: ASTP 720 (Computational Methods) HW #7 Pt. 1

################################################################################
### Import Statements
################################################################################

import numpy as np
from matplotlib import pyplot as plt


##############################################################################
## For Pretty Plotting later on
##############################################################################

params = {'font.family':  'serif',
         'legend.fontsize': 'large',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}

plt.rcParams.update(params)


################################################################################
### Open data of galaxy's initial position (and plot light curve)
################################################################################

file = 'lightcurve_data.txt'

date, flux = np.loadtxt(file, skiprows = 18, unpack = True)


'''
# Plot the lightcurve

plt.title('Lightcurve of KPLR8191672')
plt.xlabel('Time (HJD)')
plt.ylabel('De-trended normalized flux')
plt.scatter(date, flux, color = 'k', s = 3)
plt.show()
'''


################################################################################
### Fold the light curve
################################################################################

folded_date = np.zeros_like(date)
t0 = date[0]
P = 3.5485
for t in range(len(date)):
    folded_date[t] = (date[t] - t0) % P


'''
# Plot the folded lightcurve

plt.title('Folded Lightcurve of KPLR8191672')
plt.xlabel('Phase (days)')
plt.ylabel('Folded flux')
plt.scatter(folded_date, flux, color = 'k', s = 3)
plt.show()
'''


################################################################################
### Define function to model folded light curve
################################################################################

#measured by eye (I know....)
t_ref = 2.25
tau = 0.22


#provides functional values of boxcar fit at each time (also given DelI)
def f(x, DelI):
    if x < t_ref:
        return 1
    elif t_ref <= x <= t_ref + tau:
        return 1 - DelI
    elif x > t_ref + tau:
        return 1


#distribution (likelihood)
def p(x, y, DelI):
    return (1 / np.sqrt(2*np.pi)) * np.sum(np.exp(-0.5 * (y - DelI)**2))



################################################################################
### Define Metropolis-Hastings function
################################################################################


#Uniform distribution on [0, 1]
def uniform():
    return np.random.uniform(0, 1)


#Proposal distribution (normal) centered at mean of DelI
def proposal(x):
    return np.random.normal(loc = x, size = 1)


def metropolis_hastings(p, max_iter = 10000):

    X = 0 #DelI

    outcomes = []

    for i in range(max_iter):

        Y = proposal(X)
        Y = Y[0]


        ratio = p(date, flux, Y) / float(p(date, flux, X))

        print(ratio)
        if ratio >= 1:
            X_t = Y

        else:

            U = uniform()

            if U <= ratio: #accept Y
                X_t = Y

            else: #Reject Y
                X_t = X

        #if X_t < 0: #ignore case of negative value
        #    continue

        X = X_t
        print(X)
        outcomes.append(X)

    return outcomes


outcomes = metropolis_hastings(p, max_iter = 10000)


################################################################################
### Plot outcome values for Delta I
################################################################################


# An "interface" to matplotlib.axes.Axes.hist() method
n, bins, patches = plt.hist(x=outcomes, bins = 50)


plt.show()
