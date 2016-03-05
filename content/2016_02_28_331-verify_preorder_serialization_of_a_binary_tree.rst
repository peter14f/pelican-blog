331-verify_preorder_serialization_of_a_binary_tree
##################################################

:date: 2016-2-28 21:29
:tags: Preorder Traversal
:category: LeetCode
:slug: 331-verify_preorder_serialization_of_a_binary_tree

`LeetCode Problem Link <https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/>`_

The first method relies on the observation that in a preorder sequence, a leaf node always results in
``x, #, #``. For any given binary tree, you should always be able to continue removing the
existing leaf nodes until you obtain an empty tree.

So what we can do is keep replace ``x, #, #`` with ``#`` and see if we end up with ``#``.

An example

::

        a
       / \
      b   c


    [a, b, #, #, c, #, #]
    [a, #, c, #, #]
    [a, #, #]
    [#]


.. code-block:: java

    public boolean isValidSerialization(String preorder) {
        //  1234
        //"x,#,#"


        boolean foundLeaf = false;
        while (true) {
            //System.out.println(preorder);

            for (int i=1; i< preorder.length(); i++) {
                //System.out.println(" i=" + i + " " + preorder.substring(i, i+4));
                if (i + 4 <= preorder.length() &&
                        preorder.substring(i, i+4).equals(",#,#")) {

                    int j = i-1;

                    while (j >= 0 && preorder.charAt(j) != ',') {
                        j--;
                    }

                    j= j+1;

                    preorder =  preorder.substring(0, j) + "#" + preorder.substring(i+4);
                    foundLeaf = true;
                    break;
                }
            }

            if (foundLeaf == false) {
                if (preorder.length() == 1 && preorder.equals("#"))
                    return true;
                break;
            }
            else {
                foundLeaf = false; // reset to false
            }
        }

        return false;
    }
