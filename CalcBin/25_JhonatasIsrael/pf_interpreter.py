#LAURENTINO,J.I.C.
#12/04/2018
#py version 3.6.3
def interpreter(n):
    #------------------------------------------------------------------
    #sinal
    #------------------------------------------------------------------
    sinal=True
    z=n
    y=n
    numbin=format(n,"08b")
    if n & 0b10000000:
        sinal=False
    else:
        sinal=True

    #---------------------------------------------------------------
    #expoente
    #---------------------------------------------------------------
    shift = n >> 4
    expo = shift & 0b00000111

    #------------------------------------------------------------------
    #mantissa
    #------------------------------------------------------------------

    sig = n & 0b00001111
    sig1=sig & 0b1000
    sig1=sig1>>3
    sig1=sig1*(2**-1)
      
    sig2=sig & 0b0100
    sig2=sig2>>2
    sig2=sig2*(2**-2)

    sig3=sig & 0b0010
    sig3=sig3>>1
    sig3=sig3*(2**-3)
    
    sig4=sig & 0b0001
    sig4=sig4>>0
    sig4=sig4*(2**-4)

    sigf=sig1+sig2+sig3+sig4
    numbin=format(n,"08b")      
    z=z & 0b00001111
    zbin=format(z,"04b")

    #------------------------------------------------------------------
    #impressao
    #------------------------------------------------------------------
    
    if (expo>0 and expo <7):
        expo = expo - 3
        num=(sigf+1.0)*2**expo

        if sinal == True:
            print(numbin+" --> + 1."+zbin+" x 2^"+str(expo)+" --> +"+str(num))
        else:
            print(numbin+" --> - 1."+zbin+" x 2^"+str(expo)+" --> -"+str(num))

    elif (expo==0):
        expo=-2
        num=(sigf+0)*2**expo
        
        if sinal == True:
            print(numbin+" --> + 0."+zbin+" x 2^"+str(expo)+" --> +"+str(num))
        else:
            print(numbin+" --> - 0."+zbin+" x 2^"+str(expo)+" --> -"+str(num))
            
    if y == 0b11111000:
        print(numbin,"--> indetermination")
    elif y == 0b11110000:
        print(numbin, "--> -infinity")
    elif y == 0b01110000:
        print(numbin,"--> +infinity")
    elif y == 0b11111111  or y == 0b11111110 or y ==0b11111101 or y ==0b11111100  or y ==0b11111011 or y ==0b11111010  or y ==0b11111001 or y ==0b11110111  or y ==0b11110110  or y ==0b11110101  or y ==0b11110100 or y ==0b11110011  or y ==0b11110010  or y ==0b11110001 or y==0b01110001 or y == 0b01110010 or y == 0b01110011 or y == 0b01110100 or y == 0b01110101 or y == 0b01110110 or y == 0b01110111 or y == 0b01111000 or y == 0b01111001 or y == 0b01111010 or y == 0b01111011 or y==0b01111100 or y==0b01111101 or y== 0b01111110:
        print(numbin,"--> NAN")
    else:
        return;
