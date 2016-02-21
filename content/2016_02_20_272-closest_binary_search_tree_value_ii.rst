272-closest_binary_search_tree_value_ii
#######################################

:date: 2016-2-20 11:18
:tags: Binary Search Trees, Closest Value In BST
:category: LeetCode
:slug: 272-closest_binary_search_tree_value_ii

`LeetCode Problem Link <https://leetcode.com/problems/closest-binary-search-tree-value-ii/>`_

The problem seems very intimidating at first. Reading the followup question right away does not help either.

What you need is to use a simple BST as an example.

::

           7
          / \
         5   8
        /     \
       3       10
      /         \
     1          25



Say ``target`` is 7 and ``k`` is 4, the the answer should be

::

[7, 5, 8, 10]


The straightforward solution would be first get the preorder traversal of the BST.
We know that the preorder traversal results in a sorted list.
In this case, the preorder traversal results in

::

[1, 3, 5, 7, 8, 10, 25]

Find the element closest to target, record the index of that element, call it ``minIndex``.

If ``k=1``, that's the only element you need.

If ``k<1``, then use pointers ``i``, and ``j`` to point to the next smaller and bigger element.

Initialize ``i`` to ``minIndex-1`` and ``j`` to ``minIndex+1``.

Insert whichever element closer to ``target`` and move the pointer accordingly.

The time complexity is O(n) since we need to get the preorder traversal of the BST.

.. code-block:: java

    // assume k is valid
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        List<Integer> sorted = new ArrayList<Integer>();
        List<Integer> kValues = new ArrayList<Integer>();

        inorderTraversal(root, sorted);

        double minDiff = Double.MAX_VALUE;
        int minIndex = -1;

        for (int i=0; i<sorted.size(); i++) {
            double diff = Math.abs(sorted.get(i) - target);
            if (diff < minDiff) {
                minDiff = diff;
                minIndex = i;
            }
        }

        int i = minIndex;
        int j = minIndex+1;

        while (kValues.size() < k) {
            if (i >= 0 && j < sorted.size()) {
                double diffI = Math.abs(target - sorted.get(i));
                double diffJ = Math.abs(target - sorted.get(j));

                if (diffI <= diffJ) {
                    kValues.add(sorted.get(i));
                    i--;
                }
                else {
                    kValues.add(sorted.get(j));
                    j++;
                }
            }
            else if (i >= 0) {
                kValues.add(sorted.get(i));
                i--;
            }
            else {
                kValues.add(sorted.get(j));
                j++;
            }
        }

        return kValues;
    }

    private void inorderTraversal(TreeNode node, List<Integer> sorted) {
        if (node == null)
            return;

        inorderTraversal(node.left, sorted);
        sorted.add(node.val);
        inorderTraversal(node.right, sorted);
    }

Now the followup asks us

::

    Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

What we want is two stacks one with values <= target, and the other with value > target.

The two stacks must store the values in sorted order with top element closer to ``target``.

.. code-block:: java

    public List<Integer> closestKValues(TreeNode root, double target, int k) {

        Stack<Integer> preStk = new Stack<Integer>();
        Stack<Integer> sucStk = new Stack<Integer>();

        List<Integer> ans = new ArrayList<Integer>();

        getPredeccesors(root, target, preStk);
        getSuccessors(root, target, sucStk);

        while (ans.size() < k) {

            if (!preStk.isEmpty() && !sucStk.isEmpty()) {
                int smaller = preStk.peek();
                int bigger = sucStk.peek();

                double diff1 = Math.abs(target - smaller);
                double diff2 = Math.abs(target - bigger);

                if (diff1 <= diff2)
                    ans.add(preStk.pop());
                else
                    ans.add(sucStk.pop());
            }
            else if (!preStk.isEmpty()) {
                ans.add(preStk.pop());
            }
            else if (!sucStk.isEmpty()) {
                ans.add(sucStk.pop());
            }
            else {
                // this means k is larger than n
                break;
            }
        }

        return ans;
    }

    // predeccesor are node values <= taget
    private void getPredeccesors(TreeNode node, double target, Stack<Integer> preStk) {
        if (node == null)
            return;

        getPredeccesors(node.left, target, preStk);

        if (node.val > target)
            return;

        preStk.push(node.val);

        getPredeccesors(node.right, target, preStk);
    }

    private void getSuccessors(TreeNode node, double target, Stack<Integer> sucStk) {
        if (node == null)
            return;

        getSuccessors(node.right, target, sucStk);

        if (node.val <= target)
            return;

        sucStk.push(node.val);

        getSuccessors(node.left, target, sucStk);
    }

What's the time complexity?

::

    log(h) + k


