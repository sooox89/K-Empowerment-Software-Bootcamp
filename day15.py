# 응용예제 2
## 함수 선언 부분 ##
def printPoly(px):
	poly_str = "P(x) = "

	for i in range(len(px[0])):
		term = px[0][i]	# 항 차수
		coef = px[1][i]	# 계수

		if (coef >= 0):
			poly_str += "+"
		poly_str += str(coef) + "x^" + str(term) + " "

	return poly_str


def calcPoly(xVal, p_x):
	ret_value = 0

	for i in range(len(p_x[0])):
		term = p_x[0][i]	# 항 차수
		coef = p_x[1][i]	# 계수
		ret_value += coef * xValue ** term
		term -= 1

	return ret_value


## 전역 변수 선언 부분 ##
px = [ [300, 20, 0],
		[7, -4, 5] ]

## 메인 코드 부분 ##
if __name__ == "__main__":
	pStr = printPoly(px)
	print(pStr)

	xValue = int(input("X 값-->"))

	pxValue = calcPoly(xValue, px)
	print(pxValue)