numbers : list[int] = [1, 2, 3, 4, 5]

# this doesn't save memory
for number in numbers:
    print(number)

# this save memory
iterator = iter(numbers)
for number in iterator:
    print(number)

try:
    iterator = iter(numbers)
    for number in range(len(numbers)+1):
        print(next(iterator))
except Exception as e:
    print('StopIteration')