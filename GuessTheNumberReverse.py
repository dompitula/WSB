# Computer is supposed to guess user's number.

from random import randint
from sys import exit

def run():
    min_num = 0
    max_num = 1000
    attempts = 0

    while attempts < 15:
        guessedNumber = randint(min_num, max_num)
        user_answer = input(f"Czy liczba {guessedNumber} jest poprawna? (mniej, więcej, tak) ")

        if user_answer.lower() == 'tak':
            print(f"Udało się! Zgadłem liczbę {guessedNumber} w {attempts} próbach.")
            break
        elif user_answer.lower() == 'mniej':
            max_num = guessedNumber - 1
            attempts += 1
        elif user_answer.lower() == 'więcej':
            min_num = guessedNumber + 1
            attempts += 1
        elif (user_answer.lower() == 'q'):
            exit("Program został zakończony.")
        else:
            print("Nieprawidłowa odpowiedź. Odpowiedz 'mniej', 'więcej', lub 'tak'.")

        if attempts == 15:
            print("Nie udało mi się odgadnąć twojej liczby w 15 próbach.")
            break

run()
input("Press Enter to continue...")