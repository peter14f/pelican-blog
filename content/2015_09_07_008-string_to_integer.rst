008-string_to_integer
#####################

:date: 2015-9-7 17:22
:tags: C String Functions
:category: LeetCode
:slug: 008-string_to_integer

`LeetCode Problem Link <https://leetcode.com/problems/string-to-integer-atoi/>`_

I decided to do this problem in C since **atoi()** is a C function.

| We store the result in ``ans``
| First we need to eat up blank spaces.
| As we find the first non-blank character, we need to start checking for the sign.
| The sign is either '+' or '-', as we find the first non-sign character, we stop
| looking for the sign and expects numbers only...
| For each digit we see, we first shift ``ans`` to the right by 1 digit (by multiplying 10)
| and then add that digit to ``ans``
| If a non-number is found, the current ``ans`` will be returned.
| If overflow occurs and ``ans`` is positive, return ``0x7FFFFFFF``.
| If overflow occurs and ``ans`` is negative, return ``0x80000000``.



.. code-block:: c

    #include <stdlib.h>
    #include <stdio.h>
    #include <string.h>

    #define boolean unsigned char
    #define TRUE 1
    #define FALSE 0

    int myAtoi(char *str) {
      int ans = 0;
      boolean check_blank = TRUE;
      boolean check_sign = TRUE;
      boolean negative = FALSE;
      boolean overflow = FALSE;

      int i = 0;

      while (*str != '\0') {
        if (check_blank) {
          if (!is_blank_char(*str)) {
            check_blank = FALSE;
            continue;
          }
        }
        else if (check_sign) {
          if (*str == '+') {
            check_sign = FALSE;
            str++;
            i++;
          }
          else if (*str == '-') {
            negative = TRUE;
            check_sign = FALSE;
            str++;
            i++;
          }
          else {
            check_sign = FALSE;
          }
          continue;
        }
        else {
          char num = is_number(*str);

          printf("  num %d\n", num);

          if (num == -1) {
            break;
          }
          else {
            int new_ans_multiply = ans * 10;
            if (new_ans_multiply / 10 != ans) {
              overflow = TRUE;
            }
            int new_ans_sum = new_ans_multiply + num;
            if (new_ans_sum < new_ans_multiply) {
              overflow = TRUE;
            }
            ans = new_ans_sum;
          }
        }
        str++;
        i++;
      }

      if (negative) {
        ans = -ans;
        if (overflow) {
          ans = 0x80000000;
        }
      }
      else {
        if (overflow) {
          ans = 0x7FFFFFFF;
        }
      }

      return ans;
    }

    boolean is_blank_char(char c) {
      switch (c) {
        case 9:  /* TAB */
        case 10: /* LF */
        case 11: /* VT */
        case 12: /* FF */
        case 13: /* CR */
        case 32: /* Space */
          return TRUE;

        default:
          return FALSE;
      }
    }

    char is_number(char c) {
      switch (c) {
        case '0':
          return 0;
        case '1':
          return 1;
        case '2':
          return 2;
        case '3':
          return 3;
        case '4':
          return 4;
        case '5':
          return 5;
        case '6':
          return 6;
        case '7':
          return 7;
        case '8':
          return 8;
        case '9':
          return 9;
        default:
          return -1;
      }
    }