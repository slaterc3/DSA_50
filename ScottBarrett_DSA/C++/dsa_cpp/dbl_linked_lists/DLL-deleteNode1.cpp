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
        // It will be used to make sure deleteNode works with an empty DLL.
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
            if (temp) {
                temp->value = value;
                return true;
            }
            return false;
        }
        
        bool insert(int index, int value) {
            if (index < 0 || index > length) return false;
            if (index == 0) {
                prepend(value);
                return true;
            } 
            if (index == length) {
                append(value);
                return true;
            } 
        
            Node* newNode = new Node(value);
            Node* before = get(index - 1);
            Node* after = before->next;
            newNode->prev = before;
            newNode->next = after;
            before->next = newNode;
            after->prev = newNode;
            length++;
            return true;
        }
        
        void deleteNode(int index) {
            if (index < 0 || index >= length) return;
            
            if (index == 0) {
                deleteFirst();
                return;
            }
            if (index == length-1) {
                deleteLast();
                return;
            } else {
                Node* temp = get(index);
                Node* prevNode = temp->prev;
                Node* nextNode = temp->next;
                
                prevNode->next = nextNode;
                nextNode->prev = prevNode;
                
                temp->next = nullptr;
                temp->prev = nullptr;
                
                delete temp;
                length--;
            }
        }
        
        //   +=====================================================+
        //   |                 WRITE YOUR CODE HERE                |
        //   | Description:                                        |
        //   | - Write code to delete a node at a specific index   |
        //   |   in the doubly linked list.                        |
        //   | - Return type: void                                 |
        //   |                                                     |
        //   | Tips:                                               |
        //   | - Check if the index is valid. Return if not.       |
        //   | - Use 'deleteFirst' if index is 0.                  |
        //   | - Use 'deleteLast' if index is at the end.          |
        //   | - Otherwise, find the node at the index.            |
        //   | - Update pointers of adjacent nodes.                |
        //   | - Delete the node and decrease length by 1.         |
        //   | - Check output from Test.cpp in "User logs".        |
        //   +=====================================================+

};


