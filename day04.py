#Ch8 dictionary

#ver.2
import random
alcohol_foods = {
    '맥주': '치킨',
    '소주': '골뱅이소면',
    '와인': '치즈',
    '고량주': '짬뽕'
}
alcohol_list = list(alcohol_foods) #extract keys
food_list = [food for food in alcohol_foods.values()]  #extract values and append list
#print(alcohol_list, food_list)

while True:
    alcohol = input(f'술을 선택하세요 1) {alcohol_list[0]} 2) {alcohol_list[1]} 3) {alcohol_list[2]} 4) {alcohol_list[3]} 5) 아무거나 6) 계산 : ')
    if alcohol == '6':
        print('다음에 또 오세요~')
        break
    elif alcohol == '1':
            print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다')
    elif alcohol == '2':
            print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다')
    elif alcohol == '3':
            print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다')
    elif alcohol == '4':
            print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다')
    elif alcohol == '5':
            print(f'{random.choice(alcohol_list)}에 어울리는 안주는 {random.choice(food_list)}입니다')
    else:
            print('메뉴에서 골라주세요')




