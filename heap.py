def buildMaxHeap(arr):
	heap = arr[:]
	heap.insert(0, 0)
	for i in range(len(heap)//2, 0, -1):
		_maxHeapify(heap, i)
	return heap

def _maxHeapify(arr, i):
	maxIdx = i
	if i*2 < len(arr) and arr[i] < arr[i*2]:
		maxIdx = i*2
	if i*2+1 < len(arr) and arr[maxIdx] < arr[i*2+1]:
		maxIdx = i*2+1
	if maxIdx != i:
		arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
		_maxHeapify(arr, maxIdx)
