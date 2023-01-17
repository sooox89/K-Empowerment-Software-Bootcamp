# list // sort / sorted /

#mixed = [6, 4, 5, 'A', 7, '트와이스', 'B', 'b', '마마무']   ## type error // 비교해서 정렬하는데 타입이 달라서 오류가 생김
mixed = ['6', '4', '5', 'A', '7', '트와이스', 'B', 'b', '마마무']
#mixed.sort()              ## ['4', '5', '6', '7', 'A', 'B', 'b', '마마무', '트와이스']
mixed.sort(reverse=True)   ##['트와이스', '마마무', 'b', 'B', 'A', '7', '6', '5', '4']
print(mixed)


primes = [2, 19, 3, 5, 7, 11]
primes_cp =primes
print(primes)       ##[2, 19, 3, 5, 7, 11]
print(primes_cp)    ##[2, 19, 3, 5, 7, 11]
primes[-1] = 'lunch time'    # primes만 바꾸었는데 primes_cp도 바뀌었다
print(primes)       ##[2, 19, 3, 5, 7, 'lunch time']
print(primes_cp)    ##[2, 19, 3, 5, 7, 'lunch time']
primes_cp[0] = 'sooo'        # 참조하고 있는 list가 같음 >> 하나가 바뀌면 둘다 바뀜
print(primes)       ##['sooo', 19, 3, 5, 7, 'lunch time']
print(primes_cp)    ##['sooo', 19, 3, 5, 7, 'lunch time']



a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]
a[2] = 'sw'
print(a,b,c,d)   ##[1, 2, 'sw'] [1, 2, 3] [1, 2, 3] [1, 2, 3]   // 복제값은 바뀌지 않음  //immutable 원소 값이라 제대로 작동

a = [1,2,[8,9]]
b = a.copy()
c = list(a)
d = a[:]
print(a,b,c,d)   ##[1, 2, [8, 9]] [1, 2, [8, 9]] [1, 2, [8, 9]] [1, 2, [8, 9]] // list 참조라 원본, 사본 모두 변경됨 // deep copy X
# deep copy
import copy
a = [1,2,[8,9]]
b = copy.deepcopy(a)
a[2][1] = 7  #mutable,deepcopy
print(a,b)     ##[1, 2, [8, 7]] [1, 2, [8, 9]]


#primes = [2, 19, 3.0, 5, 7, 11]
#print(primes)
#primes.sort()
#print(primes)

#primes = [2, 19, 3.0, 5, 7, 11]
#primes_sorted = sorted(primes)
#print(primes)
#print(primes_sorted)

