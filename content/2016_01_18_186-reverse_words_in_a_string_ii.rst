186-reverse_words_in_a_string_ii
################################

:date: 2016-1-18 23:35
:tags: C, in-place string manipulation
:category: LeetCode
:slug: 186-reverse_words_in_a_string_ii

`LeetCode Problem Link <https://leetcode.com/problems/reverse-words-in-a-string-ii/>`_

Easier problem than 151-reverse_words_in_a_string since we don't have to deal with the leading and
trailing spaces. Also, the number of spaces between words is always 1. Way way way easier. Reverse
the whole string first and then reverse each word.

.. code-block:: java

    void reverseWords(char *s) {
      int len = 0;
      char *r;
      char *l;
      int spaceCnt = 0;
      int i, j;

      if (s==NULL)
        return;

      len = strlen(s);

      if (len==0)
        return;

      for (i=0; i<len; i++) {
        if (s[i] == ' ')
          spaceCnt++;
      }

      /* contains only one word? */
      if (spaceCnt==0)
        return;

      /* reverse the whole string first */
      l = s;
      r = s+len-1;

      while (r > l) {
        char tmp = *r;
        *r = *l;
        *l = tmp;
        r--;
        l++;
      }

      i = 0;
      j = i+1;

      /* reverse each word */
      while (i < len) {
        if (s[j] == ' ' || s[j] == '\0') {
          l = s+i;
          r = s+j-1;

          while (r > l) {
            char tmp = *r;
            *r = *l;
            *l = tmp;
            r--;
            l++;
          }

          i = j + 1;
          j = i + 1;
        }
        else {
          j++;
        }
      }
    }
