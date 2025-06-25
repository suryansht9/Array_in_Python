#CONVERSION OF 1D TO 2D
#MAKE SURE PASSING VALUE VARIABLE INSIDE OF RESHAPE IS MULTILPICATION OF TOTAL COUNT OF ELEMENTS
'''import numpy as np
s1=([2,3,4,5])
arr=np.array(s1)
print(arr.reshape(1,4),"Its 1st possible matrix")
print(arr.reshape(2,2),"Its 2nd possible matrix")
print(arr.reshape(4,1),"Its 3rd possible matrix")'''
#CONVERSION OF 1D TO 3D {2ND PROG}
'''import numpy as np 
s=([1,2,3,4,5,6,7,8,9])
arr=np.array(s)
print(arr.reshape(1,9),"Its 1st possible matrix")
print(arr.reshape(3,3),"Its 2nd possible matrix")
print(arr.reshape(9,1),"Its 3rd possible matrix")
print(arr.reshape(1,3,3),"Its 4th possible matrix")
print(arr.reshape(1,9,1),"Its 5th possible matrix")
print(arr.reshape(3,1,3),"Its 6th possible matrix")
print(arr.reshape(3,3,1),"Its 7th possible matrix")
print(arr.reshape(9,1,1),"Its 8th possible matrix")
print(arr.reshape(1,1,9),"Its 9th possible matrix")'''
#CONVERSION OF 1D TO 4D {3RD PROG}
'''import numpy as np 
s=([1,2,3,4,5,6,7,8,9,10,11,12])
arr=np.array(s)
print(arr.reshape(1,2,3,2),"Its 1st possible matrix")
print(arr.reshape(1,3,2,2),"Its 2nd possible matrix")
print(arr.reshape(1,6,1,2),"Its 3rd possible matrix")
print(arr.reshape(2,2,1,3),"Its 4th possible matrix")
print(arr.reshape(2,1,3,2),"Its 5th possible matrix")
print(arr.reshape(3,1,2,2),"Its 6th possible matrix")
print(arr.reshape(4,1,3,1),"Its 7th possible matrix")'''
#CONVERSION OF 2D TO 3D{4 prog}
'''import numpy as np
s=([[2,3,4,5],[6,7,8,9]])
arr=np.array(s)
arr3d=arr.reshape(1,2,4)
print(arr3d)
print(arr3d.shape,"this is shape of matrix")'''
#CONVERSION OF 2D TO 4D{5 prog}
'''import numpy as np
s=([[2,3,4,5],[6,7,8,9]])
arr=np.array(s)
print(arr.reshape(1,2,2,2))
print(arr.reshape(1,1,2,2,2))
print(arr.shape,"this is the shape of matrix")
'''
