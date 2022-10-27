#include <bits/stdc++.h>
using namespace std;

enum colour{RED, BLACK};
class node{
    public:
    int data;
    node* left = NULL;
    node* right = NULL;
    node* parent = NULL;
    colour col;
};

node* newNode(int data){
    node* temp = new node;
 
    temp->data = data;
 
    temp->left = NULL;
    temp->right = NULL;
 
    return temp;
}

node* TreeInsert(node* T, int key){
    node* y = NULL;
    node* x = T;
    node * z = newNode(key);
    while (x!=NULL)
    {
        y = x;
        if (z->data<x->data)
            x = x->left;
        else
            x = x->right;
    }
    z->parent = y;
    if (y==NULL)
        T = z;
    else{
        if(z->data<y->data){
            y->left=z;
        }else{
            y->right = z;
        }
    }
    return T;
}

node* TreeSearch(node* x, int k){
    while(x!=NULL && k!=x->data){
        if(k<x->data)
            x = x->left;
        else
            x = x->right;
    }
    return x;
}

void Inorder(node* root)
{
    if (root == NULL){
        return;
        }
    else {
        Inorder(root->left);
        cout << root->data << " ";
        Inorder(root->right);
    }
}

node* TreeMinimum(node* x){
    while(x->left!=NULL){
        x=x->left;
    }
    return x;
}

node* TreeMaximum(node* x){
    while(x->right!=NULL){
        x=x->right;
    }
    return x;
}

node* TreeSuccessor(node* x){
    if(x->right!=NULL)
        return TreeMinimum(x->right);
    node* y = x->parent;
    while(y!=NULL && x==y->right){
        x = y;
        y = y->parent;
    }
    return y;
}

void Transplant(node* root, node* u, node* v){
    if(u->parent==NULL)
        root = v;
    else{
        if(u==u->parent->left)
            u->parent->left = v;
        else
            u->parent->right = v;
    }
    if(v!=NULL)
        v->parent = u->parent;
}

void TreeDelete(node* root, int key){
    node* z = TreeSearch(root, key);
    if(z->left==NULL)
        Transplant(root, z, z->left);
    else{
        if(z->right==NULL)
            Transplant(root, z, z->right);
        else
        {
            node* y = TreeMinimum(z->right);
            if(y->parent!=z){
                Transplant(root, y, y->right);
                y->right =  z->right;
                y->right->parent = y;
            }
            Transplant(root, z, y);
            y->left = z->left;
            y->left = y;
        }
    }
    
}

void LeftRotate(node* root, node* x){
    node* y = x->right;
    x->right = y->left;
    if(y->left!=NULL)
        y->left->parent = x;
    y->parent = x->parent;
    if(x->parent==NULL)
        root = y;
    else{
        if(x==x->parent->left)
            x->parent->left=y;
        else
            x->parent->left = y;
    }
    y->left = x;
    x->parent = y;
}
int main(int argc, char const *argv[]){
    node* root = NULL;
    root = TreeInsert(root, 15);
    TreeInsert(root, 6);
    TreeInsert(root, 3);
    TreeInsert(root, 7);
    TreeInsert(root, 2);
    TreeInsert(root, 13);
    TreeInsert(root, 9);
    TreeInsert(root, 18);
    TreeInsert(root, 17);
    TreeInsert(root, 20);
    Inorder(root);
    cout<<"\n";
    LeftRotate(root, root->left);
    Inorder(root);
    cout<<"\n";
    return 0;
}
