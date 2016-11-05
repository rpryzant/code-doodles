"""

Given a preorder and inorder traversals of a binary tree with unique numbers, reconstruct the original tree, and return a pointer to the root node. Analyze runtime and space complexity




3 5 2 6 1 4

6 5 3 2 4 1





"""






def makeTree(inorder, preorder):
    if not inorder or not preorder:
        return None
    if len(inorder) == len(preorder) == 1:
        return Node(inorder[0])

    rt = Node(preoder[0])

    isp = inorder.index(preorder[0])
    inl, inr = in[:isp], in[isp+1:]

    psp = next((i if preorder[i] not in l for i in range(1, len(preorder))))
    prel, prer = preorder[1:psp], preorder[psp:]

    l, r = makeTree(inl, prel), makeTree(inr, prer)
    rt.l = l
    rt.r = r
    
    return rt
