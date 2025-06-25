#dtype tells you the data type of the elements in the NumPy array (e.g., int32, float64).
#In your case, since all the numbers are integers, it will likely print something like int64 or int32, depending on your system.
'''import numpy as np
a1=[[[3,4,5,6,7],[5,6,7,8,9]]]
arr1=np.array(a1)
print(arr1.dtype)'''
#BYTES TELL US THE SIZE OD PASSED VARIABLES
#Your array shape is (1, 2, 5) → 1 block, 2 sublists, each with 5 integers → total 10 elements.
#NumPy stores integers with a default type like int32 or int64, depending on your system.
'''import numpy as np
a1=[[[3,4,5,6,7],[5,6,7,8,9]]]
arr1=np.array(a1)
print(arr1.nbytes)'''
#SIZE TELLS US THE LENGTH OF GIVEN DIMENSIONS
import numpy as np
a1=[[[3,4,5,6,7],[5,6,7,8,9]]]
arr1=np.array(a1)
print(arr1.size)
