#9-2 prof ##generating
cnts = 0 #counts = 0
def get_odds():
    for num in range(10):
        if num  % 2 == 1:
            yield num

odds = get_odds()
for i in odds:
    cnts +=1   ##counts 루프 돌면서 +1
    if cnts == 3:
        print(i)

# def get_odds(first=0,last=10,step=1):
#
#
#
# #ex 9-1
#
# def good():
#
#
#
#
# #ex 9-2
# import random
# def get_odds(odds):
#     for odds in range(10):
#         odds % 2 == 1
