# Given a list of numbers and a number k,
# return whether any two numbers from the
# list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.


#  Log the appearance of each number in checkList,
#  1 for exists 0 for not. For each number in the
#  list, check to see if the complement (to reach k)
#  has been previously logged. O(n) time, O(k) space
def sumList(lst, k):
    checkList = [-1] * (k + 1)
    print(checkList)
    for num in lst:
        if checkList[k - num] == 1:
            return True
        else:
            checkList[num] = 1
    return False


def main():
    k = 17
    lst = [10, 15, 3, 7]
    sumList(lst, k)

if __name__== "__main__":
    main()
