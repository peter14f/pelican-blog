318-maximum_product_of_word_lengths
###################################

:date: 2016-2-26 22:01
:tags: Bookkeeping
:category: LeetCode
:slug: 318-maximum_product_of_word_lengths

`LeetCode Problem Link <https://leetcode.com/problems/maximum-product-of-word-lengths/>`_

Well, if we can lookup whether two strings have any character in common in O(1) time, we could
solve this problem in O(n \ :superscript:`2`) time where ``n`` is the input array size.

What about a bitmap? An integer has 32 bits and each string contains only 'a' to 'z' so that's enough.

So we need to allocate an int array of size ``n`` called ``bitMaps``.

To find out if ``words[i]`` and ``words[j]`` have any characters in common, we simply check if
(bitMaps[i] & bitMaps[j]) > 0.

Building the ``bitMaps`` will take O(nk) time though where we assume ``k`` is the average length of the ``n`` words.

.. code-block:: java

    public int maxProduct(String[] words) {
        int n = words.length;
        int[] bitMaps = new int[n];

        for (int i=0; i<words.length; i++) {
            for (int j=0; j<words[i].length(); j++) {
                char c = words[i].charAt(j);

                bitMaps[i] |= (1<<(c-'a'));
            }
        }

        int max = 0;

        for (int i=0; i<words.length; i++) {
            for (int j=i+1; j<words.length; j++) {
                if ((bitMaps[i] & bitMaps[j]) == 0) {
                    int product = words[i].length() * words[j].length();

                    if (product > max) {
                        max = product;
                    }

                }
            }
        }

        return max;
    }

