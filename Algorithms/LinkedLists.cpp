#include <iostream>
using namespace std;
class Node{
    public:
    int data;
    Node * next;
    Node * prev;
};

void insert(Node ** head, int x){
    Node* node = (struct Node*) malloc(sizeof(struct Node));
    node->data = x;
    node->prev = NULL;
    node->next = (*head);
    if(*head!=NULL){
        (*head)->prev = node;
    }
    (*head) = node;
}
void display(Node * head) {
   struct Node* ptr;
   ptr = head;
   while(ptr != NULL) {
      cout<< ptr->data <<" ";
      ptr = ptr->next;
   }
   cout<<"\n";
}
int main() {
    Node * head = NULL;
    insert(&head,3);
    insert(&head, 1);
    insert(&head, 7);
    insert(&head, 2);
    insert(&head, 9);
    cout<<"The doubly linked list is: ";
    display(head);
    return 0;
}