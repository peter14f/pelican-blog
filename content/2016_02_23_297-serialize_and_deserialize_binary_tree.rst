297-serialize_and_deserialize_binary_tree
#########################################

:date: 2016-2-23 2:29
:tags: Serialization
:category: LeetCode
:slug: 297-serialize_and_deserialize_binary_tree

`LeetCode Problem Link <https://leetcode.com/problems/serialize-and-deserialize-binary-tree/>`_

Using level order traversal and for each non-null node, also specify its left child and right child even
if they are null.

I separate each node strings with ','

.. code-block:: java

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuffer sb = new StringBuffer();

        TreeNode cur = root;

        Queue<TreeNode> q = new LinkedList<TreeNode>();

        q.offer(cur);

        while (!q.isEmpty()) {
            TreeNode n = q.poll();

            if (n == null) {
                sb.append("null");
                sb.append(",");
                continue;
            }

            sb.append(n.val);
            sb.append(",");

            q.offer(n.left);
            q.offer(n.right);
        }

        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        TreeNode root = null;
        Queue<TreeNode> q = new LinkedList<TreeNode>();

        int start = 0;
        int end = 0;

        while (start < data.length()) {
            if (data.charAt(end) != ',') {
                end++;
                continue;
            }

            String s = data.substring(start, end);

            if (root==null) {
                if (s.equals("null"))
                    return null;
                else {
                    root = new TreeNode(Integer.parseInt(s));
                    q.offer(root);
                }
            }
            else {
                TreeNode node = q.poll();

                if (!s.equals("null")) {
                    node.left = new TreeNode(Integer.parseInt(s));
                    q.offer(node.left);
                }

                start = end+1;
                end = start;

                while (data.charAt(end) != ',')
                    end++;

                String rightStr = data.substring(start, end);

                if (!rightStr.equals("null")) {
                    node.right = new TreeNode(Integer.parseInt(rightStr));
                    q.offer(node.right);
                }
            }

            start = end+1;
            end = start;
        }

        return root;
    }


