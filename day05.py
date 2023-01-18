# Ch9 함수 fuction
#ver.2 놀이공원 요금 계산 프로그램
# 몇명이 올지 모르는 상태 ! 몇살인지 모름! return : 방문 인원 몇명, 어른 몇명, 아이 몇명, total 얼마
import random
def calculate_fee(args) -> dict:
    '''
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: {'no_of_people' : 전체 인원수, 'no_of_adult' : 어른의 수, 'no_of_kid': 아이의 수, 'total_fee' : total}
    '''

    total = 0
    adults = 0
    kids = 0

    for age in args:
        if 19 <= age : #adult
            total = total + 10000
            adults = adults + 1
        else:
            total = total + 3000
            kids = kids + 1
 #   return [len(args), adults, kids, total]
    return {'no_of_people': len(args), 'no_of_adult': adults, 'no_of_kid': kids, 'total_fee': total}

no_of_visitor = int(input('몇 분 이세요?'))
ages = [random.randint(1,60) for age in range(no_of_visitor)]
results = calculate_fee(ages)
#print(f'{results[0]}명 방문하셨고 어른 {results[1]}명, 아이{results[2]}, 총 요금은 {results[-1]}원 입니다')
print(f'{results['no_of_people']명 방문하셨고 어른 {results['no_of_adult']명, 아이 {results['no_of_kid'] 명, 총 요금은 {results[total]}입니다')
# 5분 방문하셨고 어른 2명 아이 3명 총 요금은 10000원 입니다.

# # print(calculate_fee(20,20,25))
# # print(calculate_fee(45,43,10,7))
#

