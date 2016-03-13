101-symmetric_tree
##################

:date: 2015-11-24 19:54
:tags: Binary Trees, Recursion
:category: LeetCode
:slug: 101-symmetric_tree

`LeetCode Problem Link <https://leetcode.com/problems/symmetric-tree/>`_

Let me first show the recursive solution.

The method ``isSymmetric()`` takes two arguments, the ``left`` child and the ``right`` child from the parent.
We must recursively check that the outer nodes (left child of ``left`` and right child of ``right``) and the
innter nodes (right child of ``left`` and left child of ``child``) contain the same values.

.. code-block:: java

    public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;

        return isSymmetric(root.left, root.right);
    }

    private boolean isSymmetric(TreeNode a, TreeNode b) {
        if (a == null && b==null)
            return true;

        if ((a == null && b != null) || (a != null && b == null)) {
            return false;
        }

        // a and b not null
        if (a.val != b.val)
            return false;

        //     check outside                   check inside
        return isSymmetric(a.left, b.right) && isSymmetric(a.right, b.left);
    }

I was asked to do this iteratively as well. If you simply use two references ``left`` and ``right`` and try to
compare their values, that would only get you to the second level.

So I immediately thought of using the level order traversal.

::

                  3
                 / \
                1   1
               / \ / \
              4  5 5 4
                /   \
                2   2

What did you notice about the nodes in each level. They look like a palindrome - meaning if you
read the values from left to right, you will get the same result reading the values from right to
left.

.. code-block:: java

    public boolean isSymmetric(TreeNode root) {
        if (root==null)
            return true;

        LinkedList<TreeNode> curLevel = new LinkedList<TreeNode>();
        LinkedList<TreeNode> nextLevel = new LinkedList<TreeNode>();

        curLevel.add(root);

        while (!curLevel.isEmpty()) {

            // go thru nodes in curLevel left -> right and
            // right -> left should be the same

            int l = 0;
            int r = curLevel.size()-1;

            while (r >= l) {
                TreeNode left = curLevel.get(l);
                TreeNode right = curLevel.get(r);

                if ((left==null && right != null) || (left!=null && right==null) ||
                        (left!=null && right!=null && left.val != right.val)) {
                    return false;
                }

                l++;
                r--;
            }

            int size = curLevel.size();

            for (int i=0; i<size; i++) {
                TreeNode node = curLevel.removeFirst();

                if (node != null) {
                    nextLevel.add(node.left);
                    nextLevel.add(node.right);
                }
            }

            // curLevel is now empty
            // swap curLevel and nextLevel

            LinkedList<TreeNode> empty = curLevel;
            curLevel = nextLevel;
            nextLevel = empty;
        }

        return true;
    }
