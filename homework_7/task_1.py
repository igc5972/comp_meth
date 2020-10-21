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
#accepts an estimate for DelI and a single x-value to evaluate function model at
def f(x, DelI):
    if x < t_ref:
        return 1
    elif t_ref <= x <= t_ref + tau:
        return 1 - DelI
    elif x > t_ref + tau:
        return 1


#distribution (likelihood)
#accepts x, y data points and an estimate for DelI
def p(xs, ys, DelI):
    sum = 0
    for x, y in zip(xs, ys):
        sum += -0.5 * (y - f(x, DelI))**2
    l = np.log(1/np.sqrt(2*np.pi)) + sum
    lexp = np.exp(l)
    return lexp


################################################################################
### Define Metropolis-Hastings function
################################################################################


#Uniform distribution on [0, 1]
def uniform():
    return np.random.uniform(0, 1)


#Proposal distribution (normal) centered at mean of DelI
def proposal(x):
    return np.random.normal(loc = x, scale = 0.001)




def metropolis_hastings(p, max_iter = 100):
    counter = max_iter
    X = 0.007 #DelI

    outcomes = np.zeros(max_iter)

    for i in range(max_iter):

        Y = proposal(X)

        ratio = p(date, flux, Y) / float(p(date, flux, X))
        if ratio >= 1:
            X_t = Y

        else:
            U = uniform()
            if U <= ratio: #accept Y
                X_t = Y

            else: #Reject Y
                X_t = X

        if X_t < 0: #ignore case of negative value
            continue

        X = X_t

        outcomes[i] = X


        #Print out for impatient user
        print(counter)
        counter -= 1

    return outcomes




outcomes = metropolis_hastings(p, max_iter = 100)

################################################################################
### Plot outcome values for Delta I
################################################################################

n, bins, patches = plt.hist(x=outcomes, bins = 15, color = 'lightgreen')
plt.title(r'$Distribution \ of \ \Delta I$')
plt.xlabel(r'$\Delta I$')
plt.ylabel('Frequency')
plt.show()

print("Mean: " + str(np.mean(outcomes)))
print("Std: " + str(np.std(outcomes)))
