# tuple
a = 'harry'
b = ('harry',)
c = () # empty tuple
d = 'harry', 'ron' # packing
e = ('hermione')  # string
f = ('harry', 'ron')  # packing
g = ('hermione',)
print(f[1])

x, y = f  # unpacking / 튜플로 한번에 여러 변수 할당
print(x) ## harry
print(y)  ## ron

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(g, id(g))
g = g+f   #concatenation
print(g, id(g))

