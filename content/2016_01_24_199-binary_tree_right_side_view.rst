199-binary_tree_right_side_view
###############################

:date: 2016-1-24 13:08
:tags: Binary Trees, Level Order Traversal
:category: LeetCode
:slug: 199-binary_tree_right_side_view

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-right-side-view/>`_

Can solve it the same way we solved 102-binary_tree_level_order_traversal.

Just need to be aware that going to the right child from root does not get you the answer.

.. code-block:: java

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new ArrayList<Integer>();

        List<TreeNode> q = new ArrayList<TreeNode>();

        if (root != null)
            q.add(root);

        while (!q.isEmpty()) {
            int curLevelSize = q.size();

            for (int i=0; i<curLevelSize; i++) {
                TreeNode node = q.get(i);

                if (node.left != null)
                    q.add(node.left);
                if (node.right != null)
                    q.add(node.right);
            }

            ans.add(q.get(curLevelSize-1).val);

            for (int i=0; i<curLevelSize; i++) {
                q.remove(0);
            }
        }

        return ans;
    }

Every node is traversed, so this takes O(n) time.
