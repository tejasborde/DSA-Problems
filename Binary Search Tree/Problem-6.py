#Populate Inorder Successor for all Nodes

next=None
def populateNext(root):
    global next
    if(root):
        populateNext(root.right)
        root.next=next
        next=root 
        populateNext(root.left)


# void populate(Node *root,Node** next){
#     if (root) {
        
#         populate(root->right,next);
    
#         root->next = *next;
    
#         *next = root;
    
#         populate(root->left,next);
#     }
# }


# void populateNext(Node *root)
# {
#     Node* next = NULL;
#     populate(root,&next);

# }