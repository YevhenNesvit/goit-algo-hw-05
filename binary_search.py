def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return iterations, arr[mid]

    # Якщо елемент не знайдено, повертаємо "верхню межу"
    upper_bound = arr[left] if left < len(arr) else None
    return iterations, upper_bound

# Приклад використання
sorted_array = [0.1, 0.5, 1.2, 2.0, 3.5, 4.8, 5.2, 6.7, 7.1]
target_value = 3.6

print(binary_search(sorted_array, target_value))