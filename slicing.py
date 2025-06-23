#A 1D array is like a simple list.
#BELOW IS THE 1D ARRAY EXAMPLE
'''import numpy as np
a1=([2,3,4,5,6])
arr=np.array(a1)
print(arr[0:2])'''#here pass the slicing
#2D Array Slicing
#Now let’s move to 2D:
import numpy as np 
s2=([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
arr=np.array(s2)
'''print(arr[0, 2])'''  # Output: 30 (Row 0, Column 2)
'''print(arr[2, 1])'''  # Output: 100 (Row 2, Column 1)
'''print(arr[:]) '''   # entire matrix (all rows)
'''print(arr[:, 1]) '''   # All rows, column 1 → [20 60 100]
'''print(arr[:, 1:3])'''  # All rows, columns 1 and 2
'''print(arr[-1])  '''       # [ 90 100 110 120]
'''print(arr[:, -2:]) '''    # last 2 columns:
                      # [[ 30  40]
                      #  [ 70  80]
                      #  [110 120]]
'''print(arr[::-1, ::-1])''' # flips entire array both ways



