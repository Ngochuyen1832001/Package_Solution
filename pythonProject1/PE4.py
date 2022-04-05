#The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
#from unsorted part and putting it at the beginning. The algorithm maintains two sub arrays in a given array.
#1) The sub array which is already sorted.
#2) Remaining sub array which is unsorted. In every iteration of selection sort, the minimum element (considering ascending order)
#from the unsorted sub array is picked and moved to the sorted sub array.

#Write a Python program to implement the algorithm.


A = [3,4,1,5,6,8,2,5,7,9,0]

for i in range(len(A) - 1):
    min_index = i
    for j in range(i + 1, len(A)):
        if A[min_index] > A[j]:
            min_index = j
    if min_index != i:
        A[i], A[min_index] = A[min_index], A[i]

print("Sorted array: ")
for i in range(len(A)):
    print("%d " %A[i], end = ' ')
