import os
import pickle


with open('hives','rb') as fichier:
    depickler = pickle.Unpickler(fichier)
    hives = depickler.load()


with open('hivesdata','rb') as fichier:
    depickler = pickle.Unpickler(fichier)
    hivesdata = depickler.load()

hives = "A1,loc1;A2,loc2"
hivesdata = [["A1", "loc1", "none", [ ]], [ "A2", "loc2", "A1", [ ] ] ]



hivesList = hives.split(";")


print(hivesdata)

entry = 'c'

while entry != 'q':

    entry = input("\n==========\nWhat do you want to do ?\nQuit (q), get the list of the hives (h), add a hive (a), remove a hive (r), modify a hive (m), get infos on a hive (i) : ").lower()

    if entry == 'h':
        i = 0
        for elt in hivesList:
            hive = elt.split(",")
            print(str(i) + ". Hive "+ hive[0] + " is at " + hive[1])
            i+=1

    if entry == 'i':
        infos = int(input("What is the number of the hive you want to get infos about ? "))
        print(infos)
        hiveinfos = hivesdata[infos]
        print("The hive " + hiveinfos[0] + " is in " + hiveinfos[1]+".")
        print("Its parent is " + hiveinfos[2] + ".")
        #print("Remarks on this hive :\n" + hiveinfos[3])

    if entry == 'a':
        newHiveName = str(input("What is the name of the new hive ? "))
        newHiveLoc = str(input("What is the location of the new hive ? "))
        newHiveHered = str(input("What is the parent of the new hive ? "))
        hivesList = hivesList + [newHiveName + "," + newHiveLoc]
        print(hivesdata)
        hiveinfos = [newHiveName, newHiveLoc, newHiveHered,[]]
        print(hiveinfos)
        hivesdata = hivesdata.append(hiveinfos )
        print(hivesdata)
        hives = hives + ";" + newHiveName + "," + newHiveLoc

    if entry == 'r':
        deleting = int(input("What is the number of the hive that you want to delete ? "))
        delHive = str(hivesList[deleting])
        hivesList.remove(delHive)
        hivesdata.remove(delHive)

    if entry == 'm':
        modifying = int(input("What is the number of the hive that you want to modify ? "))
        modif = input("What do you want to modify ? name (n), location (l) ")

        if modif == 'n':
            hive = hivesList[modifying].split(",")
            newName = input("What is the new name of the hive ? ")
            hivesList[modifying] = newName + "," + hive[1]

        if modif == 'l':
            hive = hivesList[modifying].split(",")
            newLoc = input("What is the new location of the hive ? ")
            hivesList[modifying] = hive[0] + "," + newLoc

# Here we take note of all the changes
hives = ""
for elt in hivesList:
    if len(hives) == 0:
        hives = str(elt)
    else:
        hives = hives + ";" + str(elt)

hivesFile = open('hives','w')
hivesFile.write(hives)
hivesFile.close()

with open('hives','wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(hives)

with open('hivesdata','wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(hivesdata)

