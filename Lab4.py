import numpy as np 
a = np.matrix([[1,2],[4, -1]])
b = np.matrix ([[2, -3], [-4, 1]])
solve = (a*b)-(b*a)
print ("Answer numb 1:", solve )

c = np.matrix ([[-1,0,2],[0, 1, 0], [1, 2, -1]])
print ("Answer numb 2:", c**2 )

d = np.matrix ([[5,8,-4],[6, 9, -5], [4, 7, -3]])
i = np.matrix ([[3,2,5],[4, -1, 3], [9, 6, 5]])
print ("Answer numb 3:", d*i )

f = np.linalg.det ([[2,3,4],[1, 0, 6], [7, 8, 9]])
print ("Answer numb 4: ", f)

e = np.linalg.det ([[2,3,4, 1],[1, 2, 3, 4],[3, 4, 1, 2], [4, 1, 2, 3]])
print ("Answer numb 5: ", e)

j = np.linalg.inv ([[1,2,3],[0, 1, 2], [0, 0, 1]])
print ("Answer numb 6: ", j)

k =  np.linalg.matrix_rank ([[1,2,3,4],[3, -1, 2, 5],[1, 2, 3, 4], [1, 3, 4, 5]])
print ("Answer numb 7: ", k)

def kramar(a,b):
    c = np.linalg.det(a)
    if c!=0:
        a1 = np.matrix(a)
        a1[:,0] = b
        
        a2 = np.matrix(a)
        a2[:,1] = b
        
        a3 = np.matrix(a)
        a3[:,2] = b
        
        x = np.linalg.det(a1)/c
        y = np.linalg.det(a2)/c
        z = np.linalg.det(a3)/c
    else:
        print("No root")
    print("Kramer:")
    print (x,y,z)
    print("Check:", np.linalg.solve(a,b))
    return x, y, z
    
kramar(np.matrix([[14,4,6], [5,-3,2], [10, -11, 5]]), np.matrix([[30],[15],[36]]))

def matrixMeth():
    a3 = np.matrix('3, 2, 1; 2, -1,1; 1,5,0')
    b3 = np.matrix('5;6;-3')
    a3 = np.linalg.inv(a3)
    c3 = a3*b3
    print (c3)
    print ("Answer: ", np.linalg.solve(np.linalg.inv(a3), b3))
matrixMeth()
