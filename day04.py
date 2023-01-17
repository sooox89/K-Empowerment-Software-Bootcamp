# list comprehension / generator comprehension
odd_lists = [ i for i in range(1,11) if i % 2 == 1]
odd_tuples = (i for i in range(1,11) if i % 2 == 1)

#print(odd_tuples, type(odd_tuples))  ##<class 'generator'>
#print(odd_lists, type(odd_lists))    ##[1, 3, 5, 7, 9] <class 'list'>


#odd_lists = []
#for i in range(1,11):
#    if i % 2 == 1:
#        odd_lists.append(i)
#print(odd_lists)


