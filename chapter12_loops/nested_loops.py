nested = [['mike', 12], ['jan', 15], ['alice', 8]]
for lst in nested:
    print(f'List = {lst}')
    for item in lst:
        print(f'Item -> {item}')