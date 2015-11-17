093-restore_ip_addresses
########################

:date: 2015-11-17 22:11
:tags: Recursion
:category: LeetCode
:slug: 093-restore_ip_addresses

`LeetCode Problem Link <https://leetcode.com/problems/restore-ip-addresses/>`_

The approach is very similar to the NP problems (051-n_queens, 037-sudoku_solver). We have a current list where we store the current ip address that
has been built. At each new index, we could have three different code paths:

    1. put a '.' right after the current index (forms a one-digit number)
    2. put a '.' right after the next index (forms a two-digit number)
    3. put a '.' right after the next next index (forms a three-digit number)

However, we also need to check how many characters are left after the dot. The number of characters cannot be more than
``3*(4 - group)`` and cannot be fewer than ``(4-group)``.
The reason is simple, each group can have at most 3 digits and must
have at least 1 digit. ``(4-group)`` tells up how many more groups need to be constructed.

.. code-block:: java

    public List<String> restoreIpAddresses(String s) {
        char[] sArr = s.toCharArray();
        List<String> ans = new ArrayList<String>();

        if (sArr.length > 12)
            return ans;

        ArrayList<Integer> curList = new ArrayList<Integer>();
        getAllAddresses(sArr, 0, curList, ans);

        return ans;
    }

    private void getAllAddresses(
            char[] sArr,
            int index,
            List<Integer> curList,
            List<String> ans) {

        int num = 0;
        int group = curList.size() + 1;

        /* remaining characters left should be shorter
         * than 3 times the number of groups left and should be longer
         * then 1 times the number of groups left
         */
        if (sArr.length - (index+1) <= 3 * (4-group) &&
                sArr.length - (index+1) >= (4-group)) {
            num = sArr[index] - '0';

            if (num >= 0 && num <= 9) {
                curList.add(num);

                if (index==sArr.length - 1) {
                    ans.add(curList.get(0) + "." +
                            curList.get(1) + "." +
                            curList.get(2) + "." +
                            curList.get(3));
                }

                if (group < 4)
                    getAllAddresses(sArr, index+1, curList, ans);

                curList.remove(curList.size() -  1);
            }
        }

        if (index + 1 < sArr.length &&
                sArr.length - (index+2) <= 3 * (4-group) &&
                sArr.length - (index+2) >= (4-group)) {
            num  = sArr[index] - '0';
            if (num > 0 && num <= 9) {
                num = 10*num + (sArr[index+1] - '0');
                curList.add(num);

                if (index+1==sArr.length - 1) {
                    ans.add(curList.get(0) + "." +
                            curList.get(1) + "." +
                            curList.get(2) + "." +
                            curList.get(3));
                }

                if (group < 4)
                    getAllAddresses(sArr, index+2, curList, ans);

                curList.remove(curList.size() - 1);
            }
        }

        if (index + 2 < sArr.length &&
                sArr.length - (index+3) <= 3 * (4-group) &&
                sArr.length - (index+3) >= (4-group)) {
            num  = sArr[index] - '0';
            if (num > 0 && num <= 9) {

                num = 100*num + 10*(sArr[index+1] - '0') + (sArr[index+2] - '0');

                if (num <= 255) {
                    curList.add(num);

                    if (index+2==sArr.length - 1) {
                        ans.add(curList.get(0) + "." +
                                curList.get(1) + "." +
                                curList.get(2) + "." +
                                curList.get(3));
                    }

                    if (group < 4)
                        getAllAddresses(sArr, index+3, curList, ans);

                    curList.remove(curList.size() - 1);
                }
            }
        }
    }