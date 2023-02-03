# code 03-04

def insert_data(idx, pokemon):
    """
    선형 리스트의 idx 위치에 원소 삽입
    :param idx:
    :param pokemon:
    :return:
    """
    if idx < 0 or idx > len(pokemons):
        print("out of range !")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


def delete_data(idx):
    """
    선형 리스트 idx 위치의 원소 삭제
    :param idx: int
    :return: void
    """
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)
    pokemons[idx] = None
    for _ in range(len_pokemons - idx):
        pokemons.pop()


    # for i in range(idx + 1, len_pokemons):
    #     pokemons[i - 1] = pokemons[i]
    #     pokemons[i] = None
    #
    # del (pokemons[len_pokemons - 1])
    # pokemons.pop()


    # for i in range(idx+1,len_pokemons):
    #     pokemons[i] = None  # 데이터 삭제
    #
    # for i in range(idx , len_pokemons):
    #     pokemons.pop()


def add_data(pokemon):
    """
    선형 리스트
    :param pokemon:
    :return:
    """
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon

pokemons = []
menu = -1

if __name__ == "__main__":   ## 메인 코드 부분 ##

    while menu != 4:

        menu = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

        if (menu == 1):
                data = input("추가할 데이터--> ")
                add_data(data)
                print(pokemons)
        elif (menu == 2):
                pos = int(input("삽입할 위치--> "))
                data = input("추가할 데이터--> ")
                insert_data(pos, data)
                print(pokemons)
        elif (menu == 3):
                pos = int(input("삭제할 위치--> "))
                delete_data(pos)
                print(pokemons)
        elif (menu == 4):
                print(pokemons)
                exit()
                print("menu에서 고르세요")
                continue







    #
    # # insert_data(2, '거북왕')
    # # pokemons.insert(2,'거북왕')
    # delete_data(1)
    # print(pokemons)
    # # insert_data(6, '어니부기')
    # # pokemons.insert(6,'어니부기')
    # delete_data(3)
    # print(pokemons)
    # add_data('터검니')
    # print(pokemons)
    #
    #








