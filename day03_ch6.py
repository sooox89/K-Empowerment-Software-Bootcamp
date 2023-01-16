
#while, for문 교수님예제
#prime number


#while문 ver.1
number = int(input("input number: "))
counts = 0

k = 1
while k <= number:
    if number % k == 0:
        counts = counts + 1      # counts += 1
    k = k + 1
if counts == 2:
    print('f{number} is prime number!')
else:
    print('f{number} is NOT prime number!')

#for문 ver.2
number = int(input("input number: "))
counts = 0

for k in range(1, number+1):
    if number % k == 0:
        counts = counts + 1
if counts == 2:
    print('f{number} is prime number!')
else:
    print('f{number} is NOT prime number!')


# ver.3
number = int(input("input number: "))
counts = 0

for k in range(1, number + 1):
    if number % k == 0:
        counts = counts + 1
if counts:
    print('f{number} is prime number!')
else:
    print('f{number} is NOT prime number!')

# ver.4
number = int(input("input number :"))
is_prime = True   #변수 boolean 타입으로

for k in range(2, number):
    if number % k ==0:
        is_prime = False
        break
    print(k)

if is_prime:
    print('f{number} is prime number!')
else:
    print('f{number} is NOT prime number!')