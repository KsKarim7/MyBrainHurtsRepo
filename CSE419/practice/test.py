# # Defining a function to find the first occurrence, which will take the array of integers, the length of the array, and the number we have to search for  
# def firstOccurance(array, length, x):  
  
#     # Initializing the variable that will store the occurrences  
#     # We will start with -1 so that if the number is not present, it will return the same output  
#     result = -1   
  
#     # Beginning of the list  
#     s = 0   
#     # Ending of the list  
#     e = length - 1   
  
#     # Starting the while loop  
#     while s <= e:  
#         # Finding the middle index of the list based on the current s and e positions  
#         mid = (s + e) // 2   
  
#         # Checking if the middle element is equal to x  
#         # If yes, we will store the middle index in the result and then search in the left half  
#         if array[mid] == x:  
#             result = mid  
#             e = mid - 1  
          
#         # If the middle element is greater than x then search in the left half  
#         elif array[mid] > x:  
#             e = mid - 1   
          
#         # Else search in the right half  
#         else:  
#             s = mid + 1  
#     return result  
  
# # Creating an integer array and calling the function  
# array = [1, 2, 2, 2, 2]  
  
# # Finding the length of the array to pass to the function  
# length = len(array)  
  
# # We will search the first index of 3  
# x = 2   
# ans = firstOccurance(array, length, x)  
# print(f"The first occurrence of {x}  is at:", ans)   

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        quick_sort(arr, low, j - 1)
        quick_sort(arr, j + 1, high)

def main():
    n = 7
    # arr = [int(x) for x in input().split()]
    arr = [2,3,10,12,23,45,99]
    quick_sort(arr, 0, n - 1)
    print(' '.join(map(str, arr)))

if __name__ == "__main__":
    main()