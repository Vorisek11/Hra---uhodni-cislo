import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python hra, uhodni cislo")
print(f"vyber cislo mezi {lowest_num} a {highest_num}")

while is_running:

    guess = input("vypis cislo: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("cislo neni mezi vyberem")
        elif guess < answer:
            print("cislo je vyzsi!!")
        elif guess > answer:
            print("cislo je nizsi!!")
        else:
            print(f"--------------------------")
            print(f"SPRAVNE! cislo je {answer}")
            print(f"pocet pokusu: {guesses}")
            print(f"--------------------------")
            is_running = False

    else:
        print("TOTO NENI CISLO")
