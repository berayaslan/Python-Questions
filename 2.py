def fibonacciSayilariBulma():

    fibonacciSayilari=[]
    diziToplam=0

    n1 = 0
    n2 = 1
    toplam =0

    while n1<=4_000_000:
        fibonacciSayilari.append(n1)
        if(n1%2==0):
            toplam =toplam + n1
        nth = n1 + n2
        n1 = n2
        n2 = nth
    #print(fibonacciSayilari) Sayıları ekrana yazdırıp görmek için


    for i in range(len(fibonacciSayilari)):
        if fibonacciSayilari[i] %2==0:
            diziToplam=diziToplam+fibonacciSayilari[i]
        else:
            continue
    print("Toplam= ",diziToplam)

fibonacciSayilariBulma()