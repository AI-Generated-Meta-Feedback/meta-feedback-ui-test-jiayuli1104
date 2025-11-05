1. Algorithm Choice

Chosen Algorithm: Insertion Sort

Why?

Insertion Sort is stable, meaning if two items have the same key, their original relative order is preserved.

Given only 25 books, insertion sort performs efficiently because it handles mostly-sorted input very well.

Is it stable? Why does stability matter here?

Yes, Insertion Sort is stable.

Stability matters because books on the same shelf must keep the original return order (FIFO order when returned to the shelf).
Example: return order 1 comes before return order 2.

2. Sorting Strategy

Primary sorting criterion: shelfNumber (ascending)

Secondary criterion (same shelf): returnOrder (ascending, because earlier returned books go back first)

Comparison rule (when comparing book A and book B):

If A.shelfNumber < B.shelfNumber → A comes first
If A.shelfNumber > B.shelfNumber → B comes first
If A.shelfNumber == B.shelfNumber:
        compare returnOrder
        If A.returnOrder < B.returnOrder → A comes first

3. Complexity
Case	Time Complexity	Explanation
Worst / Random order	O(n²)	Insertion Sort compares and shifts elements
Best case (books already mostly sorted)	O(n)	Only one comparison per book

Since n = 25, performance is acceptable.
