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

class LinkedList {
    private:
        Node* head;
        int length;
        
    public:
        LinkedList(int value) {
            Node* newNode = new Node(value);
            head = newNode;
            length = 1;
        }
    
        ~LinkedList() {
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
                cout << "empty";
            } else {
                while (temp != nullptr) {
                    cout << temp->value;
                    temp = temp->next;
                    if (temp != nullptr) {
                        cout << " -> ";
                    }
                }
            }
            cout << endl;
        }

        Node* getHead() {
            return head;
        }

        int getLength() {
            return length;
        }
        
        void makeEmpty() {
            Node* temp = head;
            while (head) {
                head = head->next;
                delete temp;
                temp = head;
            }
            length = 0;
        }
    
        void append(int value) {
            Node* newNode = new Node(value);
            if (head == nullptr) {
                head = newNode;
            } else {
                Node* currentNode = head;
                while (currentNode->next != nullptr) {
                    currentNode = currentNode->next;
                }
                currentNode->next = newNode;
            }
            length++;
        }
        
        void swapPairs() {
            
            if (length <= 1) return;
            
            Node* dummy = new Node(0);
            // dummy->next = head;
            
            Node* prev = dummy;
            prev->next = head;
            Node* curr = head;
            int count = 0;
            
            while (count < length && curr->next){
                Node* toMove = curr->next;
                prev->next = toMove;
                curr->next = toMove->next;
                toMove->next = curr;
                
                prev = curr;
                curr = curr->next;
                
                count = count + 2;
            }
            
            head = dummy->next;
            dummy->next = nullptr;
            delete dummy;
            //   +===================================================+
            //   |               WRITE YOUR CODE HERE                |
            //   | Description:                                      |
            //   | - Swaps every two adjacent nodes in a singly      |
            //   |   linked list.                                    |
            //   | - The list is modified in place without altering  |
            //   |   node values or creating new nodes (except dummy)|
            //   |                                                   |
            //   | Behavior:                                         |
            //   | - A dummy node is used to simplify swapping at    |
            //   |   the head.                                       |
            //   | - In each loop, the `first` and `second` nodes    |
            //   |   are swapped by adjusting their `.next` links.   |
            //   | - The `previous` pointer tracks the node before   |
            //   |   the pair and is updated after each swap.        |
            //   | - At the end, `head` is reassigned to point to    |
            //   |   the new head after all swaps.                   |
            //   +===================================================+
        }
        
};


