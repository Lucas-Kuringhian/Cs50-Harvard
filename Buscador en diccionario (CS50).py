import sys 

numbers = [4,6,8,0,2,5,7]

if 0 in numbers:
    print("Found")
    sys.exit(0)
print("Not Found")
sys.exit(1)