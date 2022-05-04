import csv
people ={
    "Carter" : "+123456",
    "David"  : "+8791465"
}
name = input("Nombre : ")
if name in people:
    print(f"Number: {people[name]}")

