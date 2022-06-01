lt = [[10, 20, 30], [15, 1, 2], [50, 3, 5], [45,12,7], [100,200,300]]

ltm = [ x for x in lt if sum(x)> 50]

print(lt)
print(ltm)