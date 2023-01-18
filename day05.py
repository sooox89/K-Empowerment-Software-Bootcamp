#ch9
#closures

def calculate():
    x = 1
    y = 2
    temp = 0
    def add_sub(n):
        nonlocal temp
        # x = 11   #local variable
        temp = temp + x + n - y
        return temp
    return add_sub

c1 = calculate()       #calculate함수를 call
for i in range(5):     #range(5)=1~4
    print(c1(i))

print(type(c1))
print(c1)


