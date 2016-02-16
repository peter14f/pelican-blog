236-lowest_common_ancestor_of_a_binary_tree
###########################################

:date: 2016-2-15 22:32
:tags: Binary Trees, Common Ancestor
:category: LeetCode
:slug: 236-lowest_common_ancestor_of_a_binary_tree

`LeetCode Problem Link <https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/>`_

My original thought is too check if ``p`` is on the left or the right of the current node and if ``q`` is on the
left or the right of the current node starting from the current node. It is quite clear that this approach would
take O(h\ :superscript:`2`) since in the very worst case ``p`` and ``q`` could be two deepest leaf nodes that
share the same parent. Note that ``findNode()`` returns a boolean.

.. code-block:: java

     /* the given nodes p and q are in the binary tree */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null)
            return null;

        if (root == p || root == q) {
            // since we're guaranteed that the other node must also be in the binary tree
            return root;
        }

        boolean pInLeft = findNode(root.left, p);
        boolean qInLeft = findNode(root.left, q);

        if (pInLeft && qInLeft) {
            return lowestCommonAncestor(root.left, p, q);
        }
        else if (pInLeft && !qInLeft) {
            return root;
        }
        else if (!pInLeft && qInLeft) {
            return root;
        }
        else {
            return lowestCommonAncestor(root.right, p, q);
        }
    }

    private boolean findNode(TreeNode root, TreeNode node) {

        if (root == null)
            return false;

        if (root == node)
            return true;

        if (findNode(root.left, node)) {
            return true;
        }
        else {
            return findNode(root.right, node);
        }
    }

How could we do better? We have to use a bottom-approach that will prevent us from traversing to ``p`` or ``q`` more
that once.

.. code-block:: java

    // this is bottom up approach that takes O(n) time
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null)
            return null;

        if (root == p || root == q) {
            return root;
        }

        TreeNode l = lowestCommonAncestor(root.left, p, q);
        TreeNode r = lowestCommonAncestor(root.right, p, q);

        if (l != null && r != null) {
            // found one in left subtree, found one in right subtree
            return root;
        }
        else if (l != null) {
            // found both in right subtree
            return l;
        }
        else if (r != null) {
            // found both in left subtree
            return r;
        }

        return null;
    }

