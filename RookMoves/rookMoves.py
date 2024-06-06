import positionGet


def rookmove():
    columna, fila = positionGet.rookpos()
    try:
        for n in range(1, 9):
            for m in range(1, 9):
                if m == columna and n == fila:
                    print("2", end=" ")
                elif m == columna or n == fila:
                    print("1", end=" ")
                elif (n % 2 == 0 and m % 2 != 0) or (n % 2 != 0 and m % 2 == 0):
                    print("0", end=" ")
                else:
                    print("0", end=" ")
            print("")

    except:
        print("Error")