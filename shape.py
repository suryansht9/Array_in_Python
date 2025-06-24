
#IF WE WANT TO CHECK ATTRIBUTE OF ROWS AND COLUMN IN MATRIX
import numpy as np

a1 = [[4, 5, 7], [7, 8, 9]]
arr1 = np.array(a1)
print(arr1)
print(arr1.shape)



#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

import numpy as np
myarr=([1,2,3,4],ndmin=5)
print(myarr)
print(myarr.shape,"This is the 5d dimension after applying ndmin according to ques")
