import random
import time


def main():
    print("Hi there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    nahodne_cislo = number()
    upravene_nahodne_cislo = list_to_string(nahodne_cislo)
    count = 0
    start_time = time.time()
    while True:
        count += 1
        moje_cislo = get_number()
        vysledok = comparison(moje_cislo, upravene_nahodne_cislo)
        print("Cows:", vysledok[0], "Bulls:", vysledok[1])

        if vysledok[1] == 4:
            total_time = time.time() - start_time
            print(f"Correct, you've guessed the right number in {count} guesses!")
            if count < 7:
                print("That's amazing.")
            else:
                print("That's not so good.")
            print(f"It took you {int(total_time)} seconds to guess the right number.")
            break


def number():
    nahodne_cislo = [random.randint(0, 9) for n in range(4)]
    while nahodne_cislo:
        if len(nahodne_cislo) == len(set(nahodne_cislo)) and nahodne_cislo[0] != 0:
            break
        else:
            nahodne_cislo = [random.randint(0, 9) for n in range(4)]

    return nahodne_cislo


def get_number():
    while True:
        my_number = input("Enter a number " + '\n')
        if len(my_number) == 4 and my_number.isnumeric() \
                and len(my_number) == len(set(my_number)) and my_number[0] != "0":
            break
        else:
            print("You must type 4 unique number digit that does not begin with 0. Try it again.")
    return my_number


def list_to_string(nahodne_cislo):
    str1 = ""
    return str1.join([str(i) for i in nahodne_cislo])


def comparison(moje_cislo, upravene_nahodne_cislo):
    cows, bulls = 0, 0
    for x in range(4):
        if moje_cislo[x] == upravene_nahodne_cislo[x]:
            bulls += 1
        elif moje_cislo[x] in upravene_nahodne_cislo:
            cows += 1
    return cows, bulls


main()
