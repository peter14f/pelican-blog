006-zigzag_conversion
#####################

:date: 2015-9-7 16:49
:tags: String
:category: LeetCode
:slug: 006-zigzag_conversion

`LeetCode Problem Link <https://leetcode.com/problems/two-sum/>`_

On the first try, I created a 2D character array and then tried to fill in the characters.
But this requires that you figure out the number of columns needed beforehand.

Here is how I approached the problem without using extra space:

Depending on which row you are at,
here is the directions to follow the zigzag in order to reach the next character
in the same row.

* First row: down, up (right)
* Last row: up (right), down
* All other rows: down, up (right) to get the next character in the same row, and then up (right), down to get the following character

Once you figure out this pattern, the implementation just requires that you figure out how
much to add to the current index to reach the next character in the string you want.

As shown in the code below, the number to add to the current index is the same for the case of the first row
and the last row.

.. code-block:: java

    public String convert2(String s, int numRows) {
        if (numRows==1)
            return s;

        StringBuffer sb = new StringBuffer();

        int n = s.length();

        for (int row=0; row < numRows; row++) {

            if (row >= n)
                break;

            // self
            sb.append(s.charAt(row));

            if (row==0 || row==numRows-1) {
                int downSteps = numRows - 1;
                int upSteps = numRows - 1;
                int index = row;
                index += downSteps + upSteps;
                while (index < n) {
                    sb.append(s.charAt(index));
                    index += downSteps + upSteps;
                }
            }
            else {
                // down -> up, up -> down
                int part1Steps = 2*(numRows - 1 - row);
                int part2Steps = 2*row;

                int index = row;


                index += part1Steps;
                boolean one = false;

                while (index < n) {
                    sb.append(s.charAt(index));

                    if (one) {
                        index += part1Steps;
                        one = false;
                    }
                    else {
                        index += part2Steps;
                        one = true;
                    }
                }
            }
        }

        return sb.toString();
    }

