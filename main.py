import random

from algorithms import bubbleSort, insertionSort, mergeSort, quickSort

randomItems = [random.randint(-50, 100) for x in range(20)]

print(f'Before: {randomItems}')

# sorting algorithms

# bubbleSort(randomItems)
# insertionSort(randomItems)
# mergeSort(randomItems)
quickSort(randomItems)

print(f'After: {randomItems}')