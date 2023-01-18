# Ch9 함수 fuction

#is_prime 함수 만들어보기 !

def isprime(n):

    '''
    매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
    :param n: integer number
    :return: true or false
    '''

    if n <= 1:
        return False
    for k in range(2,n):
        if n % k == 0:
            return False
    else:
        return True
#print(isprime(77))
#help(isprime)  ##주석처리의 함수 설명 나옴
start = int(input("input start number : "))
end = int(input("input end number : "))

if end < start:
    start,end = end, start

for i in range(start,end+1):
    if isprime(i):
        print(i, end=' ')

