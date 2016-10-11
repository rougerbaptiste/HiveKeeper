import os
import pickle


hivesFile = open('hives','r')
hives = hivesFile.read().strip()
hivesFile.close()

hivesList = hives.split(";")


print(hivesList)

entry = 'c'

while entry != 'q':

    entry = input("\nWhat do you want to do ?\nQuit (q), get the list of the hives (h), add a hive (a), remove a hive (r), modify a hive (m) : ").lower()

    if entry == 'h':
        i = 0
        for elt in hivesList:
            hive = elt.split(",")
            print(str(i) + ". Hive "+ hive[0] + " is at " + hive[1])
            i+=1

    if entry == 'a':
        newHiveName = input("What is the name of the new hive ? ")
        newHiveLoc = input("What is the location of the new hive ? ")
        hivesList = hivesList + [newHiveName + "," + newHiveLoc]
        hives = hives + ";" + newHiveName + "," + newHiveLoc

    if entry == 'r':
        deleting = int(input("What is the number of the hive that you want to delete ? "))
        delHive = str(hivesList[deleting])
        hivesList.remove(delHive)

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
