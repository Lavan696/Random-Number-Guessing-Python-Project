from random import randrange
print("Hello. Welcome to the game of guessing Random number")
print("Enter the range for guessing:(start,end) ")
start = int(input("Enter start: "))
end = int(input("Enter end: "))
if(end <= start):
    print(f"Your number is not greater than {start}")
    print("Please restart the game")
else:
    try:
        user_input = int(input("Enter number:"))
    except Exception as ValueError:
        print("Invalid Input.Please restart the game.")
    else:
        random_number = randrange(start,end)  #You can also specify step here
        attempt = 1
        while True:

            if(user_input == random_number):
                print(f"Congratulations. You won in attempt {attempt}.")
                break
            elif(user_input < random_number):
                print("Sorry. Your number is too small.")
            else:
                print("Sorry. Your number is too high.")
            try:
                user_input = int(input("Enter again."))
                attempt +=1
            except Exception as ValueError:
                print("Invalid Input.Please restart the game.")
                break
print("******Thank You******")
