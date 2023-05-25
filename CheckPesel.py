# Sprawdzenie czy podany ciąg znaków jest prawidłowym peselem.

from sys import exit


def run():
    user_input = input("\nWciśnięcie przycisku \"Q\" spowoduje zamknięcie programu.\n"
                       "Wprowadź numer PESEL by sprawdzić jego poprawność:\n")

    while (user_input.lower() != 'q'):
        try:
            pNum = [int(x) for x in str(user_input)]
        except:
            print("We wprowadzonym numerze PESEL znajdują się nie prawidłowe znaki.")
            return

        if (len(pNum) < 11):
            print("Wprowadzony PESEL jest za krótki.")
            return
        elif (len(pNum) > 11):
            print("Wprowadzony PESEL jest za długi.")
            return

        isPeselCorrect = (
                pNum[0] * 1 + pNum[1] * 3 + pNum[2] * 7 + pNum[3] * 9 + pNum[4] * 1 + pNum[5] * 3 + pNum[6] * 7 +
                pNum[7] * 9 +
                pNum[8] * 1 + pNum[9] * 3 + pNum[10] * 1)

        if (isPeselCorrect):
            return print("Wprowadzony numer PESEL jest poprawny.")

    exit("Program został zakończony.")


if __name__ == '__main__':
    run()
    input("Press Enter to continue...")