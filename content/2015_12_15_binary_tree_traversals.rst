binary_tree_traversals
######################

:date: 2015-12-15 17:05
:tags: Binary Tree Traversals, Binary Trees
:category:
:slug: binary_tree_traversals

Here I will list the iterative ways to do binary tree traversals. Inorder and preorder traversals are more
striaghtforward whereas postorder traversal is a little more tricky.

Preorder traversal -

.. code-block:: java

    public List<Integer> preorder(TreeNode root) {
        List<Integer> nodes = new ArrayList<Integer>();

        TreeNode cur = root;
        Stack<TreeNode> stk = new Stack<TreeNode>();

        while (cur != null || !stk.isEmpty()) {
            if (cur != null) {
                nodes.add(cur.val);
                stk.push(cur);
                cur = cur.left;
            }
            else {
                TreeNode top = stk.pop();

                if (top.right != null) {
                    cur = top.right;
                }
                // else cur remains null
            }
        }

        return nodes;
    }

Inorder traversal -

.. code-block:: java

    public List<Integer> inorder(TreeNode root) {
        List<Integer> nodes = new ArrayList<Integer>();
        Stack<TreeNode> stk = new Stack<TreeNode>();

        TreeNode cur = root;

        while (cur != null || !stk.isEmpty()) {
            if (cur != null) {
                stk.push(cur);
                cur = cur.left;
            }
            else {
                TreeNode top = stk.pop();
                nodes.add(top.val);

                if (top.right != null) {
                    cur = top.right;
                }
            }
        }

        return nodes;
    }

Postorder traversal -

.. code-block:: java

    public List<Integer> postorder(TreeNode root) {
        List<Integer> nodes = new ArrayList<Integer>();

        TreeNode cur = root;
        Stack<TreeNode> stk = new Stack<TreeNode>();
        TreeNode prev = null;

        while (cur != null || !stk.isEmpty()) {

            if (cur != null) {
                stk.push(cur);
                cur = cur.left;
            }
            else {
                TreeNode top = stk.peek();

                if (top.right != null && top.right != prev) {
                    cur = top.right;
                }
                else {
                    stk.pop();
                    nodes.add(top.val);
                    prev = top;
                }
            }

        }

        return nodes;
    }

Note that the conditions in the while loop for all 3 traversals are all the same. Postorder traversal requires the
``prev`` pointer which records the last node traversed. And the condition to move to the right child is ``top.right !=
null && prev != top.right``.
