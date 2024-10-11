
from collections import deque

queue = deque()
def simulate_queue(operations):
    result = []
    for op in operations:
        if "enqueue" in op:
            # Extract the value to enqueue
            value = int(op.split('(')[1].strip(')'))
            queue.append(value)
            print(f"Enqueued: {value}")
        elif "dequeue" in op:
            if queue:
                dequeued_value = queue.popleft()
                result.append(dequeued_value)
                print(f"Dequeued: {dequeued_value}")
            else:
                result.append(None)
                print("Dequeued: None (Queue is empty)")
    return result


operations = [
    "enqueue(5)", "enqueue(3)", "dequeue()",
    "enqueue(2)", "enqueue(8)", "dequeue()",
    "dequeue()", "enqueue(9)", "enqueue(1)",
    "dequeue()", "enqueue(7)", "enqueue(6)",
    "dequeue()", "dequeue()", "enqueue(4)",
    "dequeue()", "dequeue()"
]


dequeued_elements = simulate_queue(operations)
print("Final queue state:", list(queue))
print("Returned Values:", dequeued_elements)
