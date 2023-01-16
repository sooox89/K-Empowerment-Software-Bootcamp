#while 구구단 // continue / break /
#for 반복문

while True:
    dan = int(input('Dan (0 to quit): '))

    if dan == 0 : #exit
        break
    if 1< dan < 10 : # if dan >=2 and dan <=9:
        for i in range(1,10):
            print('{0}*{1}')