027-remove_element
##################

:date: 2015-09-07 20:29
:tags: Remove Elements, Remove Elements In Arrays
:category: LeetCode
:slug: 027-remove_element

`LeetCode Problem Link <https://leetcode.com/problems/remove-element/>`_

We are asked to remove elements of the specified value in the array. We must return the new length or the array.

Basically we want these elements to be moved to the end of the array.

.. code-block:: java

    public int removeElement(int[] nums, int val) {

        if (nums==null || nums.length==0)
            return 0;

        int h=nums.length - 1;

        while (val >=0 && nums[h] == val) {
            h--;
        }

        for (int i=0; i<h; i++) {
            if (nums[i]==val) {
                nums[i] = nums[h];
                h--;
                while (nums[h] == val && val >=0) {
                    h--;
                }
            }
        }

        return h+1;
    }


This method requires fewer number of writes than the 2nd method presented here.
The second basically write each number seen that's not ``val`` from the beginning of the array.

.. code-block:: java

    public int removeElement(int[] nums, int val) {

        if (nums==null || nums.length == 0)
            return 0;

        int i = -1;

        for (int j=0; j<nums.length; j++) {
            if (nums[j] != val) {
                nums[i+1] = nums[j];
                i++;
            }
        }

        return i+1;
    }