### PURPOSE: ASTP 720 (Computational Methods) HW #2 Pt. 3
### Task 3 -
import numpy as np
import  copy



class Matrix:
    def __init__(self, matrix):
        self.nrows = len(matrix)
        self.ncols = len(matrix[0])
        self.M = np.array([[float(y) for y in i] for i in matrix])

        #^^ convert to floats to avoid silly errors later on

    #print out matrix (useful for debugging)
    def pprint(self):
        print(self.M)


    #Make array of zeros the size of n, m desired
    #(to use as initalization to populate for later)
    def zconstruct(self, n, m):

        z = []
        for r in range(n):
            new_rows = []
            for c in range(m):
                new_rows.append(0)
            z.append(new_rows)

        #print(z)
        return(Matrix(z).M)


    #construct identity matrix of size n, m
    def identity(self, n, m):

        #initialize array of zeros to hold identity matrix
        iden = []
        for r in range(n):
            new_rows = []
            for c in range(m):
                if r == c:
                    new_rows.append(1) #1 on diagonals
                else:
                    new_rows.append(0) #0 elsewhere
            iden.append(new_rows)

        return(Matrix(iden))


    # (1) Add two matrices together element-wise
    def __add__(self, other):

        #Handle case of dimension mismatch
        if self.nrows != other.nrows or self.ncols != self.ncols:
            raise(ValueError, 'Dimensions of matrices must match')


        #initialize array of zeros to hold sum
        sum = self.zconstruct(self.nrows, self.ncols)

        for r in range(self.nrows):
            for c in range(self.ncols):
                sum[r][c] = self.M[r][c] + other.M[r][c]

        return(Matrix(sum))



    # (2) Multiply two matrices together
    def __mul__(self, other):

        #Handle case of dimension mismatch
        if self.ncols != other.nrows:
            raise(ValueError, 'Dimensions of matrices must match')


        #initialize array of zeros to hold product
        mult = self.zconstruct(self.nrows, other.ncols)

        for r in range(self.nrows):
            for c in range(other.ncols):
                for k in range(other.nrows):
                    mult[r][c] += self.M[r][k] * other.M[k][c]

        return(Matrix(mult))



    # (3) Transpose a matrix
    def trans(self):

        #initialize array of zeros to hold transposed array
        tra = self.zconstruct(self.nrows, self.ncols)

        for r in range(self.nrows):
            for c in range(self.ncols):
                tra[c][r] = self.M[r][c]

        return(Matrix(tra))


    #compute upper triangle (row echelon) form of matrix
    #needed for subsequent parts
    def uppertri(self):

        m = copy.deepcopy(self.M)

        #Handle case of dimension mismatch
        if len(m) != len(m[0]):
            raise(ValueError, 'Dimensions of matrices must match')

        n = len(m) #number of rows AND columns (square matrix)

        #check pivots != 0
        #or if so, that there is an element below pivot != 0
        for i in range(n):

            if m[i][i]!= 0: #current diag. pivot != 0 --> good!
                pass

            belows = []

            for k in range(i, n): #check the elements BELOW current pivot
                belows.append(abs(m[k][i]))

            if np.sum(belows) < 1E-4: #so it is zero, esssentially
                return('ValueError: All potential pivots are zero')


        #i controls row AND col of pivot element
        for i in range(n-1):

            no_swaps = 0 #keep count to adjust sign on determinant
            maxrow = i #initialize maxrow as current pivot row
            maxpivot = m[i][i] #inialize as current pivot (diag. entry)

            #necessary to copy to avoid rewriting orig. matrix
            #find if there is a row element in col below pivot row with > max
            for k in range(i+1, n):
                if m[k][i] > maxpivot:
                    maxpivot = m[k][i]
                    maxrow = k


            #do row swapping if needed
            if maxrow != i:
                no_swaps += 1
                m[[maxrow, i], :] = m[[i, maxrow], :]

            #perform gaussian elimination
            for r in range(i+1, n):
                factor = m[r][i] / m[i][i]

                #go through all the columns
                for c in range(i, n):
                    m[r][c] -= m[i][c] * factor

        m  = np.array([[round(y, 8) for y in i] for i in m])

        return(Matrix(m), no_swaps)


    # (4) Calculate inverse of a Matrix

    def inverse(self):

        n = self.nrows

        U = copy.deepcopy(self.M)

        iden = (self.identity(self.nrows, self.ncols)).M

        #get the column slices of identiy Matrix
        #these col. vectors will be used to find coefficients of inverse matrix
        B_s = []
        for i in range(n):
            entry = iden[:][i]
            B_s.append(entry)


        #will hold column vectors of inverse matrix
        inverse = []

        #perform back subst. with each column vector of identity matrix
        for b in B_s:

            xes = [0] * n #initialize inverse coeff. for columns

            #go from i = n-1, n-2, ...., 0
            for i in range(n-1, -1, -1):

                sum = 0 #initalize
                for j in range(i+1, n):
                    sum += U[i][j] * xes[j]
                xes[i] = (1 / U[i][i]) * (b[i] - sum)

            inverse.append(xes)


        #rotate list of column vectors back into matrix form
        inverse_matrix = list(map(list, zip(*inverse)))

        #print(inverse_matrix)
        return(Matrix(inverse_matrix))


    # (6) Calculate determinant of matrix
    def determinant(self):

        uppertri, swaps = self.uppertri()
        n = uppertri.nrows

        det = 1
        #calculate det as product of diagonal entries of upper triangle form
        for i in range(n):
            det *= uppertri.M[i][i]


        #get sign on matrix
        if swaps != 0:
            det *= (-1)**swaps

        return(det)


    # (5) Calculate trace of matrix
    def trace(self):

        #Handle case of dimension mismatch
        if self.nrows != self.ncols:
            raise(ValueError, 'Dimensions of matrices must match')

        n = self.nrows

        tr = 0
        #calculate tr as sum of diagonal entries of upper triangle form
        for i in range(n):
            tr += self.M[i][i]

        return(tr)


    # (7) LU (lower upper) decomposition of Matrix
    # THIS IS NOT WORKING!!!!
    def lu(self):

        if self.nrows != self.ncols:
            raise(ValueError, 'Dimensions of matrices must match')

        L = self.zconstruct(self.nrows, self.ncols)
        U = self.zconstruct(self.nrows, self.ncols)

        n = self.nrows

        #fill in top row and left column from base case

        L[0][0] = 1.0

        for i in range(n):
            L[i][0] = self.M[i][0]

        for i in range(n):
            U[0][i] = self.M[0][i] / L[0][0]

        #iterate over all the rows within right angle of outer row and column
        for r in range(n):

            # (L)ower triangle
            #look at columns: 0, 1, 2, ..., r
            for c in range(r):
                sum = 0
                for k in range(c-1):
                    sum += float(L[r][k] * U[k][c])
                L[r][c] = (self.M[r][c] - sum) / U[c][c]

            # (U)pper triangle
            #looks at columns: r, r+1, r+2, ..., n
            for c in range(r, n):
                sum = 0
                for k in range(r-1):
                    sum += float(L[r][k] * U[k][c])
                U[r][c] = (self.M[r][c] - sum ) / L[r][r]


a= [[2., -3., 1.],
           [2., 0., 1.],
           [1., 4., 5.]]
print(np.linalg.inv(a))


a = Matrix(a)

a.inverse()

print(np.linalg.inv(a))
