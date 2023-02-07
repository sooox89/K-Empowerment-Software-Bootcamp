def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return False
def is_stack_empty():
    global SIZE,stack,top
    if top == -1:
        return  True
    return False

def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("Stack is full")
        return
    top = top +1
    stack[top] =data

def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is empty")
        return
    temp = stack[top]
    stack[top] = None
    top = top -1
    return temp
def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is empty")
        return None
    return stack[top]

def check_bracket(expr) :
	for ch in expr:
		if ch in '([{<':
			push(ch)
		elif ch in ')]}>':
			out = pop()
			if ch == ')' and out == '(':
				pass
			elif ch == ']' and out == '[':
				pass
			elif ch == '}' and out == '{':
				pass
			elif ch == '>' and out == '<':
				pass
			else:
				return False
		else :
			pass
	return is_stack_empty()


## 전역 변수 선언 부분 ##
SIZE = 100
stack = [ None for _ in range(SIZE) ]
top = -1

## 메인 코드 부분 ##
if __name__ == "__main__" :
    expression_arrray = ['2*[3+1)','(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']

    for expression in expression_arrray :
        top = -1
        print(expression, ':', check_bracket(expression))
