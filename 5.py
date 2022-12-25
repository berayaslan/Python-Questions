def listeIslemi():
    liste = [3,None,2,None,None,1,False,None,10]

    for i in range(len(liste)):
        if liste[i]==None:
            liste[i]=sonEleman
        else:
            sonEleman = liste[i]
    print(liste)

listeIslemi()