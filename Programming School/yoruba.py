numbers = dict()
'''yoruba[1] = 'ikan'
yoruba[2] = 'meji'
yoruba[3] = 'meta'
yoruba[4] = 'merin'
yoruba[5] = 'marun'
yoruba[6] = 'mefa'
yoruba[7] = 'meje'
yoruba[8] = 'mejo'
yoruba[9] = 'mesan'
yoruba[10] = 'mewa'
print (yoruba)'''

numbers['odd_numbers'] = [1, 3, 5, 7, 9, 11]
numbers['even_numbers'] = [2, 4, 6, 8, 10, 12]
print(numbers)

symptoms = dict()
symptoms['malaria'] = ['fever', 'high temperature', 'drizziness']
symptoms['typhoid'] = ['running stomach', 'uncontrolled vomitting', 'light-weightedness']
symptoms['pregnancy'] = ['big stomach', 'quick irritation', 'uncontrolled urine excretion', 'vomiting']
symptoms['ebola'] = ['golden urine', 'loss of weight', 'death']

sickness = input("Input your sickness: ")
if sickness == 'malaria':
    print("These are the symptoms you are experiencing: ", symptoms['malaria'])
elif sickness == 'typhoid':
    print("These are the symptoms you are experiencing: ", symptoms['typhoid'])    
elif sickness == 'pregnancy':
    print("Dude, you're just pregnant. Take a hike") 
elif sickness == 'ebola':
    print("Sorry fam, you're gonna be dead in a week!")

