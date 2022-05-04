def main():
    height=get_height()
    for i in range(height):
        print("#")
def get_height():
    while True:
        try:
            n=int(input("Cantidad : "))
            if n > 0:
                break
        except ValueError:
                    print("No es un numero")
    return n

main()