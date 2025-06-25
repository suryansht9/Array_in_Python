#Get the data type of an array object:
'''import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)'''

#get the data type of an array objecct whihch is in string
'''import numpy as np
arr=np.array(["apple","banana","cherry"])
print(arr.dtype)'''

#Creating Arrays With a Defined Data Type
#We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:
#Example
#Create an array with data type string:
'''import numpy as np
myarr=np.array([1,2,3,4,5,60],dtype="S")
print(myarr)
print(myarr.dtype)'''
