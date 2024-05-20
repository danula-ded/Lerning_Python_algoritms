def merge_sort(nums): 
    if len(nums) > 1: 
        mid = len(nums) // 2
        left = nums[:mid] 
        right = nums[mid:]
        merge_sort(left) 
        merge_sort(right) 
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                nums[k] = left[i] 
                i += 1
            else: 
                nums[k] = right[j] 
                j += 1
            k += 1
        while i < len(left): 
            nums[k] = left[i] 
            i += 1
            k += 1
        while j < len(right): 
            nums[k] = right[j] 
            j += 1
            k += 1

# Пример использования:
arr = [64, 25, 12, 22, 11]
print("Исходный массив:", arr)
merge_sort(arr)
print("Отсортированный массив:", arr)
