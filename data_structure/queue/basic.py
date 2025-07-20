from collections import deque

def test_queue():
    q = deque()

    q.append(1)
    print(q.pop())

test_queue()