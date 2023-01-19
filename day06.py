#day6
#교수님꺼 clone

def factorial_iter(n):
    """
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return: integer 팩토리얼 계산 결과 값
    """
    result = 1
    for k in range(1, n+1):
        result = result * k
    return result


def factorial_recu(n):
    """
    재귀 함수를 사용한 팩토리얼 계산 함수
    :param n: n!
    :return: 자기 자신을 호출 또는 1
    """
    if n == 1:  # 끝나는 조건
        return 1
    else:
        return factorial_recu(n-1) * n


print(factorial_iter(5))
print(factorial_recu(5))

try:
    expr = input('분자 분모 입력(띄어쓰기로 구분) : ').split()
    print(int(expr[0])/ int(expr[1]))
# ValueError
# ZeroDivisionError
except ValueError:
    print('숫자를 입력해주세요')
except ZeroDivisionError:
    print('분모에 0이 올 수 없습니다')
except IndexError:
    print('입력 값의 범위에 문제가 있습니다')
except:
    print('예외 발생!')