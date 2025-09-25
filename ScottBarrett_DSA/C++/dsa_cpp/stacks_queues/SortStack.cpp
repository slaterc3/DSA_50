#include "SortStack.h"


void sortStack(stack<int>& inputStack) {
    // if (stack.height == 0
    
    stack<int> newStack;
    // int temp; 
    while (!inputStack.empty()) {
        int temp = inputStack.top();
        inputStack.pop();
        while (!newStack.empty() && newStack.top() > temp) {
            inputStack.push(newStack.top());
            newStack.pop();
        }
        newStack.push(temp);
        
    }
    while (!newStack.empty()) {
        inputStack.push(newStack.top());
        newStack.pop();
    }
    
}
    //   +======================================================+
    //   |                 WRITE YOUR CODE HERE                 |
    //   | Description:                                         |
    //   | - This function sorts the input stack 'inputStack'.  |
    //   | - Uses an additional stack for sorting.              |
    //   | - Return type: void                                  |
    //   |                                                      |
    //   | Tips:                                                |
    //   | - Create an additional stack.                        |
    //   | - Pop elements from 'inputStack' and push them       |
    //   |   into 'additionalStack' in sorted order.            |
    //   | - Use a temporary variable to hold the top element   |
    //   |   of 'inputStack'.                                   |
    //   | - Move elements back to 'additionalStack' if needed. |
    //   | - Finally, move all elements back to 'inputStack'.   |
    //   | - Check output from Test.cpp in "User logs".         |
    //   +======================================================+

