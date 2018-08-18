#Laurentino, J.I.C.
#CALCbin
opcao=int(input("Digite a opção para ser realizada"
                "\n (1) Conversor"
                "\n (2) Calculadora "
                "\n (3)varrer bits"))
if opcao==1:
    n=int(input("Digite o codigo para saber em qual base o numero esta sendo inserido:"
                "\n(2)  Binaria"
                "\n(8)  Octal"
                "\n(10) Decimal"
                "\n(16) Hexadecimal"))
    m=int(input("Digite o codigo para saber para qual base o numero vai ser convertido:"
                "\n(2)  Binaria"
                "\n(8)  Octal"
                "\n(10) Decimal"
                "\n(16) Hexadecimal"))
    if ((n==2) and (m==2)) or ((n==8) and (m==8)) or ((n==10) and (m==10)) or  ((n==16) and (m==16)):
        print("A base do numero inserido tem que ser de uma base diferente da do numero que vai ser convertido!!!")
    elif(n==2) and (m==8):#de binario para octal
        x=int(input("Digite o numero para ser convertido"))
        print(oct(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==2) and (m==10):#de binario para decimal
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==2) and (m==16):#de binario para hexadecimal
        x=int(input("Digite o numero para ser convertido"))
        print(hex(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==8) and (m==10):#de octal para decimal
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==8) and (m==2):#de octal para binario
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==8) and (m==16):#de octal para hexadecimal
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==10) and (m==2):#de decimal para binario
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==10) and (m==8):#de decimal para octal
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==10) and (m==16):#de decimal para hexadecimal
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==16) and (m==10):#de hexadecimal para decimal
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==16) and (m==2):#de hexadecimal para binario
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    elif(n==16) and (m==8):#de hexadecimal para octal
        x=int(input("Digite o numero para ser convertido"))
        #if(x<=1) and (x>=0):
        print(int(x))
        #else:
            #print("o numero inserido não é octal!!")
    else:
        print("Os valores das bases digitados não estão inseridos no banco de dados")
elif opcao==2:
    n = int(input("Digite o codigo para saber em qual base o numero esta sendo inserido:"
                  "\n(2)  Binaria"
                  "\n(8)  Octal"
                  "\n(10) Decimal"
                  "\n(16) Hexadecimal \n "))
    a=int(input("Digite o primeiro valor: "))
    b=int(input("Digite o segundo valor: "))
    print("\n escolha uma das opções para fazer o calculo")
    x = int(input("(1) SOMA \n (2) SUBTRAÇÃO \n (3) DIVISÃO \n (4) MULTIPLICAÇÃO"))
    if(x==1):#SOMA
        if(n==2):
            abin=bin(a)
            bbin=bin(b)
            list(str(abin))
            list(str(bbin))
            soma=bin(a+b)
            print(abin)
            print(bbin)
            print(soma)
        elif(n==8):
            aoct = oct(a)
            boct = oct(b)
            list(str(aoct))
            list(str(boct))
            soma = oct(a + b)
            print(aoct)
            print(boct)
            print(soma)
        elif (n==10):
            adec = int(a)
            bdec = int(b)
            soma=int(a+b)
            print(adec)
            print(bdec)
            print(soma)
        elif (n == 16):
            ahex = hex(a)
            bhex = hex(b)
            soma = hex(a + b)
            print(ahex)
            print(bhex)
            print(soma)
        else:
            print("Digite um dos valores citados em cima!!")
    if(x==2):#subtração
        if (n == 2):
            abin = bin(a)
            bbin = bin(b)
            list(str(abin))
            list(str(bbin))
            sub = bin(a - b)
            print(abin)
            print(bbin)
            print(sub)
        elif (n == 8):
            aoct = oct(a)
            boct = oct(b)
            list(str(aoct))
            list(str(boct))
            sub = oct(a - b)
            print(aoct)
            print(boct)
            print(sub)
        elif (n == 10):
            adec = int(a)
            bdec = int(b)
            sub = oct(a - b)
            print(adec)
            print(bdec)
            print(sub)
        elif (n == 16):
            ahex = hex(a)
            bhex = hex(b)
            list(str(ahex))
            list(str(bhex))
            sub = oct(a - b)
            print(ahex)
            print(bhex)
            print(sub)
        else:
            print("Digite um dos valores citados em cima!!")
    if (x == 3):  # subtração
        if(n == 2):
            abin = bin(a)
            bbin = bin(b)
            sub = bin(a - b)
        elif (n == 8):
            aoct = oct(a)
            boct = oct(b)
            sub = oct(a - b)
        elif (n == 10):
            adec = int(a)
            bdec = int(b)
            sub = (a - b)
        elif (n == 16):
            ahex = hex(a)
            bhex = hex(b)
            sub = hex(a - b)
        else:
            print("Digite um dos valores citados em cima!!")
    if (x == 4):  # divisão
        if(n == 2):
            abin = bin(a)
            bbin = bin(b)
            list(str(abin))
            list(str(bbin))
            div = bin(a/b)
            print(abin)
            print(bbin)
            print(div)
        elif (n == 8):
            aoct = oct(a)
            boct = oct(b)
            list(str(aoct))
            list(str(boct))
            div = oct(a/b)
            print(aoct)
            print(boct)
            print(div)
        elif (n == 10):
            adec = int(a)
            bdec = int(b)
            div = oct(a/b)
            print(adec)
            print(bdec)
            print(div)
        elif (n == 16):
            ahex = hex(a)
            bhex = hex(b)
            list(str(ahex))
            list(str(bhex))
            div = oct(a/b)
            print(ahex)
            print(bhex)
            print(div)
        else:
            print("Digite um dos valores citados em cima!!")
elif opcao == 3:
    #1-3-4
    n=input("digite um número binario para saber o se o valor está positivo ou negativo em binario (8 bits)")
    n=int(n,2)
    sinal=0
    if n & 0b100000000:
        print("negativo")
        print(n)
        sinal=1
    else:
        #bin & 0b000000000:
        print("positivo")
        print(n)
        sinal=0
    shift=n>>4
    expo=shift & 0b00000111
    expo=expo+3
    print("expoente",expo)
    sig=n & 0b00001111
    print("mantissa",sig)

    #a= n & 0b0000111
