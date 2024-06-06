import processData

def data():
    try:
        paraula = str.lower(input())
        lletra = str.lower(input())
        if " " in paraula:
            print("Escriu-hi només una paraula")
            data()
        else:
            processData.processData(paraula, lletra)

    except:
        print("error")