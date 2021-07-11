# stack - LIFO : Last In First Out
from collections import deque
# or use List
stack = deque()

# 스택 맨 끝에 데이터 추가 - append
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack)

print(stack[-1])

# 맨 끝 데이터 삭제 - pop function
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)