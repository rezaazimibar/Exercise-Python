from functools import reduce

# def dupArr(list):
#     newlist = []
#     for item in list:
#         newlist.append(item * 2)
#     return newlist
#
#
# print(dupArr([34, 53, 2]))

# map functional
# def dupLisMap(list):
#     return list * 3
#
#
# print(f"function with map 🎢🎢{list(map(dupLisMap, [3, 5, 2, 15, 7]))}")
# #string loop
# def strToArr(str):
#     return str
# name="reza azimi"
# mapObject=map(strToArr,name)
# print(f"giv it a name and return it to a object: \n{list(mapObject)}")
# /////////////////////////////////////////////////////////////////////////////////
# filter function😀😀
# myList = [34, 5, 2, 5,6, 4634, 343, 23428]
#
#
# def filter_function(item):
#     return item % 71 != 0
#
#
# print(list(filter(filter_function, myList)))
# reduce function😀😀
#
# mylist = [34, 55, 234, 453, 234, 22, 454, 534, 345]
#
#
# def accumultor(acc, item):
#     print(acc,item)
#     return acc * item
#
#
# print(reduce(accumultor, mylist, 2))
# /////////////////////////////////////////////////////////////////////////////////////
# lambda😀😀
# mylist = [3, 5, 2, 6]
# multiList = list(filter(lambda item: item % 2 == 0, mylist))
# print(reduce(lambda acc, item: item ** 2, mylist))
# print(list(map(lambda item: item ** 2, mylist)))
# print(multiList)
#
#
# myTuple = [(23, 4), (32, -5), (45, 2), (4, 8), (87, 9)]
# myTuple.sort(key=lambda item: item[1])
# print(myTuple)
# comprehensions😀😀
# mylist = [char for char in "my name is hello"]
# mylist2 = [num ** 2 for num in range(0, 100)]
# mylist3 = [num ** 2 for num in range(0, 100) if num % 2 != 0]
# print(mylist2)
# print(mylist)
# print(mylist3)
#
# simpledic = {'df': 45, 'dfs': 44}
# mydict = {key: value ** 7 for key, value in simpledic.items()}
# print(f"dictionary is {mydict}")
# # excersise😉😉
# mylist = ['d', 'd', 's']
# print(mylist.count("d"))
# duplicatelist = list(set(char for char in mylist if mylist.count(char) > 1))
# print(duplicatelist)
