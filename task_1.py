import timeit
import random

# Сортування вставками


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сортування злиттям


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Використання Timsort (вбудована функція sorted)


def timsort(arr):
    return sorted(arr)

# Функція для генерації випадкового масиву


def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Функція для тестування алгоритму сортування та виміру часу виконання


def test_sort_algorithm(algorithm, size, trials):
    total_time = 0
    for _ in range(trials):
        arr = generate_random_array(size)
        start_time = timeit.default_timer()
        algorithm(arr)
        total_time += timeit.default_timer() - start_time
    return total_time / trials


# Розміри масивів для тестування та кількість прогонів
sizes = [100, 500, 1000, 2500, 5000, 10000]
trials = 5

# Тестування алгоритмів
for size in sizes:
    print(f"Testing arrays of size {size}")
    print(
        f"Insertion Sort: {test_sort_algorithm(insertion_sort, size, trials):.6f} seconds")
    print(
        f"Merge Sort: {test_sort_algorithm(merge_sort, size, trials):.6f} seconds")
    print(
        f"Timsort (sorted): {test_sort_algorithm(timsort, size, trials):.6f} seconds")
    print()
