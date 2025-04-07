import gc

# Disable automatic GC for demonstration
gc.disable()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a reference cycle
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

# At this point, node1 and node2 form a cycle. Their reference counts are 1 (from the variables node1 and node2),
# but they are no longer reachable from the outside if we delete node1 and node2.
del node1
del node2

# The memory occupied by the cycle would not be reclaimed by reference counting alone.
# The garbage collector will identify and collect this cycle.

# Enable automatic GC again
gc.enable()