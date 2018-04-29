dict1 ={'Name': 'Ose','Hall':'John','RoomNo':407}
# print('Room Number: ', dict1['RoomNo'])
dict1['Hall'] = 'Paul'
dict1['course']='computer Science'
print(dict1)
del dict1['RoomNo']
name = str(dict1)
print(name)
dict1.clear()
print(dict1)