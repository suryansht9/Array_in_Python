#From this practice set we are going to run indexing of arrays
'''
import numpy as np
ok=np.array([1,2,3,4,5])
print(ok[1])'''

#Get third and fourth elements from the following array and add them.
'''print(ok[2] + ok[3])'''

#Access 2-D Arrays
#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
#Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.
'''
import numpy as np
ok=np.array([[1,2,3,4],[5,6,7,8]])
print(ok[0,2])#expected output is 3
print(ok[1,1])#expected output is 6'''

#Add elements in 2-d Array
'''import numpy as np
ok=np.array([[23,24,25,26],[10,20,30,40]])
print(ok[0,2] + ok[1,2])'''

#Access 3-D Arrays
#To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
import numpy as np 
ok=np.array([[[1,2,3,4],[5,6,7,8]],[9,10,11,12],[8,5,4,3]])
print(ok[0,2,2])