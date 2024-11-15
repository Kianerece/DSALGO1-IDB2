# Assuming LinkedDeque and LinkedQueue are implemented with the usual methods


D = LinkedDeque()  # Initialize deque with given elements
Q = LinkedQueue()  # Initialize empty queue

# Insert initial values into the deque
for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    D.insert_last(i)

# Step 1: Move the first three elements from D to Q and back to D to retain order
Q.enqueue(D.delete_first())  # Q: [1]
Q.enqueue(D.delete_first())  # Q: [1, 2]
Q.enqueue(D.delete_first())  # Q: [1, 2, 3]

D.insert_last(Q.dequeue())  # D: [4, 5, 6, 7, 8, 1]
D.insert_last(Q.dequeue())  # D: [4, 5, 6, 7, 8, 1, 2]
D.insert_last(Q.dequeue())  # D: [4, 5, 6, 7, 8, 1, 2, 3]

# Step 2: Move the fourth element (4) to Q and swap it with 5 from D
Q.enqueue(D.delete_first())  # Q: [4], D: [5, 6, 7, 8, 1, 2, 3]

# Step 3: Move 5 to end of D, then move 4 from Q back to D
D.insert_last(D.delete_first())  # D: [6, 7, 8, 1, 2, 3, 5]
D.insert_last(Q.dequeue())       # D: [6, 7, 8, 1, 2, 3, 5, 4]

# Step 4: Rotate the deque to bring the elements in correct order
for _ in range(3):
    D.insert_first(D.delete_last())  # Rotate last 3 elements to front

# Final result
# After this code, D should contain the elements in the order: (1, 2, 3, 5, 4, 6, 7, 8)
