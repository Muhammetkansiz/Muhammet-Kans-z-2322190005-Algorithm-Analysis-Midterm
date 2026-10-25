import time
import random
import tracemalloc

# =========================================================
# TIMSORT IMPLEMENTATION
# =========================================================
MIN_MERGE = 32


def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort_slice(arr, left, right, stats=None):
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        while j >= left:
            if stats:
                stats["comparisons"] += 1
            if arr[j] > temp:
                arr[j + 1] = arr[j]
                if stats:
                    stats["writes"] += 1
                j -= 1
            else:
                break
        arr[j + 1] = temp
        if stats:
            stats["writes"] += 1


def merge(arr, left, mid, right, stats=None):
    len1 = mid - left + 1
    len2 = right - mid

    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len1 and j < len2:
        if stats:
            stats["comparisons"] += 1
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        if stats:
            stats["writes"] += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        if stats:
            stats["writes"] += 1
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_part[j]
        if stats:
            stats["writes"] += 1
        j += 1
        k += 1


def tim_sort_trace(arr):
    """Küçük örnek dizide TimSort prensibini (run + merge) gösterir."""
    a = list(arr)
    n = len(a)
    print(f"\n[TimSort Prensibi] Başlangıç: {a}")
    run_size = 4  # Görselleştirme için küçük dizide sembolik run boyutu

    # 1. Aşama: Parçalara Insertion Sort
    for start in range(0, n, run_size):
        end = min(start + run_size - 1, n - 1)
        insertion_sort_slice(a, start, end)
        print(f"  Parça Sıralandı [{start}:{end}]: {a[start:end + 1]} -> Güncel Dizi: {a}")

    # 2. Aşama: Sıralı parçaları birleştirme (Merge)
    size = run_size
    merge_step = 1
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(a, left, mid, right)
                print(f"  Merge Adımı {merge_step}: Sol=[{left}:{mid}], Sağ=[{mid + 1}:{right}] -> Güncel Dizi: {a}")
                merge_step += 1
        size *= 2

    print(f"[TimSort Sonuç]: {a}\n")


def tim_sort(arr):
    n = len(arr)
    min_run = calc_min_run(n)
    stats = {"comparisons": 0, "writes": 0}

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_slice(arr, start, end, stats)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(arr, left, mid, right, stats)
        size *= 2

    return arr, stats["comparisons"], stats["writes"]


def run_case_analysis(algorithm_name, sort_func, data, case_label):
    arr_copy = list(data)
    tracemalloc.start()
    t0 = time.perf_counter()

    sorted_arr, comparisons, ops = sort_func(arr_copy)

    elapsed = time.perf_counter() - t0
    _, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"[{case_label.upper()}] - Boyut: {len(data)}")
    print(f"  * Süre:                 {elapsed:.6f} saniye")
    print(f"  * Karşılaştırma Sayısı: {comparisons:,}")
    print(f"  * İşlem/Takas Sayısı:   {ops:,}")
    print(f"  * Peak Bellek Yükü:     {peak_mem / 1024:.2f} KB")
    print("-" * 50)


if __name__ == "__main__":
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    size = 2000

    best_data = list(range(size))
    worst_data = list(range(size, 0, -1))
    avg_data = [random.randint(0, 100000) for _ in range(size)]

    print("=" * 55)
    print("  TIMSORT WORKLOAD ANALİZİ & DEMO")
    print("=" * 55)

    print("\nA) KÜÇÜK ÖRNEK DİZİ ÜZERİNDE ÇALIŞMA PRENSİBİ")
    print("=" * 50)
    tim_sort_trace(sample_array)

    print("=" * 50)
    print(f"B) CPU & MEMORY WORKLOAD ANALİZLERİ (N={size})")
    print("=" * 50)
    run_case_analysis("TimSort", tim_sort, best_data, "Best Case (Zaten Sıralı)")
    run_case_analysis("TimSort", tim_sort, avg_data, "Average Case (Rastgele)")
    run_case_analysis("TimSort", tim_sort, worst_data, "Worst Case (Tersten Sıralı)")