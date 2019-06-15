# Python program for implementation of Bubble Sort
 
def bubbleSort(arr):
  n = len(arr)

  # Traverse through all array elements
  for i in range(n):

    # Last i elements are already in place
    for j in range(0, n-i-1):

      # traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element
      if arr[j] > arr[j+1]:
          temp = arr[j]
          arr[j] = arr[j+1]
          arr[j+1] = temp

myArr = [5, 3, 7, 1, 98, 65, 0]
bubbleSort(myArr)
print(myArr)