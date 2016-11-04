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

def hk_lstRefresh():
    """ Function that refreshes the list of the hives stored in the folder
    """
    hiveList = []
    for (dirpath, dirnames, filenames) in os.walk("./Hives"):
        hiveList.extend(filenames)
    
    return hiveList

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
    hive.write("\n".join(["*"+loc, "$"+mother, "%"+daughter]))
    print("\n".join([loc, mother, daughter]))
    hive.close()
    
    hive = open("./Hives/"+mother, "r")
    hiveMother = hive.readlines()
    hive.close()
    
    hiveMother[2] = ",".join([hiveMother[2], newName])+"\n"
    hive = open("./Hives/"+mother, "w")
    print("".join(hiveMother))
    hive.write("".join(hiveMother))
    hive.close()

def hk_locationModif(hiveName):
    """ Function that modifies the location of a specified hive
    """
    fileFlux = open("./Hives/"+hiveName, "r")
    hiveInfos = fileFlux.readlines()
    fileFlux.close()
    newLoc = input("What is the new location of the hive ? ")
    hiveInfos[0] = "*"+newLoc + "\n"
    
    fileFlux = open("./Hives/"+hiveName, "w")
    fileFlux.write("".join(hiveInfos))
    fileFlux.close()
    
def hk_daughterModif(hiveName):
    """ Fucntion that modifies the list of daughters of a specified hive
    """
    fileFlux = open("./Hives/"+hiveName, "r")
    hiveInfos = fileFlux.readlines()
    fileFlux.close()
    action = int(input("Do you want to modify the name of a daughter (1) or add a daughter (2) ? "))
    if action == 1:
        action
    
    
    
    