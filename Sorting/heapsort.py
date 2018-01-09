import random

def fix(i, heap):
    parent = i // 2
    while i > 0 and heap[parent] < heap[i]:
        heap[parent], heap[i] = heap[i], heap[parent] # swap
        i, parent = parent, parent // 2

def heapify(i, heap, heap_size):
    l, r = 2 * i + 1, 2 * i + 2
    g = i
    if l < heap_size and heap[l] > heap[g]:
        g = l
    if r < heap_size and heap[r] > heap[g]:
        g = r
    if g != i:
        heap[g], heap[i] = heap[i], heap[g]
        heapify(g, heap, heap_size)

def extract_insert(heap, heap_size):
    heap[0], heap[heap_size-1] = heap[heap_size-1], heap[0]
    heap_size -= 1
    heapify(0, heap, heap_size)
    return heap_size

def heap_sort(heap):
    heap_size = len(heap)
    for _ in range(len(heap)):
        heap_size = extract_insert(heap, heap_size)

if __name__ == '__main__':
    size = 50
    int_range = 100
    iterations = 100
    try:
        for _ in range(iterations):
            arr = [random.randint(1, int_range) for _ in range(size)]
            #print(arr)
            for i in range(len(arr)//2 - 1, -1, -1):
                heapify(i, arr, len(arr))
            heap_sort(arr)
            assert all(arr[i-1] <= arr[i] for i in range(1, len(arr))), 'Incorrect... {}'.format(arr)
    except AssertionError as e:
        print(e)
    else:
        print('all passed!!')
    

    
