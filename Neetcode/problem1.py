# Given an integer array 'nums' 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct

# Brute force approach
# Time Complexity -> O(n2)
# Space Complexity -> O(n)


# Optimal Approach
# Time Complexity -> O(n)
# Space Complexity -> O(n)
def determineUniquenessOfArray(array):
    elements_set = set()
    for i in array:
        if i in elements_set:
            return True
        elements_set.add(i)
    return False

array1 = [0, 2, 1, 5, 6, 2]
array2 = [0, 2, 1, 5, 6, 7, 10, 16]

containsRepetitiveElements = determineUniquenessOfArray(array2)
if containsRepetitiveElements:
    print("Array contains repetative elements")
else:
    print("Array contains distinct elements")


