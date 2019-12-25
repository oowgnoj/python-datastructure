import collections

c = collections.Counter('abcabc')
print(c)

d = collections.Counter({'red': 4, 'blue': 2})

print(d)
# def compareAtoB(a, b):
#     splitedA = list(str(a))
#     splitedB = list(str(b))

#     for i in range(0, min(len(splitedA), len(splitedB))):
#         if(int(splitedA[i]) != int(splitedB[i])):
#             return print(a) if (int(splitedA[i]) > int(splitedB[i])) else print(b)
#         continue


# compareAtoB(11, 12)
