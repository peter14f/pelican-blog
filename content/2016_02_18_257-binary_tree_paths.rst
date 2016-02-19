257-binary_tree_paths
#####################

:date: 2016-2-18 18:51
:tags: DFS, Recursion
:category: LeetCode
:slug: 257-binary_tree_paths

`LeetCode Problem Link <https://leetcode.com/problems/binary-tree-paths/>`_

Need a List<Integer> that stores the current path.
Each node is visited once, so the time complexity should be O(n)

.. code-block:: java

    public List<String> binaryTreePaths(TreeNode root) {

        List<String> paths = new ArrayList<String>();

        List<Integer> curPath = new ArrayList<Integer>();

        if (root != null)
            dfsFindPathToLeaf(root, curPath, paths);

        return paths;
    }

    private void dfsFindPathToLeaf(TreeNode node,
                                    List<Integer> curPath,
                                    List<String> paths) {

        curPath.add(node.val);

        if (node.left==null && node.right==null) {
            StringBuffer sb = new StringBuffer();

            sb.append(curPath.get(0));

            for (int i=1; i<curPath.size(); i++) {
                sb.append("->");
                sb.append(curPath.get(i));
            }
            paths.add(sb.toString());
        }

        if (node.left != null) {
            dfsFindPathToLeaf(node.left, curPath, paths);
        }

        if (node.right != null) {
            dfsFindPathToLeaf(node.right, curPath, paths);
        }

        curPath.remove(curPath.size()-1);
    }
