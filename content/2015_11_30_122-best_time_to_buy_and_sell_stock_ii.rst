122-best_time_to_buy_and_sell_stock_ii
######################################

:date: 2015-11-30 22:43
:tags: Greedy Algorithm, Best Time To Buy/Sell
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

The previous approach turns out to be too much. We can use greedy algorithm even though we cannot
make more than one transaction on one day. In the case of ``[1, 2, 3, 4]``, even though we are
adding to profit three times, conseucutive addition will be counted as  one transaction. We are
still buying at day ``0`` and selling at day ``3``. So we should sell at day ``i`` as long as the
price at day ``i`` is higher than the price at day ``i-1``.

.. code-block:: java

    public int maxProfit(int[] prices) {
        int profit = 0;

        for (int i=1; i<prices.length; i++) {
            if (prices[i] - prices[i-1] > 0) {
                profit += prices[i] - prices[i-1];
            }
        }

        return profit;
    }

This also takes O(n) time only.


