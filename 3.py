def palindrom():

    palindrom = []

    for i in range(100,1000):
        for j in range(100,1000):
            if str(i*j)== str(i*j)[::-1]:
                palindrom.append(i*j)
    print(max(palindrom))
    
palindrom()