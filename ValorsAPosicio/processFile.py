import datafile


def showValuesForEachPosition():
    try:
        for item in range(len(datafile.enters)):
            print("Position", item, ":", datafile.enters[item])

    except:
        print("Error")