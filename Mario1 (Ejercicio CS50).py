from csv import excel


def main():
    largo=get_large()
    for i in range(largo):
        print("?",  end="")

def get_large():
    while True:
        try:
            n=int(input("Inserte Numero :"))
            if n > 0:
                break
        except ValueError:
            print("No es un numero")
    return n
main()

for i in range(3):
    print("#"*3)