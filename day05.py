#ch9
#lambda//

import random
def process(no_list, f):
    for no in no_list:
        print(f(no))


## fuction as parameter
# def squares(n):
#     '''
#     제곱 함수
#     :param n:
#     :return:
#     '''
#     return n * n

numbers = [random.randint(1,100) for i in range(5)]
print(numbers)
# process(numbers, squares)
process(numbers, lambda x: x * x)  #lambda

