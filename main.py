import random

from algorithms import bubbleSort, insertionSort

randomItems = [random.randint(-50, 100) for x in range(20)]

print(f'Before: {randomItems}')

# sorting algorithms

# bubbleSort(randomItems)
insertionSort(randomItems)

print(f'After: {randomItems}')