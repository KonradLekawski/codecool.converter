import csv
flag = True
dictionary_file = open('dictionary.CSV','r')
dictionary = {}
reader = csv.reader(dictionary_file)
for arg in reader:
    dictionary[arg[0]] = arg[1],arg[2]
dictionary_file.close()

print("Dictionary for a little programmer  :")
print("")
while flag:
    choosen_number = input("1) search for explanation by apellation \n2) add new definition \n3) show all apellations alphabetically \n0) exit\n")
    if choosen_number == "1":
        appellation = input("enter name of appellation:  ")
        if appellation in dictionary:
            appellation_value = dictionary.get(appellation)
            appellation_value = tuple(appellation_value)
            print(appellation_value[0])
            print("source:")
            print(appellation_value[1])
        else:
            print("there in no appellation like %s in dictionary" %appellation)
    elif choosen_number == "2":
        new_appellation = input("enter new appellation: ")
        new_definition = input("enter new definition: ")
        new_source = input("enter new source: ")
        dictionary[new_appellation] = new_definition , new_source
        dictionary_file = open('dictionary.CSV','w')
        writer = csv.writer(dictionary_file)
        for key, value in dictionary.items():
            writer.writerow([key, value[0],value[1]])
        dictionary_file.close()
    elif choosen_number == "3":
        for key, value in sorted(dictionary.items()):
            print (key)
    elif choosen_number == "0":
        exit()
    else:
        print("invalid input")
