### PURPOSE: ASTP 720 (Computational Methods) HW #1 Pt 2.
### [Isabella Cox, Aug. 2020]

# Import Statements
import numpy as np
from matplotlib import pyplot as plt
import interpolate


### [Task 6]


# Set up universal plotting formats (text size and such)

params = {'font.family':  'serif',
         'legend.fontsize': 'small',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'medium',
         'ytick.labelsize':'medium'}

plt.rcParams.update(params)



# Open the data points from a text file and save them as arrays

x, y = np.loadtxt('lens_density.txt', delimiter = ',', unpack = True, skiprows = 1)



# Visualize the data

plt.scatter(x, y, color = 'k')
plt.xlabel('x')
plt.ylabel(r'$N_e (x)$')
plt.title('Raw Data')
#plt.savefig('raw_data.eps')
#plt.show()



# Perform interpolation on the data

func_interp = interpolate.interpolate(x, y)
halfs = np.arange(0.5, x[-1], 1) #x-values to interpolate at

print(func_interp(halfs))
new_ys = func_interp(halfs) #new y-values


#Visualize interpolated points and original data Points

plt.scatter(x, y, color = 'k', label = 'Raw Data')
plt.scatter(halfs, new_ys, color = 'r', marker = '^', label = 'Interpolated')
plt.xlabel('x')
plt.ylabel(r'$N_e (x)$')
plt.title('Raw Data with Interpolated Points')
plt.legend()
#plt.savefig('interp_data.eps')
plt.show()
