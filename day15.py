# code 03-05

def print_poly(px):
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수
        if i > 0 and  coef > 0:
            poly_str = poly_str + "+"

        elif coef == 0:
            term = term - 1
            continue
        poly_str = poly_str + f'{coef}x^{term} '
        term = term - 1


    return  poly_str


def cal_ploy(x_val, px):
    ret_value = 0
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = px[i]  # 계수
        ret_value += coef * x_value ** term
        term = term - 1

    return ret_value


## 전역 변수 선언 부분 ##
px = [3, -4, 0, 6]  # = 3x^3 -4x^2 +0x^1 +6x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = print_poly(px)
    print(pStr)

    x_value = int(input("X값 : "))

    print(cal_ploy(x_value, px))

