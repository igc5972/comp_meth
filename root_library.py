### Library of 3 root finding methods (bisection, newton and secant)
###

### Import Statements



### Bisection method

def bisection(f, a, b, thresh, pr = True):

    '''
    Locate a root of a function using the bisection method.

    Input values:

    f --       the function of which to find the roots
    a --       leftward initial bound of where the root is
    b --       rightward initial bound of where the root is
    thresh --  maximum acceptable value below which a functional value will be
               considered a roots
    pr ---     flag for printing out number of iterations required to find the
               root

    Output value:

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

    counter = 0 # Initialize counter for number of iterations

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

    print("Found the midpoint within threshold")
    if pr == True:
        print("Number of Interations taken: " + str(counter))
    return(new_m)
