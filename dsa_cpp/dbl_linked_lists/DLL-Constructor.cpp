#include <iostream>

using namespace std;

class Node { 
    public: 
        int value;
        Node* next;
        Node* prev;
    
        Node(int value) {
            this->value = value;
            next = nullptr;
            prev = nullptr;
        }
};

class DoublyLinkedList {
    private:
        Node* head;
        Node* tail;
        int length;
    
    public:
        DoublyLinkedList(int value) {
            Node* newNode = new Node(value);
            head = newNode;
            tail = newNode;
            length = 1;
        }
        //   +=====================================================+
        //   |                 WRITE YOUR CODE HERE                |
        //   | Description:                                        |
        //   | - This is the constructor for DoublyLinkedList.     |
        //   | - It takes an integer value to initialize the list. |
        //   | - The method sets up the head and tail pointers     |
        //   |   and initializes the list length.                  |
        //   | - Return type: n/a (constructor)                    |
        //   |                                                     |
        //   | Tips:                                               |
        //   | - Create a new Node object with the given value.    |
        //   | - Set 'head' and 'tail' to point to this new node.  |
        //   | - Set 'length' to 1 as there is one node.           |
        //   | - Check output from Test.cpp in "User logs".        |
        //   +=====================================================+


        ~DoublyLinkedList() {
            Node* temp = head;
            while (head) {
                head = head->next;
                delete temp;
                temp = head;
            }
        }
    
        void printList() {
            Node* temp = head;
            if (temp == nullptr) {
                cout << "empty" << endl;
                return;
            }
            while (temp->next != nullptr) {
                cout << temp->value << " <-> ";
                temp = temp->next;
            }
            cout << temp->value << endl;
        }
    
        Node* getHead() {
            return head;
        }
    
        Node* getTail() {
            return tail;
        }
    
        int getLength() {
            return length;
        }

};


