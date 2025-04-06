# (Sorted Maps - Insertion Order
from collections import OrderedDict

ordered_dict = OrderedDict([('x', 1), ('b', 2), ('c', 3)])
print(ordered_dict)

#Sorted Maps - Key Order
my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_items = sorted(my_dict.items())
print(sorted_items)  # Output: [('a', 1), ('b', 2), ('c', 3)]

from collections import deque
my_queue = deque()
my_queue.append(1)
my_queue.append(2)
first_item = my_queue.pop()
print(first_item)

#First-In, First-Out) queues
import queue
my_q = queue.Queue()
my_q.put(10)
my_q.put(11)
item = my_q.get()
print(item)

#Priority Queue - min heap
import heapq
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
lowest = heapq.heappop(min_heap)
print(lowest)  # Output: 1


max_heap = []
heapq.heappush(max_heap,-1)
heapq.heappush(max_heap,-3)
heapq.heappush(max_heap,-2)
heapq.heappush(max_heap,-5)
highest = -heapq.heappop(max_heap)
print(highest)



# Counter
from collections import Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_counts = Counter(words)
print(word_counts)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# char map of a string
str1 = 'dinesh'
#print(str1.split(""))
charMap = Counter(list(str1))
print(charMap)
print(charMap.items())
print(charMap.keys())
print(charMap.values())


#heap functions
print("heapify")
list111 = [1,4,4,2,2,7,6,]
heapq.heapify(list111)
print(list111)

print(heapq.heappop(list111))
print(heapq.heappop(list111))
print(heapq.heappop(list111))


