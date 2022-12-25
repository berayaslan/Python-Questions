def saymaSayilari():

    karakter=(",.!?:;")
    elemanToplam=0
    ortalama=0

    dizi=("Elma Portakal Armut")
    yeni = dizi.split(" ")

    for i in range(len(yeni)):
        if yeni[i]==karakter:
            pass
        else:
            elemanToplam+=int(len(yeni[i]))

    ortalama=elemanToplam/len(yeni)
    str(ortalama)
    print("avg_len{} -> {:.2f}".format(yeni,ortalama))

saymaSayilari()