173-binary_search_tree_iterator
###############################

:date: 2016-1-17 23:31
:tags: Binary Search Trees
:category: LeetCode
:slug: 173-binary_search_tree_iterator

`LeetCode Problem Link <https://leetcode.com/problems/binary-search-tree-iterator/>`_

We asked to implement the inorder traversal iterator of a binary tree.
The only field the Iterator needs is a Stack.

.. code-block:: java

    public class BSTIterator {
        Stack<TreeNode> stk;

        public BSTIterator(TreeNode root) {
            stk = new Stack<TreeNode>();
            while (root != null) {
                stk.push(root);
                root = root.left;
            }
        }

        /** @return whether we have a next smallest number */
        public boolean hasNext() {
            return !stk.isEmpty();
        }

        /** @return the next smallest number */
        public int next() {
            TreeNode node = stk.pop();
            TreeNode t = node.right;

            while (t != null) {
                stk.push(t);
                t = t.left;
            }

            return node.val;
        }
    }
