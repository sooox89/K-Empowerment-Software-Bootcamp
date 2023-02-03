# code 04-05
# simple linked list
## 클래스와 함수 선언 부분 ##
class Node():
	def __init__(self):
		self.data = None
		self.link = None


def print_nodes(start):
	current = start
	if current == None :
		return
	print(current.data, end=' ')
	while current.link != None:
		current = current.link   # 다음 노드로 이동
		print(current.data, end=' ')
	print()


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()		# 첫 번째 노드
	node.data = data_array[0]
	head = node
	memory.append(node)

	for data in data_array[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node    # 이전 링크를 노드에 연결
		memory.append(node)

	print_nodes(head)