import random
from timeit import default_timer as timer

"""сортировка списка"""

my_list = []
for i in range(5000):
    my_list.append(i)
random.shuffle(my_list)
start_time = timer()
my_list.sort()
end_time = timer()
print(end_time - start_time)
print(my_list)


"""быстрая сортировка"""

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

start_time = timer()
quick_sort(my_list)
end_time = timer()
print(end_time - start_time)
print(my_list)

# сортировка с помощью встроенной функции sort() показала себя быстрее, чем "быстрая сортировка", реализованная по схеме Хоара