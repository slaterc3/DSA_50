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
        
        // This method will make the DLL empty.
        // It will be used to make sure deleteLast works with an empty DLL.
        void makeEmpty() {
            Node* current = head;
            while (current != nullptr) {
                Node* nodeToDelete = current;
                current = current->next;
                delete nodeToDelete;
            }
            head = nullptr;
            tail = nullptr;
            length = 0;
        }
        
        void append(int value) {
            Node* newNode = new Node(value);
            if (length == 0) {
                head = newNode;
                tail = newNode;
            } else {
                tail->next = newNode;
                newNode->prev = tail;
                tail = newNode;
            }
            length++;
        }
        
        void deleteLast(){
            if (length == 0) return;
            
            Node* temp = tail;
            
            if (length == 1) {
                head = nullptr;
                tail = nullptr;
                // delete head;
            } else {
                tail = tail->prev;
                tail->next = nullptr;
            }
            delete temp;
            
            length--;
            
            
        }
        
        //   +=====================================================+
        //   |                 WRITE YOUR CODE HERE                |
        //   | Description:                                        |
        //   | - Write code to delete the last node of the doubly  |
        //   |   linked list                                       |
        //   | - Return type: void                                 |
        //   |                                                     |
        //   | Tips:                                               |
        //   | - If the list is empty, return immediately          |
        //   | - Update the 'tail' and 'prev' pointers             |
        //   | - Remember to delete the node and update 'length'   |
        //   | - Check output from Test.cpp in "User logs"         |
        //   +=====================================================+
    
};


