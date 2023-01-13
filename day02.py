##Chap 4 if

limits = 20
tweets = "pass" *  4
if limits - len(tweets) >= 0 :
    print(tweets)
else :
    print('제한 글자 수 초과')


limits = 20
tweets = "pass" *  6
diff = limits - len (tweets)
if diff >= 0:
    print(tweets)
# if diff := limits - len(tweets) >= 0 :

else :
    print(f'글자수 {abs(diff)}초과')

import random

limits = 20
tweets = "pass" * random.randint(1,10) # 1에서 10 사이의 정수가 임의로 발생
diff = limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f'글자수 {abs(diff)}초과')




print(bool([]))
print(bool([set()]))
print(bool([dict()]))

a= []
print(bool(a))
a.append(5)
print(bool(a))
print(bool([set()]))
print(bool([dict()]))


vowels ='aeiou'
letter = 'x'
if letter in vowels:
    print("실행안됨")

vowels ='aeiou'
letter = 'u'
if letter in vowels:
    print("실행 됨 !")

vowels ='aeiou'
letter = 'u'
if letter not in vowels:
    print("실행 안됨")

