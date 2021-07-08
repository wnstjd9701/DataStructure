# deque
from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("1")
queue.append("2")
queue.append("3")
queue.append("4")
queue.append("5")

print(queue)

# 큐의 가장 앞 데이터 접근
print(queue[0])

# 맨 앞 데이터 삭제 -  popleft
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)