my_list = [1, 2, 3]
for number in my_list:
    if number == 4:
        print('Found number 4!')
        break
    print(number)
else:
    print('Number 4 not found')