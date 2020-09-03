### PURPOSE: ASTP 720 (Computational Methods) HW #2 Pt. 1
### Numerical Calculus Functions (1 derivative mode, 3 integral modes)
### [Isabella Cox, Sept. 2020]



def derivative(f, x, h):

    '''
    Compute derivative of a function at a given value using the symmetric method

    Input values:

    f -- function of which to take the derivative
    x -- x-position to evaluate derivative at
    h -- incremental size

    Returns:

    f'(x) --  derivative f(x)
    '''

    return (f(x+h) - f(x-h))/2h





def midpoint(f, a, b, N):

    '''
    Compute integral of function between bounds using left edge riemann sums

    Input values:

    f -- function of which to integrate
    a -- left bound of region to integrate over
    b -- right bound of region to integrate over
    N -- number of intervals

    Returns:

    int(f(x)) from a to b
    '''

    dx = (b - a)/N

    x_leftpts = np.arange(a, b, dx) #x-values to evaluate y-values at
    y_leftpts = f(x_leftpts) #y-values of rectangle's left edges

    sum = 0 #initialize holder for answer

    for y in y_leftpts:
        sum = sum + y * dx

    return(sum)






def trapezoid(f, a, b, N):

    '''
    Compute integral of function between bounds using trapezoid rule

    Input values:

    f -- function of which to integrate
    a -- left bound of region to integrate over
    b -- right bound of region to integrate over
    N -- number of intervals

    Returns:

    int(f(x)) from a to b
    '''

    dx = (b - a)/N #base of trapezoid

    x_leftpts = np.arange(a, b, dx) #left points of sub-intervals
    x_rightpts = np.arange(a, b+dx, dx)

    sum = 0 #initialize integral sum
    for l, r in zip(x_leftpts, x_rightpts):
        sum += (f(l) + f(r)) * dx / 2 #compute integral of each interval

    return(sum)








def simpsons(f, a, b, N):

    '''
    Compute integral of function between bounds using Simpson's rule

    Input values:

    f -- function of which to integrate
    a -- left bound of region to integrate over
    b -- right bound of region to integrate over
    N -- number of intervals (must be evenly divisible by 2)

    Returns:

    int(f(x)) from a to b
    '''

    #Check that N is even

    if N % 2 != 0:
        return('Error: N needed to be even')

    dx = (b - a)/N

    x = np.arange(a, b+dx, dx) #x values

    sum = 0 #initialize integral sum
    for i in range(1, int(N/2)):
        sum += f(x[2*i]) + 4*f(x[2*i+1]) + f(x[2*i+2])

    sum *= dx/3

    return(sum)


#Testing
'''
f = lambda x: x**2

sum_m = midpoint(f, 4, 20, 100000)
sum_t = trapezoid(f, 4, 20, 100000)
sum_s = simpsons(f, 4, 20, 100000)

print(sum_m)
print(sum_t)
print(sum_s)
'''
