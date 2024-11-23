def evenorodd(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

def main():
    number = int(input("enter a number:"))
    evenorodd(number)

main()