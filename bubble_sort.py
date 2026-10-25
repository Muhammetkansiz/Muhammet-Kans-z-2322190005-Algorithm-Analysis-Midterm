import time
import random
import tracemalloc

# =========================================================
# BUBBLE SORT IMPLEMENTATION
# =========================================================
def bubble_sort_trace(arr):
    """Küçük örnek dizilerde Bubble Sort prensibini adım adım ekrana yazdırır."""
    a = list(arr)
    n = len(a)
    print(f"\n[Bubble Sort Prensibi] Başlangıç: {a}")
    step = 1
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                print(f"  Adım {step:02d}: {a[j + 1]} > {a[j]} tespit edildi, yer değiştirildi -> {a}")
                swapped = True
                step += 1
        if not swapped:
            print("  Dizi sıralandı (erken çıkış / swapped=False).")
            break
    print(f"[Bubble Sort Sonuç]: {a}\n")


def bubble_sort(arr):
    """Metrik ölçümleri için performans sürümü."""
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return arr, comparisons, swaps


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
    print("  BUBBLE SORT WORKLOAD ANALİZİ & DEMO")
    print("=" * 55)

    print("\nA) KÜÇÜK ÖRNEK DİZİ ÜZERİNDE ÇALIŞMA PRENSİBİ")
    print("=" * 50)
    bubble_sort_trace(sample_array)

    print("=" * 50)
    print(f"B) CPU & MEMORY WORKLOAD ANALİZLERİ (N={size})")
    print("=" * 50)
    run_case_analysis("Bubble Sort", bubble_sort, best_data, "Best Case (Zaten Sıralı)")
    run_case_analysis("Bubble Sort", bubble_sort, avg_data, "Average Case (Rastgele)")
    run_case_analysis("Bubble Sort", bubble_sort, worst_data, "Worst Case (Tersten Sıralı)")