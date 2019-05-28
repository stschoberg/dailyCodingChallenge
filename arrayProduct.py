from functools import reduce
# Given an array of integers, return a new array
# such that each element at index i of the new array
# is the product of all the numbers in the original
# array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Multiply all the numbers in the list to get a total.
# Divide the total by arr[i] for each element to get
# total without that sum O(n) time
def productList(lst):
    # Sums the list
    prod = reduce((lambda x, y: x*y), lst)
    toReturn = []
    for num in lst:
        toReturn.append(prod/num)

    # print(toReturn)



# Follow-up: what if you can't use division?

# The product of the list minus arr[i] is the product
# of all elements before i times all the elements after i.
# Create a list of all the elements before i, and the elements
# after i, then multiply those two lists element by element.


def productListNoDivision(lst):
    # Product of items before arr[0] is one
    prodsBeforeIndex = [1]
    # Product of items after last element is one
    prodsAfterIndex = [1]

    # prodsBeforeIndex[i] is the product of elements before lst[i]
    for i in range(0, len(lst) - 1):
        prodsBeforeIndex.append(lst[i] * prodsBeforeIndex[i])

    lst.reverse()

    # prodsAfterIndex[i] is the product of elements after lst[i]
    for j in range(0, len(lst) - 1):
        prodsAfterIndex.append(lst[j] * prodsAfterIndex[j])
        # prodsAfterIndex.append(lst[i] * prodsAfterIndex[i])

    prodsAfterIndex.reverse()

    # Multiply the two lists 
    print([a*b for a,b in zip(prodsBeforeIndex,prodsAfterIndex)])


def main():
    lst = [3,2,1]
    productList(lst)
    productListNoDivision(lst)

if __name__== "__main__":
    main()
