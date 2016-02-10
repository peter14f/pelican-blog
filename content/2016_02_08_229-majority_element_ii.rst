229-majority_element_ii
#######################

:date: 2016-2-8 23:48
:tags: Majority Vote Algorithm
:category: LeetCode
:slug: 229-majority_element_ii

`LeetCode Problem Link <https://leetcode.com/problems/majority-element-ii/>`_

In this problem, the majority is defined as appearing more than floor(n/3) times. So we can have 0, 1, or 2 majority
elements in any given input array.

Therefore, we can extend our solution to 169-majority_element to keep track of two numbers. Just remember than when
the current number does not match with both numbers, we need to decrement both counts.

.. code-block:: java

    public List<Integer> majorityElement(int[] nums) {
        List<Integer> ans = new ArrayList<Integer>();

        Integer n1 = null;
        Integer n2 = null;

        int count1 = 0;
        int count2 = 0;

        for (int i=0; i<nums.length; i++) {
            if (n1==null) {
                n1 = nums[i];
                count1 = 1;
            }
            else if (nums[i] == n1) {
                count1++;
            }
            else if (n2 == null) {
                n2 = nums[i];
                count2 = 1;
            }
            else if (nums[i] == n2) {
                count2++;
            }
            else if (count1 == 0){
                n1 = nums[i];
                count1 = 1;
            }
            else if (count2 == 0) {
                n2 = nums[i];
                count2 = 1;
            }
            else {
                count1--;
                count2--;
            }
        }

        int n = nums.length;
        int cnt1 = 0;
        int cnt2 = 0;

        for (int i=0; i<nums.length; i++) {
            if (nums[i] == n1)
                cnt1++;
            else if (nums[i] == n2)
                cnt2++;
        }

        if (cnt1 > n/3)
            ans.add(n1);
        if (cnt2 > n/3)
            ans.add(n2);

        return ans;
    }
