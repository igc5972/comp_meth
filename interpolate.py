### PURPOSE: ASTP 720 (Computational Methods) HW #1
### [Isabella Cox, Aug. 2020]

### [Task 5]

def interpolate(x, y):
    '''
    Perform piece-wise linear interpolation

    Input values:

    x --    xvalues for a set of data points
    y --    yvalues for a set of data points

    Returns:

    f -- function to be used to construct new data points
    '''

    for i in range(1, len(x)-1):

        func = lambda x: y[i]*(1 - ((x - x[i])/(x[i+1] - x[i]))) + y[i+1] * ((x - x[i])/(x[i+1] - x[i]))
        return func
