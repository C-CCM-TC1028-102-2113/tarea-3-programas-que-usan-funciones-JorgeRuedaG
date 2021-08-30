
def main():
    pli=int(input("Dame la cantidad de pliegos de papel albanene:"))
    plu=int(input("Dame la cantidad de plumones:"))
    a=pli*12
    b=plu*35
    if a>=b:
        print("El número máximo de tarjetas que se pueden hacer es:" + str(b))
    else:
        print("El número máximo de tarjetas que se pueden hacer es:" + str(a))

   
    pass

if __name__=='__main__':
    main()
