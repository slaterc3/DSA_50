"""Coding Exercise: Josephus problem
There are n friends that are playing a game. 
The friends are sitting in a circle and are numbered 
from 1 to n in clockwise order. More formally, 
moving clockwise from the ith friend brings you 
to the (i+1)th friend for 1 <= i < n, and moving clockwise 
from the nth friend brings you to the 1st friend. 
The rules of the game are as follows: 
Start at the 1st friend. 
Count the next k friends in the clockwise direction 
including the friend you started at. 
The counting wraps around the circle 
and may count some friends more than once. 
The last friend you counted leaves the circle and loses the game. 
If there is still more than one friend in the circle, 
go back to step 2 starting from the friend immediately clockwise 
of the friend who just lost and repeat. 
Else, the last friend in the circle wins the game. 
Given the number of friends, n, and an integer k, 
return the winner of the game."""
def findTheWinner(n, k):
    #write code here
    arr = [x for x in range(1, n+1)]
    def helper(arr, start):
        if len(arr) == 1:
            return arr[0]
        remove = (start + k-1)%len(arr)
        del arr[remove]
        return helper(arr, remove)
    return helper(arr, 0)
    
# def josephus_problem1(n, k):
#     # creating array
#     arr = [x for x in range(1,n+1)]
#     # if len(array) == 0:
#     #     return 1
#     # now the helper function
#     def winner(arr, start):
#         if len(arr) == 1:
#             return arr[0]
#         # the position of kill (remove)
#         # starting position == 1
#         kill_position = (start + k-1) % len(arr)
#         del arr[kill_position] # reduces length by 1
#         # recursive call
#         return winner(arr, kill_position)
    
#     return winner(arr, 0)

if __name__ == "__main__":
    test_cases = [
        (1, 1, 1),
        (5, 2, 3),
        (7, 3, 4),
        (6, 6, 4),
        (4, 7, 2),
        (10, 3, 4)
    ]
    
    for i, (n, k, expected) in enumerate(test_cases, 1):
        result = findTheWinner(n, k)
        print(f"Test case {i}: n = {n}, k = {k}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"{'Passed' if result == expected else 'Failed'}\n")
