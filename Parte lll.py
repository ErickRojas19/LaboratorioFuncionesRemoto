def primo(n):
    try:
        cont = 0
        for i in range(1,n+1):
            if n%1==0:
                cont = cont + 1
        if cont == 2:
            print("1")
        else:
            print(0)
    except:
        print("-1")



cont2=0
while True:
    a=int(input("Digite un numero:"))
    if a>0:
        print("Pailas :v")
        break
    else:
        if a<=0:
        cont2 =c ont2 + 1
        n=int(input("Digite otro numero:"))
        print(primo(n))
