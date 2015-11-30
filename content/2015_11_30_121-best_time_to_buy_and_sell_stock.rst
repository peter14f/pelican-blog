121-best_time_to_buy_and_sell_stock
###################################

:date: 2015-11-30 22:11
:tags:
:category: LeetCode
:slug: 121-best_time_to_buy_and_sell_stock

`LeetCode Problem Link <https://leetcode.com/problems/best-time-to-buy-and-sell-stock/>`_

In this problem, we're only allowed to make one trade. That means we can only buy once at time ``i`` and then
sell once at time ``j`` where ``j>i``.
Keep track of the ``maxProfit`` and ``buyIndex``. Update ``buyIndex`` if current price is lower than price at
``buyIndex``. This take O(n) time.

.. code-block:: java

    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int buyIndex = 0;

        for (int i=1; i<prices.length; i++) {

            if (prices[i] < prices[buyIndex]) {
                buyIndex = i;
            }

            if (prices[i] - prices[buyIndex] > maxProfit) {
                maxProfit = prices[i] - prices[buyIndex];
            }
        }

        return maxProfit;
    }
