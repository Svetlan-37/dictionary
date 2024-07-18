# dict
my_coworkers = {'Elena': 1968, 'Julia': 1984, 'Olga': 1983, "Tanya": 2002}
print(my_coworkers)
print(my_coworkers.get('Olga'))
print(my_coworkers.get('Mariya'))
my_coworkers.update({'Anna': 1987, 'Nadya': 1984})
print(my_coworkers)
a = my_coworkers.pop('Tanya')
print(a)
print(my_coworkers)
# set
a = {1, 'tomato', (1, 1.5, 2), 1, 2, 1.5, 'orange', 'tomato'}
print(set(a))
print(a.remove(1))
print(a.add(11))
print(a.add('peach'))
print(a)
