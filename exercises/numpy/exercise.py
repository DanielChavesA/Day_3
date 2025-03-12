import numpy as np

#a Null vector
vector_a=np.zeros(10)
vector_a[4]=1
print("a:",vector_a)

#b values ranging from 10 to 49
vector_b = np.arange(10, 50)
print("b:", vector_b)

#c Reverse a vector 
vector_c = vector_b[::-1]
print("c:", vector_c)

#d 3x3 matrix with values ranging from 0 to 8
matrix_d = np.arange(9).reshape(3, 3)
print("d:\n", matrix_d)

#e indices of non-zero elements from [1,2,0,0,4,0]
vector_e = np.array([1, 2, 0, 0, 4, 0])
indices = np.nonzero(vector_e)
print("e:", indices)

#f random vector of size 30 and find the mean value
vector_f = np.random.rand(30)
mean_value = np.mean(vector_f)
print("f:", mean_value)

#g 2D array with 1 on the border and 0 inside
matrix_g = np.ones((5, 5))
matrix_g[1:-1, 1:-1] = 0
print("g:\n", matrix_g)

#h Create an 8x8 matrix with a checkerboard pattern
matrix_h = np.zeros((8, 8), dtype=int)
matrix_h[1::2, ::2] = 1
matrix_h[::2, 1::2] = 1
print("h:\n", matrix_h)

#i checkerboard matrix using the tile function
matrix_i = np.tile([[0, 1], [1, 0]], (4, 4))
print("i:\n", matrix_i)

#j Negate all elements which are between 3 and 8, in place
Z = np.arange(11)
Z[(Z > 3) & (Z < 8)] *= -1
print("j:", Z)

#k random vector of size 10 and sort it
Z = np.random.random(10)
Z.sort()
print("k:", Z)

#l Cequal between A|B randomn arrays
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.array_equal(A, B)
print("l:", equal)

#m square of every number in an array in place
Z = np.arange(10, dtype=np.int64)
print("m (before):", Z)
Z **= 2
print("m (after):", Z)

#n Get the diagonal of a dot product
A = np.arange(9).reshape(3, 3)
B = A + 1
C = np.dot(A, B)
D = np.diag(C)
print("n:", D)
