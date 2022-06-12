
#Find Least Common Ancestor of Two Nodes

# def LCA(root, n1, n2):
    
#     node=root
    
#     while(node):
#         if(node.data>n1 and node.data<n2):
#             return node
#         elif(node.data>n1 and node.data>n2):
#             node=node.left
#         elif(node.data<n1 and node.data<n2):
#             node=node.right
#         else:
#             return node