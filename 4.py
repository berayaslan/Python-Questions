def asalSayiHesaplama(x):
    asallar = [2]
    test = 3
    while len(asallar) < x:
        kontrol_limit = int(test/2)
        asal_bulduk = True
        for asal in asallar:
            if asal > kontrol_limit:
                break
            if test % asal == 0:
                asal_bulduk = False
                break
        if asal_bulduk:
            asallar.append(test)
        test += 2
    print(asallar[x-1]) 

asalSayiHesaplama(10001)