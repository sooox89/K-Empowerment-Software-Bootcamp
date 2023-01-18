# Ch9 함수 fuction
#ver.2 놀이공원 요금 계산 프로그램
# v0.2 return Dictionary
import random


def calculate_fee(args) -> dict:
    """
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: {'no_of_people':전체 인원 수, 'no_of_adult':어른 수, 'no_of_kid':아이 수, 'total_fee':지불할 총 입장료}
    """
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 19 <= age:  # adult
            total = total + 10000
            adults = adults + 1
        else:
            total = total + 3000
            kids = kids + 1
    return {'no_of_people': len(args), 'no_of_adult': adults, 'no_of_kid': kids, 'total_fee': total}

help(len)
no_of_visitor = int(input('몇 분 이세요? '))
ages = [random.randint(1, 60) for age in range(no_of_visitor)]
results = calculate_fee(ages)
print(f"{results['no_of_people']}명 방문 하셨고 어른 {results['no_of_adult']}명, 아이 {results['no_of_kid']}명 총 요금은 {results['total_fee']}원 입니다")
