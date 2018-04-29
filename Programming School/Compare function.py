'''def double_stuff(a_list):
    for index, value in enumerate(a_list):
        a_list[index]=2*value
things=[2,5, 'spam', 9.5]
double_stuff(things)
print(things)
'''
def double_stuff(a_list):
    new_list=[]
    for vailue in a_list:
        new_list += [2 * value]
    return new_list
