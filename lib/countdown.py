# your code goes here!

from time import sleep

# Write a function countdown() that takes in an integer argument and uses a while loop to countdown from that integer to 1, outputting f'{number} SECOND(S)!' in each iteration of the loop. The function should print() "HAPPY NEW YEAR!" after the loop finishes:
def countdown(number):
    while number:
        print(f'{number} SECOND(S)!')
        number -= 1
    print('HAPPY NEW YEAR!')

# Our Python program executes so quickly that it doesn't actually count down at the speed of one second per number. Write a second function called countdown_with_sleep() that also takes one integer argument for the countdown and makes the loop pause for one second each trip around.
def countdown_with_sleep(number):

    while number:
        print(f'{number} SECOND(S)!')
        number -= 1
        sleep(1)

    print('HAPPY NEW YEAR!')