# when doing heap sort in place, we divided
# the array into 2 parts:
#   index [1] to index [heap length - 1] is the heap
#   index [heap length] to index [array length - 1]
#     is the subset of sorted array
# we make use of the O(lg n) time extraction of
# maximum element from max heap, and put it at the
# beginning of the sorted subset at the end, e.g.:
#   init:   [max, a1, a2, a3, ...]
#   loop 1: [2nd-max, a1', a2', a3', ..., max]
#   loop 2: [3rd-max, a1'', a2'', a3'', ..., 2nd-max, max]
#   etc.
def heapSort(arr):
	buildMaxHeap(arr)
	heapLen = len(arr)

	for i in range(len(arr)-1, 1, -1):
		# put the max at the end if sorted subset,
		# and put the last leaf node of the tree
		# to the top
		arr[i], arr[1] = arr[1], arr[i]

		# now the length of heap is reduced by 1,
		# and the length of the subset of sorted
		# array is increased by 1
		heapLen -= 1

		# because the original last leaf node is
		# now on root, we need to repair the max
		# heap property again, it takes O(lg n)
		_maxHeapify(arr, 1, heapLen)

	del arr[0]	# remove dummy element at beginning

	return arr

def buildMaxHeap(arr):
	# in order to maintain the property that 
	# left child of i is in i * 2
	# right child of i is in i * 2 + 1
	# we need to insert dummy element to the beginning
	# since 0 * (anything) = 0, which
	# violate the property stated above
	arr.insert(0, 0)

	# start from the bottom of the tree,
	# we "heapify" the subtree incrementally
	# why is it work? let see the loop invariant:
	#   init: every leaf node of the tree is already
	#     heapify since they have only one element
	#   maintain: from bottom up to the top, because
	#     the subtree under the current node is 
	#     already heapify, make the tree of current 
	#     node heapify is simply "push" the current 
	#     node down to the suitable position
	#   terminate: the loop stop on index 1,
	#     that is the first node of the tree, so
	#     all nodes in the tree is now satisfy the
	#     max heap property

	# the loop start at the last parent node of the
	# tree, since all leaf nodes are already heapify
	lastNodeIdx = len(arr)-1
	lastParentIdx = lastNodeIdx//2
	for i in range(lastParentIdx, 0, -1):
		_maxHeapify(arr, i, len(arr))

	return arr

# this function assume the subtree under the current
# node is already heapified, it will make the tree
# of current node heapify because:
#   by comparing the current node with it's childs,
#   3 cases will happen:
#     - current node is already the max: do nothing
#     - left child is the max: swap it with current
#       node
#     - right child is the max: same action as above
#   for case 2 and 3, we don't need to touch the child
#   on the non-swapped side, since arr[newMaxIdx] >= 
#   arr[nonSwappedChildIdx] after swap, and subtree
#   under non-swapped index is already heapified,
#   therefore we only go for the swapped side child's
#   substree and try to repair the heap property of
#   it recursively
def _maxHeapify(arr, i, heapLen):
	maxIdx = i

	# declare these variables for clarity
	leftChildIdx = i * 2
	rightChildIdx = i * 2 + 1

	# max sure the left child idx (i*2) exists
	if leftChildIdx < heapLen:
		if arr[i] < arr[leftChildIdx]:
			maxIdx = leftChildIdx

	# max sure the right child idx (i*2+1) exists
	if rightChildIdx < heapLen:
		if arr[maxIdx] < arr[rightChildIdx]:
			maxIdx = rightChildIdx

	# if swap needed, call the function recursively
	# on the swapped side
	if maxIdx != i:
		arr[i], arr[maxIdx] = arr[maxIdx], arr[i]
		_maxHeapify(arr, maxIdx, heapLen)
