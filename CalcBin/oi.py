n = input("digite um número binario para saber o se o valor está positivo ou negativo em binario (8 bits)")
print(n)
binario= bin(n)
print(binario)
print(decimal)
sinal=True

#sinal________________________________________
if decimal & 10000000:
    print("negativo")
    print(n)
    sinal=False
else:
    #bin & 0b000000000:
    print("positivo")
    print(n)
    sinal=True

#expoente
print(decimal)
binario=int(decimal,2)
print(binario)
shift = binario >> 4
print("Shift",shift)
#a variavel pega o expoente e compara com 0b00000111 onde quando o numero só 1 quando os dois forem 1.
#expo = shift & 0b00000111
#soma o excesso
#expo = expo + 3
#print("expoente: ", expo)
#sig = n & 0b00001111

sig1=sig & 0b1000
print(sig1)
sig1=sig1>>3
print(sig1)
sig1=sig1*(2**-1)
print(sig1)
  
sig2=sig & 0b0100
#print(sig2)
sig2=sig2>>2
#print(sig2)
sig2=sig2*(2**-2)
#print(sig2)

sig3=sig & 0b0010
#print(sig3)
sig3=sig3>>1
#print(sig3)
sig3=sig3*(2**-3)
#print(sig3)

sig4=sig & 0b0001
#print(sig4)
sig4=sig4>>0
#print(sig4)
sig4=sig4*(2**-4)
#print(sig4)




print(sinal)
