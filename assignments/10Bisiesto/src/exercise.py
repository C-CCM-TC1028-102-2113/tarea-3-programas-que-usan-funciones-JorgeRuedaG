
def main():
    #escribe tu código abajo de esta línea
    año=int(input("Dame un año:"))
    if año % 4 == 0 and año % 100 != 0:
        print("true")
    elif año % 4 == 0 and año % 100 == 0:
        if año % 400 == 0:
            print("true")
        else:
            print("false")
    else:
        print("false")
    pass

if __name__=='__main__':
    main()
