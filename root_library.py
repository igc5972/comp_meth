### PURPOSE: Three functions for methods of root finding
### Can be called from other scripts
### [Isabella Cox, Aug. 2020]

### [Task 1]


def bisection(f, a, b, thresh=1E-10, pr = True):

    '''
    Locate a root of a function using the bisection method.

    Input values:

    f --       the function of which to find the roots
    a --       leftward initial bound of where the root is
    b --       rightward initial bound of where the root is
    thresh --  maximum acceptable value below which a functional value will be
               considered a roots
    pr --      flag for printing out number of iterations required to find the
               root

    Returns:

    location of the root if possible to finding
    can use pr flag to choose to print number of iterations
    otherwise, returns None and an error print statement
    '''


    # Check that f(a) x f(b) < 0, if not, return error Statements
    f_a = f(a)
    f_b = f(b)

    if f_a * f_b > 0:
        print("Starting boundaries not appropriate, no roots found")
        return None

    new_a = a
    new_b = b

    # Calculate the midpoint
    new_m = (new_a + new_b ) / 2

    counter = 1 # Initialize counter for number of iterations

    # Iterate through while the midpoint is not within threshold
    while abs(f(new_m)) > thresh:

        new_m = (new_a + new_b) / 2

        counter += 1

        # Case where actual midpoint lies between new_m and new_a
        if f(new_m) * f(new_a) < 0:
            new_b = new_m

        # Case where actual midpoint lies between new_m and new_b
        if f(new_m) * f(new_b) < 0:
            new_a = new_m

    # Case where functional value of midpoint is within threshold of == 0
    # If the while loop is exited
    print("Found the root within threshold")
    if pr == True:
        print("Number of Interations taken: " + str(counter))
        return(new_m, counter)
    return(new_m)



def newton(f, xn, thresh = 1E-10, pr = True):

    '''
    Locate a root of a function using the Newton method.

    Input values:

    f --       the function of which to find the roots
    xn --      inital guess point close to root
    thresh --  maximum acceptable value below which a functional value will be
               considered a roots
    pr --      flag for printing out number of iterations required to find the
               root

    Returns:

    location of the root if possible to finding
    can use pr flag to choose to print number of iterations
    otherwise, returns None and an error print statement
    '''

    #Calculate the derivative of a function (from lambda) using def. of derivative
    def deriv(f, x, h = 1E-10):
        return (f(x+h) - f(x))/h

    xnn = xn - (f(xn)/deriv(f, xn))

    counter = 1 # Initialize counter for number of iterations

    # Iterate while the point is not the within threshold of zero
    while abs(f(xnn)) > thresh:

        xnn = xnn - (f(xnn)/deriv(f, xnn))


    # Case where while loop was exited because root was found
    print("Found the root within threshold")
    if pr == True:
        print("Number of Interations taken: " + str(counter))
        return(xnn, counter)
    return(xnn)



def secant(f, x0, x1, thresh=1E-10, pr = True):

    '''
    Locate a root of a function using the Secant method.

    Input values:

    f --       the function of which to find the roots
    x0 --      inital guess for left bound on root
    x1 --      initial guess for right bound on root
    thresh --  maximum acceptable value below which a functional value will be
               considered a roots
    pr --      flag for printing out number of iterations required to find the
               root

    Returns:

    location of the root if possible to finding
    can use pr flag to choose to print number of iterations
    otherwise, returns None and an error print statement
    '''


    if f(x0) * f(x1) > 0:
        print("Starting boundaries not appropriate, no roots found")
        return None

    x2 = x1 - f(x1) * ((x1 - x0)/(f(x1) - f(x0)))

    counter = 1 # Initialize counter for number of iterations
    while x2 > thresh:

        counter += 1

        x2 = x1 - f(x1) * ((x1 - x0)/(f(x1) - f(x0)))

        # Case of very close to root, difference ~ 0
        if f(x1) - f(x0) < 1E-15:
            break

        x0 = x1
        x1 = x2


    # Case where while loop was exited because root was found
    print("Found the root within threshold")
    if pr == True:
        print("Number of Interations taken: " + str(counter))
        return(x2, counter)
    return(x2)






#########################
#Testing:
#########################

'''
f = lambda x: x**2 - 45 #function to find root of

rootb = bisection(f, 4, 8, pr = True)
rootn = newton(f, 1, pr = True)
roots = secant(f, 4, 8, pr = True)

print("Root with bisection method: " + str(rootb))
print("Root with newton method: " + str(rootn))
print("Root with secant method: " + str(roots))
'''
