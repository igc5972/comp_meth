"""
Michael Lam
ASTP-720, Fall 2020

A simple function that will return a Python dictionary of the A_ul coefficients
found in A_coefficients.dat. This is merely a convenience and some other method
can be written. To use, simply import this file and run the function in a form:

Adict = read_coefficients()

The dictionary will take a tuple as a key in the format (lower, upper) level.

If the A_coefficients.dat is stored in a separate directory, you should
specify that as an argument:

read_coefficients(filename=/path/to/file)
"""

import numpy as np
import astropy.units as un


def read_coefficients(filename="A_coefficients.dat"):
    """
    read_coefficients() as defined above

    Parameter
    =========
    filename (optional): another path to the A_coefficients.dat file.
    """
    # unpack the text file
    l, u, As = np.loadtxt(filename, unpack=True, delimiter=",",
                          dtype={"names": ('l', 'u', 'A_ul'),
                                 "formats": (np.int, np.int, np.float)})

    # Apply units of inverse seconds
    As /= un.s

    # Create the dictionary to return
    Adict = dict()
    for i in range(len(l)):
        Adict[(l[i], u[i])] = As[i]

    return Adict


if __name__ == '__main__':
    Adict = read_coefficients()
    print(Adict)
    print("Check: 778000 1 / s is roughly")
    print(Adict[(3, 6)])
