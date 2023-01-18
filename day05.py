# Ch9 함수 fuction
#
# def inha(): #return도 없음
#     '''
#     숫자 출력 함수
#     :return:
#     '''
#     print(60)
#
# def call_func(f):
#     '''
#     매개변수로 함수를 넘겨 받아 실행
#     :param f: 매개변수가 함수
#     :return:
#     '''
#     f()  # 넘겨 받은 함수 실행
#
# call_func(inha)
# print(type(call_func))

def subtract(n1,n2):'''

    :param n1: 
    :param n2: 
    :return: 
    '''
    print(n1-n2)

def run_function(fuction,arg1,arg2): '''

    :param fuction: 첫 번쨰 인수는 함수
    :param arg1: 정수 값
    :param arg2: 정수 값
    :return: 
    '''
    fuction(arg1,arg2)
run_function(subtract,99,88)