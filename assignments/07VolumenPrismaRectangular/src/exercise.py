
def main():
    #escribe tu código abajo de esta línea
    base=float(input("Dame la base:"))
    alt=float(input("Dame la altura:"))
    area=base*alt
    prof=float(input("Dame la profundidad:"))
    vol=area*prof
    print("el volumen es:" + str(vol))
    
    pass

if __name__=='__main__':
    main()
