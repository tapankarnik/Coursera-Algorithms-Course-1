def bifurcate(num,n):
    return num[:-n],num[-n:]

def karatsuba(x,y):
    if(int(x)<10 or int(y)<10):
        return str(int(x)*int(y))
    n = max(len(x),len(y))

    a,b = bifurcate(x,n//2)
    c,d = bifurcate(y,n//2)


    ac = karatsuba(a,c)
    
    bd = karatsuba(b,d)
 

    adplusbc = karatsuba(str(int(a)+int(b)),str(int(c)+int(d)))
    adplusbc = str(int(adplusbc) - int(ac) - int(bd))  #Gauss' Trick

    xy = str((int(ac)*(10**(2*(n//2))) + ((10**(n//2))*int(adplusbc)) + int(bd)))
    return xy

if __name__ == '__main__':
    x = '5678'
    y = '1234'
    print(karatsuba(x,y))
