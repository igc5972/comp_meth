### PURPOSE: ASTP 720 (Computational Methods) HW #1
### [Isabella Cox, Aug. 2020]

### [Task 5]

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
            for i in range(0, len(xs)-1):
                print(xs[i], x, xs[i+1])
                if xs[i] < x < xs[i+1]:
                    new_y.append(ys[i]*(1 - ((x - xs[i])/(xs[i+1] - xs[i]))) \
                    + ys[i+1] * ((x - xs[i])/(xs[i+1] - xs[i])))
        return(new_y)
        print(new_y)

    func = lambda x: apply(x)
    return func


'''
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

halfs = [1.5, 2.5, 3.5, 4.5]

func = interpolate(x, y)
print(func(halfs))
'''
