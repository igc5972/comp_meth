### PURPOSE: ASTP 720 (Computational Methods) HW #1 Pt. 2
### Calculate FWHM of pseudo-isothermal sphere using root-finding Methods
### [Isabella Cox, Aug. 2020]

# Import Statements
import numpy as np
from root_library import bisection, newton, secant
from matplotlib import pyplot as plt


# Setup for plotting later
params = {'font.family':  'serif',
         'legend.fontsize': 'small',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'medium',
         'ytick.labelsize':'medium'}

plt.rcParams.update(params)


#def a = x/r_c

# Function to find the roots of
pi_sphere = lambda a : ( 1 + (a)**2 )**(-1/2) - 1/2


# Function for finding iterations as function of threshold
# Run separate for diferent functions because of different accepted parameters
def interations(thresholds, function, a = None, b = None, xn = None):
    iteras = []
    new_values = []
    if function == bisection or function == secant:
        for t in thresholds:
            new_value, iter = function(pi_sphere, a, b, thresh=t, pr = True)
            new_values.append(new_value)
            iteras.append(iter)
        return(new_values, iteras)

    elif function == newton:
        for t in thresholds:
            new_value, iter = function(pi_sphere, xn, thresh=t, pr = True)
            new_values.append(new_value)
            iteras.append(iter)
        return(new_values, iteras)

    else:
        return("Error in choosing function")



#Threshold array to evaluate on
thresholds = np.linspace(1E-4, 0.1, 10000)


# Method 1: Bisesction
b_values, b_iteras = interations(thresholds, bisection, a = 0, b = 3)


# Method 2: Newton
n_values, n_iteras = interations(thresholds, newton, xn = 2)


# Method 3: Secant
s_values, s_iteras = interations(thresholds, secant, a = 0, b = 3)

method_iteras = [b_iteras, n_iteras, s_iteras]
names = ['Bisection', 'Newton', 'Secant']


#Plotting

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12,5))

    for idx, (row, m, name) in enumerate(zip(ax, method_iteras, names)):
        row.set_xscale('log')
        row.set_xlim(10E-6, 10E-1)
        row.set_ylim(0, 15)
        row.set_xlabel('Threshold')
        row.set_title(name)
        row.scatter(thresholds, m, color = 'k', s = 5)

        if idx == 0: #only label y-axis for left-most subplot
            row.set_ylabel('Number of Iterations')

    plt.subplots_adjust(top=0.85)
    plt.suptitle('Root-Finding Iterations vs. Threshold', fontsize = 16)
    plt.show()
