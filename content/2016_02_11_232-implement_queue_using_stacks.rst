232-implement_queue_using_stacks
################################

:date: 2016-2-11 11:22
:tags: Stacks, Queues
:category: LeetCode
:slug: 232-implement_queue_using_stacks

`LeetCode Problem Link <https://leetcode.com/problems/implement-queue-using-stacks/>`_

Use two stacks. After each queue operation, I make sure that elements end up in ``stk1``.

.. code-block:: java

    public class MyQueue {
        Stack<Integer> stk1;
        Stack<Integer> stk2;

        public MyQueue() {
            stk1 = new Stack<Integer>();
            stk2 = new Stack<Integer>();
        }

        // Push element x to the back of queue.
        public void push(int x) {
            stk1.push(x);
        }

        // Removes the element from in front of queue.
        public void pop() {
            while (stk1.size() > 1) {
                stk2.push(stk1.pop());
            }
            stk1.pop();
            while (!stk2.isEmpty()) {
                stk1.push(stk2.pop());
            }
        }

        // Get the front element.
        public int peek() {
            int ret;

            while (stk1.size() > 1) {
                stk2.push(stk1.pop());
            }

            ret = stk1.peek();

            while (!stk2.isEmpty()) {
                stk1.push(stk2.pop());
            }

            return ret;
        }

        // Return whether the queue is empty.
        public boolean empty() {
            return (stk1.isEmpty());
        }
    }
