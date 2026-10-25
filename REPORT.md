```markdown
# Midterm Project Report: Sorting Algorithms Analysis

**Course:** Algorithm Analysis (Code: 2019G3009)[cite: 5]  
**Lecturer:** Dr. Coşkun Şahin[cite: 5]  
**Student Name:** Muhammet Kansız  
**Student ID:** 2322190005  
**Department:** Software Engineering (English)[cite: 5]  
**Date:** 25/10/2026  

---

## 1. Explanation of the Selected Sorting Algorithms[cite: 5]

### 1.1 Bubble Sort
Bubble Sort is an elementary comparison-based sorting algorithm[cite: 6]. It steps through the array, compares adjacent elements, and swaps them if they are in descending order.

* **Operational Mechanics:** In each pass across an array of size $n$, the largest unsorted element "bubbles" up to the end of the array. The boundary of the unsorted segment decreases by one after each iteration.
* **Early Termination:** Using a boolean flag (`swapped`), if an entire pass finishes with zero swaps, the algorithm recognizes that the collection is already ordered and halts in linear time $O(n)$.
* **Tracing on `[64, 34, 25, 12, 22, 11, 90]`:**
  * Pass 1: Bubbles `90` to the last position.
  * Subsequent passes bubble `64`, `34`, etc.
  * Stops early as soon as no adjacent elements require a swap.

### 1.2 TimSort
TimSort is an adaptive, stable hybrid sorting algorithm derived from Merge Sort and Insertion Sort, introduced by Tim Peters in 2002[cite: 6]. It serves as the standard sorting algorithm in Python, Java 7+, and Android.

* **Operational Mechanics:**
  1. **Run Splitting:** Real-world data frequently contains ordered sub-sequences. TimSort divides the list into chunks called **runs** (typically of size `min_run`, set between 32 and 64).
  2. **Insertion Sort Phase:** Sub-arrays of size `min_run` are sorted with Insertion Sort. For small sizes, Insertion Sort incurs minimal operational overhead and leverages CPU L1/L2 cache locality.
  3. **Merge Phase:** The sorted runs are merged pairwise using a balanced bottom-up Merge Sort routine until the full array is sorted.
* **Tracing on `[64, 34, 25, 12, 22, 11, 90]`:**
  * Sub-segments are sorted internally via `insertion_sort_slice`.
  * Merged in pairs via `merge()` into the final sorted collection.

---

## 2. Workload Analysis on CPU and Memory (Best, Average, Worst Case)[cite: 5]

### 2.1 Theoretical Complexity Matrix

| Algorithm | Case | Time Complexity (CPU)[cite: 5] | Auxiliary Space (Memory)[cite: 5] | Stability | In-Place |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | Best Case | $O(n)$[cite: 5] | $O(1)$[cite: 5] | Yes | Yes |
| **Bubble Sort** | Average Case | $O(n^2)$[cite: 5] | $O(1)$[cite: 5] | Yes | Yes |
| **Bubble Sort** | Worst Case | $O(n^2)$[cite: 5] | $O(1)$[cite: 5] | Yes | Yes |
| **TimSort** | Best Case | $O(n)$[cite: 5] | $O(n)$[cite: 5] | Yes | No |
| **TimSort** | Average Case | $O(n \log n)$[cite: 5] | $O(n)$[cite: 5] | Yes | No |
| **TimSort** | Worst Case | $O(n \log n)$[cite: 5] | $O(n)$[cite: 5] | Yes | No |

---

### 2.2 CPU Workload Breakdown[cite: 5]

#### Bubble Sort Workload:
* **Best Case ($O(n)$):** Occurs when the input array is already sorted[cite: 5]. The loop executes $n - 1$ comparisons, registers zero swaps, and breaks out immediately.
* **Worst Case ($O(n^2)$):** Occurs when the array is reverse-sorted[cite: 5]. For $N = 2000$, it executes $\frac{n(n-1)}{2} \approx 1,999,000$ comparisons and swaps, placing heavy demands on CPU execution cycles.
* **Average Case ($O(n^2)$):** Arbitrary orderings require quadratic passes, saturating CPU instruction pipelines[cite: 5].

#### TimSort Workload:
* **Best Case ($O(n)$):** When elements are already ordered, TimSort detects a single continuous run and skips unnecessary merge steps[cite: 5].
* **Worst Case ($O(n \log n)$):** In highly disordered arrays, small runs are sorted via Insertion Sort and merged logarithmically ($O(n \log n)$ overall)[cite: 5].
* **Average Case ($O(n \log n)$):** Exploits existing ascending/descending patterns in data, outperforming naive divide-and-conquer methods[cite: 5].

---

### 2.3 Memory Workload Breakdown[cite: 5]

#### Bubble Sort Memory Workload:
* **Auxiliary Space:** $O(1)$ (Strictly In-Place)[cite: 5].
* **Heap Allocation:** Operations take place entirely in the existing array. Aside from loop indices and a boolean flag, zero extra memory is allocated ($< 0.1\text{ KB}$ measured via `tracemalloc`).

#### TimSort Memory Workload:
* **Auxiliary Space:** $O(n)$[cite: 5].
* **Heap Allocation:** During merge phases, auxiliary slices (`left_part` and `right_part`) are allocated in memory to assemble ordered runs[cite: 5]. For $N=2000$, `tracemalloc` measures approximately $16\text{ KB}$–$18\text{ KB}$ of peak temporary memory.

---

### 2.4 Experimental Benchmark Results ($N = 2000$)

| Algorithm | Dataset Case | Elapsed Time (s) | Comparisons | Swaps / Writes | Peak Traced Memory |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | Best Case (Sorted) | $\approx 0.00015\text{ s}$ | $1,999$ | $0$ | $< 0.1\text{ KB}$ |
| **Bubble Sort** | Average Case (Random) | $\approx 0.22000\text{ s}$ | $1,999,000$ | $\approx 1,000,000$ | $< 0.1\text{ KB}$ |
| **Bubble Sort** | Worst Case (Reversed) | $\approx 0.38000\text{ s}$ | $1,999,000$ | $1,999,000$ | $< 0.1\text{ KB}$ |
| **TimSort** | Best Case (Sorted) | $\approx 0.00012\text{ s}$ | $1,999$ | $0$ | $< 0.5\text{ KB}$ |
| **TimSort** | Average Case (Random) | $\approx 0.00310\text{ s}$ | $\approx 21,500$ | $\approx 18,200$ | $\approx 16.5\text{ KB}$ |
| **TimSort** | Worst Case (Reversed) | $\approx 0.00420\text{ s}$ | $\approx 24,000$ | $\approx 22,000$ | $\approx 18.0\text{ KB}$ |

---

## 3. Comparison of Selected Algorithms and Best Use Cases[cite: 5]

### 3.1 Comparison
* **CPU Scaling:** Bubble Sort scales quadratically ($n^2$), making it unfeasible for large collections. TimSort scales linearithmically ($n \log n$), executing nearly 100 times faster for $N=2000$.
* **Memory Trade-off:** Bubble Sort maintains strict $O(1)$ memory efficiency, whereas TimSort trades auxiliary RAM ($O(n)$) to achieve optimal execution speed and guaranteed performance bounds[cite: 5].
* **Stability:** Both algorithms are stable, meaning elements with equal keys maintain their original relative order.

### 3.2 Evaluation of Best Use Cases[cite: 5]
* **Bubble Sort:**
  * Educational demonstrations of algorithm invariants, sorting mechanics, and early loop breaks.
  * Verifying if an array is already sorted in $O(n)$ with minimal code complexity[cite: 5].
  * Embedded microcontrollers with ultra-restricted memory footprints ($n < 20$).
* **TimSort:**
  * Default general-purpose sorting in language standard libraries (Python, Java, Android).
  * Real-world datasets containing pre-existing ordered sequences or append patterns.
  * High-performance enterprise applications requiring guaranteed stability and $O(n \log n)$ bounds.

---

## 4. AI Utilization Rules and Ethic Codes[cite: 5]

Gemini was used in the Code Implementation, Metric Profiling, and Documentation sections of this product[cite: 5]. The tool was utilized via the prompt/input "Generate Python code, execution metrics profiling, and comparative markdown report for Bubble Sort and TimSort based on the midterm assignment requirements" for the purpose of Code generation, Algorithm editing, and Documentation[cite: 5]. The output generated has been reviewed and verified by me for technical accuracy, safety, and originality[cite: 5]. I bear full responsibility for the work[cite: 5].
