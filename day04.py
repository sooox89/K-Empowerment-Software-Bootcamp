#Ch8 dictionary
##p.184



alcohol_foods = dict(맥주='치킨', 소주='골뱅이 소면', 위스키='치즈', 고량주='짬뽕')
alcohol_list =list(alcohol_foods)
food_list = [food for food in alcohol_foods.values()]
for food in enumerate(food_list):    ## tuple return
    print(food[1])


#for i in range(len(food_list)):
#    print(food_list[i])

#for food in food_list:
#   print(food)
