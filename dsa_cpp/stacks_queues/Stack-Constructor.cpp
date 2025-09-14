#include <iostream>

using namespace std;

class Node {
    public:
        int value;
        Node* next;
        Node(int value) {
            this->value = value;
            next = nullptr;
        }
};

class Stack {
    private:
        Node* top;
        int height;
        
    public:
        Stack(int value) {
            Node* newNode = new Node(value);
            top = newNode;
            height = 1;
        }
        //   +=====================================================+
        //   |                 WRITE YOUR CODE HERE                |
        //   | Description:                                        |
        //   | - This is the constructor for the Stack class.      |
        //   | - It takes an integer value to initialize the stack |
        //   |   with a single node.                               |
        //   | - The method sets up the 'top' pointer and          |
        //   |   initializes the 'height' of the stack.            |
        //   | - Return type: n/a (constructor)                    |
        //   |                                                     |
        //   | Tips:                                               |
        //   | - Create a new Node object with the given value.    |
        //   | - Set 'top' to point to this new node.              |
        //   | - Set 'height' to 1 as there is one node.           |
        //   | - Check output from Test.cpp in "User logs".        |
        //   +=====================================================+

    
        ~Stack() {
            Node* temp = top;
            while (top) {
                top = top->next;
                delete temp;
                temp = top;
            }
        }
    
        void printStack() {
            Node* temp = top;
            while (temp) {
                cout << temp->value << endl;
                temp = temp->next;
            }
        }
    
        Node* getTop() {
            return top;
        }
    
        int getHeight() {
            return height;
        }
    
};


