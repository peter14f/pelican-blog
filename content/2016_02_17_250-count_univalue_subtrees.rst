250-count_univalue_subtrees
###########################

:date: 2016-2-17 23:22
:tags: Recursion, Binary Trees, Univalue Trees
:category: LeetCode
:slug: 250-count_univalue_subtrees

`LeetCode Problem Link <https://leetcode.com/problems/count-univalue-subtrees/>`_

Use recursion and an int array so that I can increment count and preserve the changes across recursive calls.

.. code-block:: java

    // empty tree is not considered a unival tree
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null)
            return 0;

        int[] cnt = {0};

        isUnivalSubtree(root, cnt);

        return cnt[0];
    }

    private boolean isUnivalSubtree(TreeNode root, int[] cnt) {
        //System.out.println(root.val + " " + root);

        if (root.left == null && root.right == null) {
            //System.out.println("leaf");
            cnt[0]++;
            return true;
        }
        else if (root.left == null && root.right != null) {
            if (isUnivalSubtree(root.right, cnt) && root.val == root.right.val) {
                cnt[0]++;
                return true;
            }
        }
        else if (root.left != null && root.right == null) {
            if (isUnivalSubtree(root.left, cnt) && root.val == root.left.val) {
                cnt[0]++;
                return true;
            }
        }
        else {
            boolean l = isUnivalSubtree(root.left, cnt);
            boolean r = isUnivalSubtree(root.right, cnt);

            if (l &&
                    r &&
                    root.val == root.left.val &&
                    root.val == root.right.val) {
                cnt[0]++;
                return true;
            }
        }

        return false;
    }
