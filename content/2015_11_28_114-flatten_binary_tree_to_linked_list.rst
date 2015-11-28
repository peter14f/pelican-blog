114-flatten_binary_tree_to_linked_list
######################################

:date: 2015-11-28 15:25
:tags: Recursion, Binary Trees
:category: LeetCode
:slug: 114-flatten_binary_tree_to_linked_list

`LeetCode Problem Link <https://leetcode.com/problems/flatten-binary-tree-to-linked-list/>`_

Recursion is the way to go here. We do however have to know the preorder traversal predecessor of the current node
though.

.. code-block:: java

    public void flatten(TreeNode root) {

        TreeNode[] prev = new TreeNode[1];
        prev[0] = null;

        flatten(root, prev);
    }

    private void flatten(TreeNode node, TreeNode[] prev) {
        if (prev[0] != null) {
            prev[0].right = node;
            prev[0].left = null;
        }

        prev[0] = node;

        TreeNode rightChild = node.right;

        if (node.left != null)
            flatten(node.left, prev);

        if (rightChild != null)
            flatten(rightChild, prev);
    }
