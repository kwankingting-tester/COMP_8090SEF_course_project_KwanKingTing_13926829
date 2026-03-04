Task 2: Self-Study – Binary Heap + Heap Sort

Integration Plan with Task 1
In the final GUI version, Task 2 will be integrated into Task 1 to provide real-time "Top 5 Highest Spending Alerts" and sorted expense reports using the Heap.

Data Structure – Binary Heap
- ADT: `insert()`, `extract_max()`, `peek()`, `get_top_k()`, `build_heap()`
- Implementation: Array-based complete binary tree
- Application in this project: Maintains priority of highest expenses in real-time

Algorithm – Heap Sort
- Time Complexity**: O(n log n) in all cases (best / worst / average)
- Steps: Build max-heap → repeatedly extract max
- Advantage: More efficient than Bubble Sort or Selection Sort for large transaction lists

