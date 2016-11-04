import os

def hk_list():
    """
    Function that list the hives stored in the folder
    """
    hiveList = []
    for (dirpath, dirnames, filenames) in os.walk("./Hives"):
        hiveList.extend(filenames)
    i = 0
    print("  ")
    for elt in hiveList:
        hive = elt.split(",")
        print(str(i) + ". Hive " + hive[0])
        i += 1

def hk_infos(hivename):
    """ Function that returns the infos of a hive
    """
    hive = open("./Hives/"+hivename,"r")
    print("  ")
    print("Hive " + hivename + " : ")
    for ligne in hive:
        ligne = ligne.rstrip()
        if ligne[0] == "*":
            print("location : " + ligne.split("*")[1])
        if ligne[0] == "$":
            print("mother : " + ligne.split("$")[1])
        if ligne[0] == "%":
            print("daughter : " + ligne.split("%")[1])
    hive.close()

def hk_newHive():
    """ Function that creates a new hive
    """
    newName = input("What is the name of the new hive ? ")
    hive = open("./Hives/"+newName, "w")
    loc = input("What is the location of the new hive ? ")
    mother = input("What is the name of the mother of this hive ? (If none, write none) ")
    daughter = input("What is the name of the daughter of this hive ? (If none, write none) ")
    hive.write("\n".join([loc, mother, daughter]))