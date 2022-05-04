import csv
file = open("phonebook.csv","a") #significa formato apendice
name = input("Nombre : ")
numero= int(input("Numero : "))

writer = csv.writer(file)
writer.writerow([name,numero])
file.close()