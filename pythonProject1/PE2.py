
#In a nutshell, the search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison.
#Compare x with the middle element.  If x matches with the middle element, we return the mid index.
#Else if x is greater than the mid element, then x can only lie in the right (greater) half sub array after the mid element. Then we apply the algorithm again for the right half.
#Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
#Write a program in the python programming language to implement the Search algorithm above.
# Test array
#arr = [ 2, 3, 4, 10, 40 ]
#x = 10
#Output:
#Element is present at index 3.

arr = [0,1,5,6,8,9]
left = 0
right = len(arr) - 1

x = input("Number to be searched: ")
x = int(x)
check = False

while(left <= right):
    mid = int((left + right)/2)
    if arr[mid] == x:
        print("Element present at index %d" %mid)
        check = True
        break
    elif arr[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

if check == False:
    print("Element does not exist in the list")
