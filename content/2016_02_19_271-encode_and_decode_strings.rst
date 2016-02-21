271-encode_and_decode_strings
#############################

:date: 2016-2-19 23:43
:tags:
:category: LeetCode
:slug: 271-encode_and_decode_strings

`LeetCode Problem Link <https://leetcode.com/problems/encode-and-decode-strings/>`_

Here is my format

::

    3:a,b,c,xxxxxxxxxxxxxxxx

``3`` is the number of strings in the list, this case, 3
**:** marks the end of ``n``
``a`` is the length of string 1, ``,`` marks the end of ``a``
``b`` is the length of string 2, ``,`` marks the end of ``b``
``c`` is the length of string 3, ``,`` marks the end of ``c``

After the last ``,`` the real data begins. Since the receiver has the length of each string, he knows
how many characters to read for each string.

.. code-block:: java

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuffer sb = new StringBuffer();

        int n = strs.size();

        if (n == 0) {
            sb.append("0:");
            return sb.toString();
        }

        sb.append(n + ":");

        for (int i=0; i<strs.size(); i++) {
            sb.append(strs.get(i).length());
            sb.append(",");
        }

        for (String s: strs) {
            sb.append(s);
        }

        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        int i=0;
        while (s.charAt(i) != ':') {
            i++;
        }

        int n = Integer.parseInt(s.substring(0, i));

        List<String> strs = new ArrayList<String>();

        if (n==0)
            return strs;

        List<Integer> lengths = new ArrayList<Integer>();
        i++;
        int j = i+1;

        for (int z=0; z<n; z++) {
            while (s.charAt(j) != ',') {
                j++;
            }

            int l = Integer.parseInt(s.substring(i, j));
            lengths.add(l);
            j++;
            i = j;
        }

        for (int l : lengths) {
            StringBuffer sb = new StringBuffer();
            for (int z=0; z<l; z++) {
                sb.append(s.charAt(i));
                i++;
            }
            strs.add(sb.toString());
        }

        return strs;
    }

