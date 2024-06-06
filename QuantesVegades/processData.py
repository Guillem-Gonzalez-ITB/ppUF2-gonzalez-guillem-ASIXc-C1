import getData
import printData


def processData(paraula, lletra):
    try:
        llista = []
        for n in range(len(paraula)):
            if lletra == paraula[n]:
                llista.append(lletra)
        printData.printdata(lletra, paraula, llista)
    except:
        print("error")