def bubbleSort(items):
	for i in range(len(items)):
		for j in range(len(items)-1-i):
			if items[j] > items[j+1]:
				tmpItem = items[j]
				items[j] = items[j+1]
				items[j+1] = tmpItem

def insertionSort(items):
	for i in range(len(items)):
		j = i
		while j > 0 and items[j] < items[j-1]:
			tmpItem = items[j]
			items[j] = items[j-1]
			items[j-1] = tmpItem

			j -= 1