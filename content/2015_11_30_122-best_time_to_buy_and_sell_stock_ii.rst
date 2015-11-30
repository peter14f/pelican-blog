122-best_time_to_buy_and_sell_stock_ii
######################################

:date: 2015-11-30 22:43
:tags:
:category: LeetCode
:slug: 122-best_time_to_buy_and_sell_stock_ii

`LeetCode Problem Link <https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/>`_

The problem is different from the previous problem 121-best_time_to_buy_and_sell_stock in that
we are now allowed to make multiple trades. The idea is pretty much the same.

.. code-block:: java

    // multiple transactions allowed
    public int maxProfit(int[] prices) {

        int buyIndex = 0;
        int sellIndex = 0;
        int profit = 0;

        for (int i=1; i<prices.length; i++) {
            if (prices[i] < prices[buyIndex]) {
                if (sellIndex > buyIndex)
                    profit += prices[sellIndex] - prices[buyIndex];

                buyIndex = i;
                sellIndex = i;
            }
            else if (prices[i] < prices[sellIndex]) {
                if (sellIndex > buyIndex)
                    profit += prices[sellIndex] - prices[buyIndex];

                buyIndex = i;
                sellIndex = i;
            }
            else if (prices[i] > prices[buyIndex]) {
                sellIndex = i;
            }
        }

        if (sellIndex > buyIndex)
            profit += prices[sellIndex] - prices[buyIndex];

        return profit;
    }
