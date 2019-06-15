""" Sorting Algos left:
Recursive Bubble Sort
Insertion Sort
Recursive Insertion Sort
Merge Sort
Iterative Merge Sort
Quick Sort
Iterative Quick Sort
Heap Sort
Counting Sort
Radix Sort
Bucket Sort
ShellSort
"""

# Python program for implementation of Bubble Sort

""" Pseudocode for Bubble Sort
do
  swapped = false

  for i = 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap(leftElement, rightElement)
      swapped = true
while swapped
"""

def bubbleSort(A):
  n = len(A)

  # Traverse through all array elements
  for i in range(n):

    # Last i elements are already in place
    for j in range(0, n-i-1):

      # traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element
      if A[j] > A[j+1]:
          temp = A[j]
          A[j] = A[j+1]
          A[j+1] = temp

myArr1 = [5, 3, 7, 1, 98, 65, 0]
bubbleSort(myArr1)
print(myArr1)

# Python program for implementation of Bubble Sort
""" Pseudocode for Selection Sort
repeat (numOfElements - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum

  swap minimum with first unsorted position
"""
def selectionSort(A):
  # Traverse through all array elements 
  for i in range(len(A)): 
        
      # Find the minimum element in remaining  
      # unsorted array 
      min_i = i 
      for j in range(i+1, len(A)): 
          if A[j] < A[min_i]: 
              min_i = j 
                
      # Swap the found minimum element with  
      # the first element         
      # A[i], A[min_i] = A[min_i], A[i] 
      temp = A[i]
      A[i] = A[min_i]
      A[min_i] = temp

myArr2 = [5, 3, 7, 1, 98, 65, 0]
selectionSort(myArr2)
print(myArr2)