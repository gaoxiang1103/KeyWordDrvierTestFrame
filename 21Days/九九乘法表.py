j = 0
while j < 9:
    j += 1
    i = 0
    while i < 9:
        i += 1
        print(i, "*", j, "=", (i * j), sep="", end="\t")
        if i == j:
            break
    print()

# j = 0
# while j <9:
#     j+=1
#     i=0
#     while i<j:
#         i +=1
#         print(i, '*', j, '=', (i*j), end = "   ")
#     print()

