285-inorder_successor_in_bst
############################

:date: 2016-2-22 7:08
:tags: Binary Search Trees
:category: LeetCode
:slug: 285-inorder_successor_in_bst

`LeetCode Problem Link <https://leetcode.com/problems/inorder-successor-in-bst/>`_

Seems like for the test cases on OJ, we can assume that ``p`` is in the BST.

If that's the case, then we can use the approach to find the successors as in 272-closest_binary_search_tree_values_ii.

We use a stack to store nodes that are larger than p. And the top of the stack contains the closest value
that's larger. That will be successor node if ``p`` is indeed in the BST.

.. code-block:: java

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {

        Stack<TreeNode> stk = new Stack<TreeNode>();

        findSuccessors(root, p.val, stk);

        if (stk.isEmpty())
            return null;

        return stk.peek();
    }

    private void findSuccessors(
            TreeNode node,
            int v,
            Stack<TreeNode> stk) {

        if (node == null)
            return;

        findSuccessors(node.right, v, stk);

        if (node.val <= v)
            return;

        stk.push(node);

        findSuccessors(node.left, v, stk);
    }

In fact, since we only care about the successor, we don't need a stack. We just need the storage space for one
node.

.. code-block:: java

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {

        Stack<TreeNode> stk = new Stack<TreeNode>();

        findSuccessors(root, p.val, stk);

        if (stk.isEmpty())
            return null;

        return stk.peek();
    }

    private void findSuccessors(
            TreeNode node,
            int v,
            Stack<TreeNode> stk) {

        if (node == null)
            return;

        findSuccessors(node.right, v, stk);

        if (node.val <= v)
            return;

        stk.push(node);

        findSuccessors(node.left, v, stk);
    }

Well, here's another recursive solution that simply does the inorder traversal and if p is previously traversed
node, we just return the next node. This solution is good even if ``p`` is not found in the BST. ``null`` will be
returned in that case.

.. code-block:: java

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        TreeNode[] prev = {null};
        TreeNode successor = inorder(root, prev, p);
        return successor;
    }

    private TreeNode inorder(TreeNode node, TreeNode[] prev, TreeNode p) {

        if (node == null)
            return null;

        TreeNode leftResult = inorder(node.left, prev, p);

        if (leftResult != null)
            return leftResult;

        if (prev[0] == p)
            return node;

        prev[0] = node;

        TreeNode rightResult = inorder(node.right, prev, p);

        return rightResult;
    }

Here's another solution. We look at two cases.

1) p has a right child: Then find the smallest node in the right subtree.
2) p does not have a right child: Then need to find the smallest node that's larger than p.

.. code-block:: java

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {

        if (p.right != null) {
            // return the smallest node in the right subtree

            TreeNode node = p.right;

            while (node.left != null) {
                node = node.left;
            }

            return node;
        }
        else {
            // need to find the smallest node that's bigger than p

            TreeNode node = root;
            TreeNode successor = null;

            while (node != null) {

                if (node.val > p.val) {
                    // record it
                    successor = node;

                    // want to see if a smaller node that's bigger than p exists
                    node = node.left;
                }
                else if (node.val <= p.val) {
                    // nodes smaller are not of interest
                    // find bigger nodes
                    node = node.right;
                }
            }

            return successor;
        }
    }

This last solution is O(h) time and O(1) space since no stacks and no recursion were used.