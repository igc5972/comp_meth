### PURPOSE: ASTP 720 (Computational Methods) HW #1 Pt. 1
### [Isabella Cox, Aug. 2020]

# Import Statements
from root_library import bisection, newton, secant


### [Task 2]
# Calculate FWHM of pseudo-isothermal sphere using root-finding Methods


'''
Variables for pseudo-isothermal sphere (pi_sphere):

    n0 -- central column density
    rc -- critical radius
'''

pi_sphere = lambda x : n0 * ( 1 + (x/rc)**2 )**(-1/2) - n0/2
