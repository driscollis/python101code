# a simple while loop
i = 0
while i < 10:
    print(i)
    i = i + 1
  
# this is how to break out of a loop
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
    
# an example of break and continue
i = 0
while i < 10:
    if i == 3:
        i += 1
        continue
    
    print(i) 
    
    if i == 5:
        break
    i += 1