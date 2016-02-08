225-implement_stack_using_queues
################################

:date: 2016-2-8 15:54
:tags: Stacks, Queues
:category: LeetCode
:slug: 225-implement_stack_using_queues

`LeetCode Problem Link <https://leetcode.com/problems/implement-stack-using-queues/>`_

Use two queues. Here after each operation, I always put elements back into  ``q1``.

.. code-block:: java

    class MyStack {
        Queue<Integer> q1;
        Queue<Integer> q2;

        public MyStack() {
            q1 = new LinkedList<Integer>();
            q2 = new LinkedList<Integer>();
        }

        // Push element x onto stack.
        public void push(int x) {
            q1.offer(x);
        }

        // Removes the element on top of the stack.
        public void pop() {
            if (q1.isEmpty())
                return;

            while (q1.size() > 1)
                q2.offer(q1.poll());

            q1.poll();

            while (!q2.isEmpty())
                q1.offer(q2.poll());
        }

        // Get the top element.
        public int top() {
            while (q1.size() > 1)
                q2.offer(q1.poll());

            int ret = q1.poll();
            q2.offer(ret);

            while (!q2.isEmpty())
                q1.offer(q2.poll());

            return ret;
        }

        // Return whether the stack is empty.
        public boolean empty() {
            return q1.isEmpty();
        }
    }
