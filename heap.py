class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        
        self._bubble_down(0)
        
        return min_val

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _bubble_up(self, index):
        parent = self._parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    def _bubble_down(self, index):
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

# Test
heap = MinHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(0)

print(heap.pop())  # 0
print(heap.pop())  # 1
print(heap.pop())  # 3
