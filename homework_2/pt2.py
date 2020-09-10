### PURPOSE: ASTP 720 (Computational Methods) HW #2 Pt. 2
### Task 2
### [Isabella Cox, Sept. 2020]

# Import Statements
import numpy
import numpy as np #for natural log
from matplotlib import pyplot as plt #for plotting
from calculus_library import derivative, trapezoid

# Plotting Parameters for pretty plots

params = {'font.family':  'serif',
         'legend.fontsize': 'large',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}

plt.rcParams.update(params)


###############################################################################
### calculate M_enc(r) and plot
###############################################################################

def pt1(c, v200):

    '''
    Input:

    c -- value variable (supplied)
    v200 -- value variable (supplied)
    plot -- boolean flag for if user wants to plot

    Output:

    prints plot of M_enc vs. r, can save plot (if plot = True)
    returns function for M_enc to use in other places
    '''


    # initialize r values
    rs = np.linspace(0, 300, 10)

    # function for circular velocity: v_c
    def v_c(r, c, v200, r200):
        return ((v200**2 / (r/r200)) * ((np.log(1 + c*(r/r200)) \
        - (c*(r/r200))/(1+c*(r/r200)))/(np.log(1+c) - (c)/(1+c))))**0.5

    # function for enclosed mass
    m_enc = lambda r: r * v_c(r, c, v200, r200) / G

    return(m_enc)


###############################################################################
### calculate M of dark matter halo
###############################################################################

def pt2(m_enc):

    '''
    Input:

    m_enc -- function to calculate enclosed mass at radius r

    Output:

    mass -- integrated mass enclosed from 0 --> big # (inf)
    '''

    mass = trapezoid(m_enc, 1E-4, 1E20)
    print(mass)


###############################################################################
### calculate M(r), amt. of mass in a shell around r +/- dr
###############################################################################

def pt3(m_enc, dr = 1E-4):

    '''
    Input:

    m_enc -- function to calculate enclosed mass at radius r
    dr    -- +/- amt. around pt. r to construct shell

    Output:

    shell_mass -- function that gives M(r) for a given r
    '''

    shell_mass = lambda r : trapezoid(m_enc, 1E-4, r+dr) \
                            - trapezoid(m_enc, 1E-4, r-dr)

    return(shell_mass)


###############################################################################
### calculate dM/dr
###############################################################################

def pt4(shell_mass):

    '''
    Input:

    shell_mass -- function to calculate enclosed mass at radius r


    Output:

    d_shell_mass -- function that gives dM/dr for a given r
    '''

    d_shell_mass = lambda r : derivative(shell_mass, r)

    return(d_shell_mass)



###############################################################################
### the actual running of code
###############################################################################


# Constant constants
r200 = 230       # kpc
G = 6.67E-20     # km^3 / s^2 / kg


# Run 1 constants
v200 = 160       # km / s
c = 15           # constant


me_1 = pt1(c, v200)
shell_1 = pt3(me_1)
dshell_1 = pt4(shell_1)




# Run 2 constants
v2002 = 300       # km / s
c2 = 15           # constant

me_2 = pt1(c2, v2002)
shell_2 = pt3(me_2)
dshell_2 = pt4(shell_2)



# Run 3 constants
v2003 = 160       # km / s
c3 = 4            # constant

me_3 = pt1(c3, v2003)
shell_3 = pt3(me_3)
dshell_3 = pt4(shell_3)



###############################################################################
### plotting: M_enc
###############################################################################


r = np.linspace(1, 300, 30)


fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, sharey = 'row',figsize = (14, 6))

ax1.scatter(r, me_1(r), color = 'k')
ax2.scatter(r, me_2(r), color = 'k')
ax3.scatter(r, me_3(r), color = 'k')


ax1.set_ylabel('Mass enclosed [kg]')
ax1.set_xlabel('Outer radius [kpc]')
ax2.set_xlabel('Outer radius [kpc]')
ax3.set_xlabel('Outer radius [kpc]')

ax1.set_yscale('log')
ax2.set_yscale('log')
ax3.set_yscale('log')


ax1.set_title(r'$c = 15, v_{200} = 160$')
ax2.set_title(r'$c = 15, v_{200} = 300$')
ax3.set_title(r'$c = 4, v_{200} = 160$')


plt.suptitle('Enclosed Mass as a Function of Radius', fontsize = 'xx-large')
#plt.savefig('enclosed_masses.eps')
#plt.show()




###############################################################################
### plotting: M(r)
###############################################################################

r = np.linspace(1, 300, 30)


fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, sharey = 'row',figsize = (14, 6))

ax1.scatter(r, [shell_1(i) for i in r], color = 'k')
ax2.scatter(r, [shell_2(i) for i in r], color = 'k')
ax3.scatter(r, [shell_3(i) for i in r], color = 'k')

ax1.set_ylim(1E17, 1E22)
ax1.set_ylabel('M(r)')
ax1.set_xlabel('Radius [kpc]')
ax2.set_xlabel('Radius [kpc]')
ax3.set_xlabel('Radius [kpc]')

ax1.set_yscale('log')
ax2.set_yscale('log')
ax3.set_yscale('log')


ax1.set_title(r'$c = 15, v_{200} = 160$')
ax2.set_title(r'$c = 15, v_{200} = 300$')
ax3.set_title(r'$c = 4, v_{200} = 160$')


plt.suptitle(r'$M(r) \ for \ r \pm 1 \times 10^{-4} kpc$', fontsize = 'xx-large')
plt.show()


###############################################################################
### plotting: dM/dr
###############################################################################

r = np.linspace(1, 300, 10)


fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, sharey = 'row',figsize = (14, 6))

ax1.scatter(r, [dshell_1(i) for i in r], color = 'k')
ax2.scatter(r, [dshell_2(i) for i in r], color = 'k')
ax3.scatter(r, [dshell_3(i) for i in r], color = 'k')


ax1.set_ylabel('dM/dr')
ax1.set_xlabel('Radius [kpc]')
ax2.set_xlabel('Radius [kpc]')
ax3.set_xlabel('Radius [kpc]')

ax1.set_yscale('log')
ax2.set_yscale('log')
ax3.set_yscale('log')


ax1.set_title(r'$c = 15, v_{200} = 160$')
ax2.set_title(r'$c = 15, v_{200} = 300$')
ax3.set_title(r'$c = 4, v_{200} = 160$')


plt.suptitle('dM/dr', fontsize = 'xx-large')
plt.show()
