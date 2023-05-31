# This program will count every number "2" in a list that consists of numbers from 1 to user input

while True:
    numList = []
    count = 0

    try:
        userNumber = int(input("Wprowadź liczbę: "))
        if (userNumber < 1):
            print("Podaj liczbę większą od 0.")
            continue
        for number in range(userNumber):
            numList = [int(dig) for dig in str(number)]

            for digit in numList:
                if digit == 2:
                    count += 1
        break
    except ValueError:
        print("Podana liczba jest nieprawidłowa, spróbuj jeszcze raz.")

print(f"W ciągu liczb od 1 do {userNumber} cyfra '2' została użyta {count} razy.")