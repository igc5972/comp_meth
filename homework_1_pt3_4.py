### PURPOSE: ASTP 720 (Computational Methods) HW #1 Pt. 3 and 4
### Solve lens equation  for values of x-prime for different lenses
### [Isabella Cox, Aug. 2020]

# Import Statements
from root_library import bisection, newton, secant
import math ##for pi



### TASK 3: Gaussian Lens

# Lens Parameters

D = 3.086E21    # 1 kpc
a = 1.496E13    # 1 AU
wave = 21       # 21 cm
N0 = 3.09E16    # 0.01 pc cm^{-3}
re =  2.8E-13   #e^2/(m^e c ^2)




xplain = []
for p in xprime:
    func = x * (1 + ((wave**2 * re * N0 * D)/(math.pi() * a^^2))*e^(-x/a)**2) - p
    xplain.append(bisection(func))




### TASK 4: Pseudo-Isotermal lens

# Additional lens Parameters

rc = 1.496E13
