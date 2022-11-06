def des(non_negative):
    lis = list(str(non_negative))
    lis.sort()
    desorder = ""
    for i in range(-1, -len(lis)-1, -1):
        desorder +=lis[i]
    return int(desorder)

love = des(12343)
print(love)