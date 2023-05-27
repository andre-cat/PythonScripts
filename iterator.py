from typing import Iterator

numbers: list[int] = [1, 2, 3]

iterator: Iterator[int] = iter(numbers)

for _ in range(len(numbers)):
    next_ = next(iterator)
    print(next_)
    if next_ == None:
        iterator = iter(list(iterator))