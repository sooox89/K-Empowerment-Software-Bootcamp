#

try:
    raise "쉬는 시간!"  ##input도 실행되지 않고 except의 마지막 > ## 예외 발생! : exceptions must derive from BaseException 종료ㅔ
    expr = input('분자 분모 입력(띄어쓰기로 구분) : ').split()
    print(int(expr[0])/ int(expr[1]))
# ValueError
# ZeroDivisionError
except ValueError as err:
    print(f'숫자를 입력해주세요 ({err})')
except ZeroDivisionError as err:
    print(f'분모에 0이 올 수 없습니다 ({err}) ')
except IndexError:
    print(f'입력 값의 범위에 문제가 있습니다 ({err})')
except Exception as other:
    print(f'예외 발생! : {other}')
else: # 예외가 발생 하지 않았을 때  // 만약 (55 6)대입시, except실행되지 않고 else 실행됨 > ##값 프로그램 정상종료
    print('프로그램 정상', end='')
finally:  # 예외 발생 여부와 상관 없이 무조건 실행   // 만약 err > except실행되고 else 실행되지않음 > ##f'string 종료
    print('종료')

