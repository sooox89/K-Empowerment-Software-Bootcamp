stack = [ None for _ in range(5)]
top= -1

top = top +1
stack[top] = "커피"
top = top +1
stack[top] = "녹차"
top = top + 1
stack[top] = "꿀물"

for i in range(len(stack)-1,-1,-1):
    print(stack[i])

data = stack[top]
stack[top] = None
top = top -1
print(data)

