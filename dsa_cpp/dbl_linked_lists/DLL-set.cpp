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
        // It will be used to make sure set works with an empty DLL.
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
    
        void deleteLast() {
            if (length == 0) return;
            Node* temp = tail;
            if (length == 1) {
                head = nullptr;
                tail = nullptr;
            } else {
                tail = tail->prev;
                tail->next = nullptr;
            }
            delete temp;
            length--;
        }
    
        void prepend(int value) {
            Node* newNode = new Node(value);
            if (length == 0) {
                head = newNode;
                tail = newNode;
            } else {
                newNode->next = head;
                head->prev = newNode;
                head = newNode;
            }
            length++;
        }
    
        void deleteFirst() {
            if (length == 0) return;
            Node* temp = head;
            if (length == 1) {
                head = nullptr;
                tail = nullptr;
            } else {
                head = head->next;
                head->prev = nullptr;
            }
            delete temp;
            length--;
        }
    
        Node* get(int index) {
            if (index < 0 || index >= length) return nullptr;
            Node* temp = head;
            if (index < length/2) {
                for (int i = 0; i < index; ++i) {
                    temp = temp->next;
                }
            } else {
                temp = tail;
                for (int i = length - 1; i > index; --i) {
                    temp = temp->prev;
                }
            }
            return temp;
        }
        
        bool set(int index, int value) {
            Node* temp = get(index);
            if (temp != nullptr){
                temp->value = value;
                return true;
            } 
            return false;
        }
        
        //   +=====================================================+
        //   |                 WRITE YOUR CODE HERE                |
        //   | Description:                                        |
        //   | - Write code to set the value of a node at a        |
        //   |   specific index in the doubly linked list.         |
        //   | - Return type: bool (True if success, False         |
        //   |   otherwise)                                       |
        //   |                                                     |
        //   | Tips:                                               |
        //   | - Use the 'get' method to find the node to update.  |
        //   | - If index is invalid, return false.                |
        //   | - If successful, set the node value and return      |
        //   |   true.                                             |
        //   | - Check output from Test.cpp in "User logs".        |
        //   +=====================================================+
    
};


