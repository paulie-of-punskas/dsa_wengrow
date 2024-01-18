# The following function finds the greatest single number within the array, but has an efficiency of O(N^2).
# Rewrite the function so that it becomes a speedy O(N)

def greatestNumber(array):
    for i in array:
        # Assume for now that i is the greatest
        isValTheGreatest = True

        for j in array:
            # If we find another value that is greater than i
            # i is not the greatest
            if j > i:
                isValTheGreatest = False
        
        # If, by the time we checked all the other numbers, i
        # is still the greatest, it means that i is the greatest number
        if isValTheGreatest:
            return i

# Solution that is O(n)
def greatestNumberOn(array):
    greatestNumber = array[0]
    for i in range(len(array) - 1):
        if greatestNumber < array[i + 1]:
            greatestNumber = array[i + 1]
    return greatestNumber


numbers_list = [2345, 4564, 56, 456, 45, 3, 0, 22, 2, 167, 7]

print(greatestNumber(numbers_list))
print(greatestNumberOn(numbers_list))
