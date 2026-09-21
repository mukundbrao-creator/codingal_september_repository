L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original list:", L)

count = 0 

for i in L:
    count += i

avg = count/len(L)

print("sum: ", count)
print("average: ", avg)

L.sort()

print("The smallest element is: ", L[0])

print("The largest eleement is: ", L[-1])