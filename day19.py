import random

## 함수 선언 부분 ##
def find_insert_idx(ary, data) :
	find_idx = -1			# 초깃값은 없는 위치로
	for i in range(0, len(ary)) :
		if (ary[i] < data ) :
			find_idx = i
			break
	if find_idx == -1 :			# 큰 값을 못찾음 == 제일 마지막 위치
		return len(ary)
	else :
		return find_idx

## 전역 변수 선언 부분 ##
before = [random.randint(0,200) for  _  in range (10)]
after = []

## 메인 코드 부분 ##
print('정렬 전 -->', before)
for i in range(len(before)) :
	data = before[i]
	insert_position = find_insert_idx(after, data)
	after.insert(insert_position, data)
print('정렬 후 -->', after)