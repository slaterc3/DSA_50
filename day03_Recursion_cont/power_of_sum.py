"""Coding Exercise: Power Sum
Question:

Power Sum - Let’s define a peculiar type of array in which each element is either an integer or another peculiar array. Assume that a peculiar array is never empty. Write a function that will take a peculiar array as its input and find the sum of its elements. If an array is an element in the peculiar array you have to convert it to it’s equivalent value so that you can sum it with the other elements. Equivalent value of an array is the sum of its elements raised to the number which represents how far nested it is. For e.g. [2,3[4,1,2]] = 2+3+ (4+1+2)^2

another example - [1,2,[7,[3,4],2]] = 1 + 2 +( 7+(3+4)^3+2)^2"""

def power_sum(array,power=1):
    #write code here
    total = 0 
    for element in array:
        if type(element) == int:
            total += element
        else:
            total += power_sum(element, power+1)
    return total**power     

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3], 6),
        ([2, 3, [4, 1, 2]], 54),
        ([1, 2, [7, [3, 4], 2]], 123907),
        ([1, [2, [3]]], 842),
        ([[5]], 25),
        ([10, [5, [2, 3]]], 16910)
    ]
    
    # Running test cases
    for i, (array, expected) in enumerate(test_cases, 1):
        result = power_sum(array)
        print(f"Test case {i}: array = {array}")
        print(f"Expected: {expected}, Got: {result}")
        print("Passed" if result == expected else "Failed", "\n")


