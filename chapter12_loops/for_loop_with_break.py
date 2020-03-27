list_of_tuples = [(1, 'banana'), (2, 'apple'), (3, 'pear')]
for number, fruit in list_of_tuples:
    if fruit == 'apple':
        print('Apple found!')
        break
    print(f'{number} - {fruit}')