my_dict = {
    'tuple': (1, 2, 3, None, False, 'last'),
    'list': [1, 2, [3, 4], (5, 6), {'one': 1}],
    'dict': {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5},
    'set': {'a', 'b', 'c', 'd', 'e'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(True)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = (1, 2)
my_dict['dict'].pop('may')

my_dict['set'].add('f')
my_dict['set'].remove('a')

print(my_dict)
