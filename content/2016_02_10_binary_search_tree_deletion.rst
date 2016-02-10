binary_search_tree_deletion
###########################

:date: 2016-2-10 23:07
:tags: Binary Search Trees
:category:
:slug: binary_search_tree_deletion

While doing the problem 230-kth_smallest_element_in_a_bst, I realized I was forgetting what to do when
trying to delete from a BST.

Deleting leaf nodes are trivial. Deleting nodes with only one child is also trivial.

What happens when we need to delete a node with two children?

What we have to remember is that for any given node in a BST, the two values closest to it is the largest value
in its left subtree and the smallest value in its right subtree.

Replace the node's value with either of the two first, and then look for the replaced node and then delete that
node. Both the largest value in the left subtree and the smaller value in the right subtree must be leaf nodes,
so deleting them is again trivial.
