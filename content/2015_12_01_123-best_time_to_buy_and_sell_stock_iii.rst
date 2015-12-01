123-best_time_to_buy_and_sell_stock_iii
#######################################

:date: 2015-12-1 17:56
:tags: Dynamic Programming
:category: LeetCode
:slug: 123-best_time_to_buy_and_sell_stock_iii

`LeetCode Problem Link <https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/>`_

We can make at most two transactions. That means if i goes from ``1`` to ``n-2``, we would go
through all the possible ways to partition the prices into two groups. The first group is prices[0..i]
and second group is prices[i+1, n-1].

So here is one way we could solve the problem. We see if making one transaction yields more profit or
any of the ways making two transactions yields more profit.

.. code-block:: java

    public int maxProfit(int[] prices) {

        int maxProfit = maxProfitOne(prices, 0, prices.length-1);

        for (int i=1; i<prices.length-2; i++) {
            int profit = maxProfitOne(prices, 0, i) + maxProfitOne(prices, i+1, prices.length-1);
            if (profit > maxProfit)
                maxProfit = profit;
        }

        return maxProfit;
    }

    private int maxProfitOne(int[] prices, int low, int high) {
        int buyIndex = low;
        int maxProfit = 0;

        for (int i=low+1; i<=high; i++) {

            if (prices[i] < prices[buyIndex]) {
                buyIndex = i;
            }
            else {
                int profit = prices[i] - prices[buyIndex];
                if (profit > maxProfit)
                    maxProfit = profit;
            }
        }

        return maxProfit;
    }

What's the time complexity for this approach? Outer loop iterates ``n`` times and the inner loop iterates ``n``
Unfortunately this won't pass the gigantic test case on OJ. So let's now look at the dynamic programming approach.

For the DP approach, we will maintain two int array ``profit1`` and ``profit2``, each of size ``n``. ``profit1[i]`` is
the maximum profit made with one transaction only and considering the prices from index 0 to index i .

``profit2[i]`` is the maximum profit made with one transaction only considering the
prices from index i to index n-1. We will fill out ``profit1`` from index ``0`` all the way up to index ``n-1``.
We know what to do when we see a new price just like in 121-best_time_to_buy_and_sell_stock. We will fill out
``profit2`` from index ``n-1`` all the down to index ``0``. Now instead of seeing a newer price, we are seeing an
older price.

One both array have been filled out, we can add the number at the corresponding index and see which sum is the
greatest profit. Note that profit1[0] + profit2[0] should be the same as profit1[n-1] + profit2[n-1]. This represent
making one transaction in total where the other sums represent making two transactions.

.. code-block:: java

    public int maxProfit(int[] prices) {

        int maxProfit = maxProfitOne(prices, 0, prices.length-1);

        for (int i=1; i<prices.length-2; i++) {
            int profit = maxProfitOne(prices, 0, i) + maxProfitOne(prices, i+1, prices.length-1);
            if (profit > maxProfit)
                maxProfit = profit;
        }

        return maxProfit;
    }

    private int maxProfitOne(int[] prices, int low, int high) {
        int buyIndex = low;
        int maxProfit = 0;

        for (int i=low+1; i<=high; i++) {

            if (prices[i] < prices[buyIndex]) {
                buyIndex = i;
            }
            else {
                int profit = prices[i] - prices[buyIndex];
                if (profit > maxProfit)
                    maxProfit = profit;
            }
        }

        return maxProfit;
    }
