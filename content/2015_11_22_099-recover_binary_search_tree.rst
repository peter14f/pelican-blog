099-recover_binary_search_tree
##############################

:date: 2015-11-22 21:15
:tags: Binary Search Trees, Morris Traversal
:category: LeetCode
:slug: 099-recover_binary_search_tree

`LeetCode Problem Link <https://leetcode.com/problems/recover-binary-search-tree/>`_

This problem brings up a problem that has been overlooked by me. That is the space complexity of a recursive
function. The space complexity of a recursive call is the number of calls on the stack. So for
inorder tree traversal, the space complexity is O(log n).

I am going to present the O(n) space solution first. The idea is to keep track of the previous node in
the inorder traversal. If ``prev`` is bigger than ``cur``, then we know there is problem. We insert both ``cur`` and
``prev`` into a list.

When the traversal is done, we either end up with 2 nodes in the list or 4 nodes in the list. In the 2 node case,
we simply swap the values of the two. In the 4 node case, we swap the values of the first node and the last node
only.

.. code-block:: java

    public void recoverTree(TreeNode root) {

        if (root==null)
            return;

        List<TreeNode> toSwap = new ArrayList<TreeNode>();

        inOrderTraversal(root, toSwap, new TreeNode[1]);

        System.out.println(toSwap.size());

        if (toSwap.size() == 2) {
            TreeNode a = toSwap.get(0);
            TreeNode b = toSwap.get(1);

            int tmp = a.val;
            a.val = b.val;
            b.val = tmp;
        }
        else if (toSwap.size() == 4) {
            TreeNode a = toSwap.get(0);
            TreeNode b = toSwap.get(3);

            int tmp = a.val;
            a.val = b.val;
            b.val = tmp;
        }
    }

    private void inOrderTraversal(TreeNode cur, List<TreeNode> toSwap, TreeNode[] prev) {
        if (cur==null)
            return;

        inOrderTraversal(cur.left, toSwap, prev);

        if (prev[0] != null) {
            if (prev[0].val > cur.val) {
                toSwap.add(prev[0]);
                toSwap.add(cur);
            }
        }

        prev[0] = cur;

        inOrderTraversal(cur.right, toSwap, prev);
    }

But LeetCode wants a solution that uses only O(1) space. We must use Morris traversal then.

.. code-block:: java

    public void recoverTree(TreeNode root) {

        TreeNode cur = root;
        TreeNode current = null;
        TreeNode prev = null;
        TreeNode toSwapA = null;
        TreeNode toSwapB = null;

        while (cur != null) {

            if (cur.left == null) {
                prev = current;
                current = cur;

                if (prev != null && current.val < prev.val) {
                    if (toSwapA == null) {
                        toSwapA = prev;
                    }
                    toSwapB = current;
                }

                cur = cur.right;
            }
            else {

                TreeNode t = cur.left;

                while (t.right != null && t.right != cur) {
                    t = t.right;
                }

                if (t.right == null) {
                    t.right = cur;
                    cur = cur.left;
                }
                else {
                    t.right = null;

                    prev = current;
                    current = cur;

                    if (prev != null && current.val < prev.val) {
                        if (toSwapA == null) {
                            toSwapA = prev;
                        }
                        toSwapB = current;
                    }

                    cur = cur.right;
                }

            }
        }

        if (toSwapA!=null && toSwapB!=null) {
            int tmp = toSwapA.val;
            toSwapA.val = toSwapB.val;
            toSwapB.val = tmp;
        }
    }