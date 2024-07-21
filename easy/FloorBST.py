def floorInBST(root, X):

    f =-1

    while root is not None:

        if root.val==X:

            return X

        elif root.val <= X:

            f=root.val

            root = root.right

        else:

            root = root.left

    return f