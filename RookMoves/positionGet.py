

def rookpos():
    try:
        columna, fila = str.split(input())
        fila = int(fila)
        columna = int(columna)
        return columna, fila
    except:
        print("prova amb 2 nombres")
        return rookpos()
