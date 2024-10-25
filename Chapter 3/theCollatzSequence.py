#Collatz Sequence Program

def collatz(number):
    if number % 2 == 0: #check if number is even
        result = number // 2
    else:
        result = 3 * number + 1 
    print(result)
    return result

# Main program that runs the Collatz sequence
def main():
    try:
        number = int(input("Enter number: "))
        while number != 1:
            number = collatz(number)
    except ValueError:
        print("Please enter a valid integer.")
        
# Start the program
main()