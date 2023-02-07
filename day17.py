## 함수 선언 부분 ##
def is_queue_full() :
	global SIZE, queue, front, rear
	if ( (rear + 1) % SIZE == front) :
		return True
	else :
		return False


def is_queue_empty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False


def en_queue(data) :
	global SIZE, queue, front, rear
	if (is_queue_full()) :
		print("큐가 꽉 찼습니다.")
		return
	rear = (rear + 1) % SIZE
	queue[rear] = data


def de_queue() :
	global SIZE, queue, front, rear
	if (is_queue_empty()) :
		print("큐가 비었습니다.")
		return None
	front = (front + 1) % SIZE
	data = queue[front]
	queue[front] = None
	return data


def peek() :
	global SIZE, queue, front, rear
	if (is_queue_empty()) :
		print("큐가 비었습니다.")
		return None
	return queue[(front + 1) % SIZE]

## 전역 변수 선언 부분 ##
SIZE = int(input("큐의 크기를 입력하세요 ==> "))
queue = [ None for _ in range(SIZE) ]
front = rear = 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
	select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	while (select != 'X' and select != 'x') :
		if select=='I' or select =='i' :
			data = input("입력할 데이터 ==> ")
			en_queue(data)
			print("큐 상태 : ", queue)
			print("front : ", front, ", rear : ", rear)
		elif select=='E' or select =='e' :
			data = de_queue()
			print("추출된 데이터 ==> ", data)
			print("큐 상태 : ", queue)
			print("front : ", front, ", rear : ", rear)
		elif select=='V' or select =='v' :
			data = peek()
			print("확인된 데이터 ==> ", data)
			print("큐 상태 : ", queue)
			print("front : ", front, ", rear : ", rear)
		else :
			print("입력이 잘못됨")

		select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

	print("프로그램 종료!")