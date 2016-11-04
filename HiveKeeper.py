import os
import hkfunctions

hiveList = []
for (dirpath, dirnames, filenames) in os.walk("./Hives"):
    hiveList.extend(filenames)

entry = ""

while entry != "q":
    entry = input("\n==========\nWhat do you want to do ? (Quit : q, Help : h) : ").lower()
    
    if entry == "h":
        print("Quit (q)\nGet this help (h)\nList the hives (l)\nAdd a hive (a)\nModify a hive (m)\n or get infos on a hive (i)")
        
    if entry == "l":
        hkfunctions.hk_list()
    
    if entry == "i":
        index = int(input("What is the number of the hive you want to get infos of ? "))
        hiveName = hiveList[index]
        hkfunctions.hk_infos(hiveName)
    if entry == "a":
        hkfunctions.hk_newHive()
        hiveList = hkfunctions.hk_lstRefresh()
    if entry == "m":
        index = int(input("What is the number of the hive that you want to modify ? "))
        hiveName = hiveList[index]
        action = int(input("What do you want to modify in this hive : Location (1), Daughter (2)"))
        if action == 1:
            hkfunctions.hk_locationModif(hiveName)
        if action == 2:
            hkfunctions.hk_daughterModif(hiveName)