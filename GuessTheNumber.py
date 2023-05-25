# User is supposed to guess pseudo-randomly generated number.

from random import randint
from sys import exit

def run():
    randomNumber = randint(1,1000)
    attempts = 0

    print("\nLiczba została wylosowana, czas rozpocząć grę!\n")

    while True:
        user_input = input("Zgadnij liczbę (lub wciśnij 'q' aby zakończyć grę): ")

        if (user_input.lower() == 'q'):
            exit("Program został zakończony.")

        try:
            guess = int(user_input)
        except:
            print("Wprowadź poprawną liczbę.")
            continue

        if (guess < 1 or guess > 1000):
            print("Podana Liczba znajduje się poza przedziałem (1-1000)")
            continue

        attempts += 1

        if guess < randomNumber:
            print("Podana liczba jest za mała!")
            continue
        if guess > randomNumber:
            print("Podana liczba jest za duża!")
            continue
        else:
            print(f"Gratulacje! Odgadłeś prawidłową liczbę w {attempts} próbach.")
            break

run()
input("Press Enter to continue...")