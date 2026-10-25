# Algorithm Analysis Midterm Project: Sorting Algorithms Analysis

**Course:** Algorithm Analysis  
**Lecturer:** Dr. Coşkun Şahin[cite: 1]  
**Student Name:** Muhammet Kansız  
**Student ID:** 2322190005  
**Department:** Software Engineering[cite: 1]  

---

## 1. Overview and Mechanics of Selected Algorithms[cite: 1]

### 1.1 Bubble Sort
Bubble Sort is a straightforward comparison-based sorting algorithm[cite: 2]. It continuously iterates through the list, compares adjacent elements, and swaps them if they are in descending order.
* **Mechanism & Tracing:** An unsorted array (e.g., `[64, 34, 25, 12, 22, 11, 90]`) is sorted by bubbling the largest unsorted element to the end of the array in each outer pass.
* **Early Termination:** By tracking swaps with a boolean flag (`swapped`), if a complete pass occurs with zero swaps, the algorithm terminates immediately in linear time $O(n)$.

### 1.2 TimSort
TimSort is a high-performance, adaptive, stable hybrid sorting algorithm derived from Merge Sort and Insertion Sort, designed by Tim Peters in 2002[cite: 2].
* **Mechanism & Tracing:** TimSort divides the input list into small ordered segments called **runs**.
* **Insertion Sort Phase:** Sub-arrays of size `min_run` are sorted using Insertion Sort, taking advantage of low constant factor overhead and CPU cache locality on small contiguous memory blocks.
* **Merge Phase:** Once runs are sorted, they are merged in pairs using a bottom-up Merge Sort routine until the entire collection is sorted.

---

## 2. Complexity Analysis: CPU and Memory Workloads[cite: 1]

### 2.1 Theoretical Complexity Matrix

| Algorithm | Best Case (Time)[cite: 1] | Average Case (Time)[cite: 1] | Worst Case (Time)[cite: 1] | Auxiliary Space Complexity[cite: 1] | Stability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$[cite: 1] | $O(n^2)$[cite: 1] | $O(n^2)$[cite: 1] | $O(1)$[cite: 1] | Yes |
| **TimSort** | $O(n)$[cite: 1] | $O(n \log n)$[cite: 1] | $O(n \log n)$[cite: 1] | $O(n)$[cite: 1] | Yes |

---

### 2.2 Workload Breakdown on CPU and Memory[cite: 1]

#### Bubble Sort Workload:
* **Best Case CPU Workload ($O(n)$):** Occurs when the input is already fully sorted[cite: 1]. Only $n - 1$ comparisons and 0 swaps take place.
* **Worst Case CPU Workload ($O(n^2)$):** Occurs when the input is reverse-sorted[cite: 1]. Requires $\frac{n(n-1)}{2}$ comparisons and $\frac{n(n-1)}{2}$ swap operations, placing heavy demands on CPU cycles.
* **Average Case CPU Workload ($O(n^2)$):** In arbitrary permutations, the nested loop executes quadratic operations[cite: 1].
* **Memory Workload ($O(1)$):** Operates strictly in-place; pointer-swapping occurs without allocating additional heap buffers[cite: 1].

#### TimSort Workload:
* **Best Case CPU Workload ($O(n)$):** When elements are already ordered, TimSort detects a single continuous run and skips unnecessary merge steps[cite: 1].
* **Worst Case CPU Workload ($O(n \log n)$):** In highly disordered arrays, small runs are sorted via Insertion Sort and merged logarithmically ($O(n \log n)$ overall)[cite: 1].
* **Average Case CPU Workload ($O(n \log n)$):** Outperforms standard algorithms on real-world data due to its exploitation of pre-existing ascending/descending runs[cite: 1].
* **Memory Workload ($O(n)$):** During the merge routine, auxiliary sub-arrays (`left_part` and `right_part`) are allocated in memory, which is demonstrated via Python's `tracemalloc` output[cite: 1].

---

## 3. Comparison and Evaluation of Best Use Cases[cite: 1]

### Comparison:
* **Instruction Count & Scaling:** For $N=2000$, Bubble Sort triggers over 1.9 million comparisons in worst/average cases, whereas TimSort completes the task with a fraction of operations.
* **Memory Trade-off:** Bubble Sort provides optimal $O(1)$ space efficiency but scales poorly, whereas TimSort trades temporary memory ($O(n)$ overhead) for drastically superior execution speeds[cite: 1].

### Best Use Cases[cite: 1]:
* **Bubble Sort:**
  * Educational demonstrations of basic sorting mechanics and algorithm invariants.
  * Verifying whether an array is already sorted in $O(n)$ with minimal code complexity[cite: 1].
  * Strictly constrained embedded environments with ultra-limited memory where $n < 20$.
* **TimSort:**
  * Standard library default sorting algorithm (used in Python's `sort()`, Java 7+, and Android).
  * Real-world datasets with pre-existing ordered segments or repetitive sequences.
  * Scenarios where stability is strictly required alongside optimal $O(n \log n)$ performance.

---

## 4. AI Utilization Rules and Ethic Codes[cite: 1]

Gemini was used in the Code Implementation, Metric Profiling, and Documentation sections of this product[cite: 1]. The tool was utilized via the prompt/input "Generate Python code and Markdown comparison report for Bubble Sort and TimSort based on the midterm assignment requirements" for the purpose of Code generation, Algorithm editing, and Documentation[cite: 1]. The output generated has been reviewed and verified by me for technical accuracy, safety, and originality[cite: 1]. I bear full responsibility for the work[cite: 1].
