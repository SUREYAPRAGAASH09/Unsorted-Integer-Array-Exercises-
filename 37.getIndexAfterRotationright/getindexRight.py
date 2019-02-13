Problem :
=========
    Given an unsorted integer array A,find the value that will be in 3rd position or index after 2 rotations to the right.
Input :
=======
    An Unsorted Integer Array , 
      
    Rotation value of type integer
Output :
=========
    Integer is extracted after rotation is made 
Code :
======
import Rotateright

def getIndexAfterrotationRight(array, rotation_value):
    afterRotation = Rotateright.swapRight(array,rotation_value)
    return afterRotation[3]
