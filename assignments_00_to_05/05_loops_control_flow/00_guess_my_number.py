
import random

def main():
    secret_number = random.randint(0, 99)  
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))  
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break  
        except ValueError:
            print("Please enter a valid number!")  


if __name__ == '__main__':
    main()