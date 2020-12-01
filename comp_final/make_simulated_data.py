### PURPOSE: ASTP 720 (Computational Methods) Final Project
### Produce simulated data log(color-mass) to run logistic regression code on
### [Isabella Cox, Nov. 2020]

##############################################################################
#Import statements
##############################################################################
import numpy as np
import matplotlib.pyplot as plt


##############################################################################
#Simulate some color-mass data as an example
##############################################################################
np.random.seed(12) #seed the random generator for debugging purposes

ndata = 1000

#simulate 1000 spiral galaxies
clump1 = np.random.multivariate_normal([8, 0], [[0.1, 1],[1, 0.1]], ndata)

#simulate 1000 elliptical galaxies
clump2 = np.random.multivariate_normal([10.5, 2.75], [[1, .5],[.75, 1]], ndata)


#features are (1) Mass and (2) Color
features = np.vstack((clump1, clump2))

#labels are 0 for clump1 (spirals) and 1 for clump2 (elliptical)
labels = np.hstack((np.zeros(ndata), np.ones(ndata)))


#save the data
np.savetxt('sim_data.txt', np.column_stack([features, labels]))


##############################################################################
#Plot this simulated data to visualize
##############################################################################
'''
## Test plotting
plt.scatter(clump1[:, 0], clump1[:, 1], color = 'blue', label = 'Spiral')
plt.scatter(clump2[:, 0], clump2[:, 1], color = 'red', label = 'Elliptical')
plt.xlabel(r'$Stellar \ Mass \ log \ M_* \ (M_{\odot})$', fontweight = 'bold')
plt.ylabel('u - r color', fontweight = 'bold')

plt.tick_params(axis="x", direction="in")
plt.tick_params(axis="y", direction="in")
'''
