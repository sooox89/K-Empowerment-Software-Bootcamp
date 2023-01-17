# list

scores = ('B+', 'A+', 'C+')
print(scores[1],scores[2])
temp = list(scores)  # 임시로 scores tuple을 list로 변환
temp[1] = 'C+'       # list는 mutable 하기 때문에 변경 가능!!
temp[2] = 'A+'
scores = tuple(temp)  # 다시 list를 tuple로 변환
print(scores[1],scores[2])

# split함수 이용해서 list 만들기 // split함수 (문자열을 구분자 단위로 분할하여 리스트 생성)

# 오프셋

# append함수 // 리스트 끝에 새 항목 추가
# insert함수 // 원하는 위치에 추가
big_bang = ['GD', '태양','탑','대성', '승리']
exo = ['백현','첸']
#big_bang.append('인하')
big_bang.insert(1, '인하')  #1번 자리에 삽입
print(big_bang)
#print(big_bang * 2)
#exo.extend(big_bang)
#extend함수 // 다른 리스트 병합
#exo = exo + big_bang
exo.append(big_bang)    ##['백현', '첸', ['GD', '인하', '태양', '탑', '대성', '승리']]  // 리스트 안에 리스트생성
print(exo)
print(exo[2][2])  ## 태양
print(exo[2])     ##['GD', '인하', '태양', '탑', '대성', '승리']
print(exo[-1][-4]) ##태양

exo[-2] = '시우민'  #항목 바꾸기
print(exo)

#pop함수 // 리스트에서 항목을 가져오는 동시에 그 항목 삭제
#print(exo.pop())     #빅뱅 pop  #pop() == pop(-1)
print(exo[2].pop())  #승리 pop
print(exo)
print(exo[2].pop(-2))  #탑 pop
print(exo)
del exo[2][-1]  #대성 delete
print(exo)
#exo.remove('인하')   ##not in list
exo[2].remove('인하')
print(exo)
#clear함수 // 모든 항목 지우는 함수
exo.clear()
print(exo)


