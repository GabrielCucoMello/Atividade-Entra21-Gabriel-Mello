list = []

for i in range(2000, 2201):
    if(i % 7 == 0 ) and (i % 5 != 0):
        list.append(str(i))

print(','.join(list))