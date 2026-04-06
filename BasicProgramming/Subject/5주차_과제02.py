i, j, k = 0, 0, ''
for i in range(2, 10) :
    k += ("#  %d단  # " % i)
print(k)
for i in range(9, 0, -1) :
    k = ""
    for j in range(9, 1, -1) :
        k += str("%d X %d =%2d " % (j, i, j*i))
    print(k)
