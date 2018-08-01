import random 
ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1


for num in ourList:
    if num < 5:
        print (num)
        belowFive = list()
        belowFive.append(num)

print (belowFive)