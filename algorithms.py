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

def mergeSort(items):
	if len(items) > 1:
		middleIndex = int(len(items)/2)
		left = items[0:middleIndex]
		right = items[middleIndex:]

		mergeSort(left)
		mergeSort(right)

		leftIndex, rightIndex = 0, 0
		for i in range(len(items)):
			leftValue = left[leftIndex] if leftIndex < len(left) else None
			rightValue = right[rightIndex] if rightIndex < len(right) else None

			if (leftValue and rightValue and leftValue < rightValue) or rightValue is None:
				items[i] = leftValue
				leftIndex += 1
			elif (leftValue and rightValue and leftValue >= rightValue) or leftValue is None:
				items[i] = rightValue
				rightIndex += 1
			else:
				raise Exception('Could not merge!')

def quickSort(items):
	if len(items) > 1:
		pivotIndex = int(len(items)/2)
		smallerItems = []
		largerItems = []

		for i, value in enumerate(items):
			if i != pivotIndex:
				if value < items[pivotIndex]:
					smallerItems.append(value)
				else:
					largerItems.append(value)
		
		quickSort(smallerItems)
		quickSort(largerItems)
		items[:] = smallerItems + [items[pivotIndex]] + largerItems