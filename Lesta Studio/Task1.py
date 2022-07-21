from timeit import default_timer as timer

def is_even(value):
    return value % 2 == 0

def even(value):
    return value & 1 == 0


start_time = timer()
num = is_even(14678577)
end_time = timer()
print(end_time - start_time)

start_time = timer()
nums = even(13456456456)
end_time = timer()
print(end_time - start_time)
print(num, nums)

# Первая функция проста в понимании, но вторая быстрее в обработке