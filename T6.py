def generate_postorder(inorder_seq, preorder_seq):
    if not inorder_seq or not preorder_seq:
        return []

    root_node = preorder_seq[0]  
    root_index = inorder_seq.index(root_node)
    
    left_subtree = generate_postorder(inorder_seq[:root_index], preorder_seq[1:root_index+1])
    right_subtree = generate_postorder(inorder_seq[root_index+1:], preorder_seq[root_index+1:])
    
    return left_subtree + right_subtree + [root_node]

num_nodes = int(input())
inorder_seq = list(map(int, input().split()))
preorder_seq = list(map(int, input().split()))
postorder_seq = generate_postorder(inorder_seq, preorder_seq)
print(' '.join(map(str, postorder_seq)))

