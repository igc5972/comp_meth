### PURPOSE: ASTP 720 (Computational Methods) HW #1 Pt. 5
### Linear, piecewise interpolation code
### [Isabella Cox, Aug. 2020]


def interpolate(xs, ys):

    '''
    Perform piece-wise linear interpolation

    Input values:

    x --    xvalues for a set of data points
    y --    yvalues for a set of data points

    Returns:

    f -- function to be used to construct new data points
    '''

    def apply(new_x):
        new_y = []
        for x in new_x:
            #check that x is within existing values
            if x < xs[0] or x > xs[-1]:
                continue
            for i in range(0, len(xs)-1):
                if xs[i] < x < xs[i+1]:
                    new_y.append(ys[i]*(1 - ((x - xs[i])/(xs[i+1] - xs[i]))) \
                    + ys[i+1] * ((x - xs[i])/(xs[i+1] - xs[i])))
        return(new_y)

    func = lambda x: apply(x)
    print("test")

    return func
