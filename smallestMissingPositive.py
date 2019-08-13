# Given an array of integers, find the first missing positive integer
# in linear time and constant space. In other words,
# find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.



# METHOD:
# 1. Want the missing Positive, filter out the negs.


def smallestMissingPositive(arr):
    # Seperate positive and negative in the array
    x = partition(arr)
    print arr
    for i in range(0, x + 1):
        # print i
        if(arr[i] < len(arr)):
            print(arr[i])
            arr[abs(arr[i])] *= -1
    print(arr)
    for i in range(1, len(arr)):
        if(arr[i] > 0):
            print(i)
            return i


def partition(arr):
        x = True
        i = 0
        j = len(arr) - 1
        iStopped = 0
        jStopped = 0

        while(i < j):
            if(arr[i] > 0):
                i+=1
            else:
                iStopped = 1

            if(arr[j] < 0):
                j-=1
            else:
                jStopped = 1

            if(iStopped == 1 and jStopped == 1):
                arr[i], arr[j] = arr[j], arr[i]
                iStopped = 0
                jStopped = 0
        return i



def main():
    lst = [3, 4, -1, 1]

    smallestMissingPositive(lst)


if __name__== "__main__":
    main()
