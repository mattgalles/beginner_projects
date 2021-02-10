

def main():
    userInput = 0
    while userInput < 1 or userInput > 1000:
        userInput = int(input("Please pick a number between 1 and 1000: "))
        if userInput < 1 or userInput > 1000:
            print('The number is not between 1 and 1000. Please pick another number.')

    if userInput % 2 == 0:
        print(f'{userInput} is an even number.')
    else:
        print(f'{userInput} is an odd number.')

if __name__ == "__main__":
    main()
