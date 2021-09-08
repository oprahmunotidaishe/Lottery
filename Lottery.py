import random

prediction_of_numbers = 'yes'

while prediction_of_numbers == 'yes':

    if prediction_of_numbers == 'yes':

        answer = input("Would you prefer to "
                       "\nguess the 5 numbers yourself or "
                       "\nhave the computer generate the numbers?"
                       "\n "
                       "\nType g for guess, "
                       "\nType c for computer generated numbers: ")

        print(" ")
        if answer == 'g':

            guess_1 = int(input("Enter your first  guess: "))
            guess_2 = int(input("Enter your second guess: "))
            guess_3 = int(input("Enter your third  guess: "))
            guess_4 = int(input("Enter your fourth guess: "))
            guess_5 = int(input("Enter your fifth  guess: "))

            a = random.randrange(1, 3, 1)
            b = random.randrange(3, 5, 1)
            c = random.randrange(5, 7, 1)
            d = random.randrange(7, 9, 1)
            e = random.randrange(9, 10, 1)

            if guess_1 == guess_2:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_1 == guess_3:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_1 == guess_4:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_1 == guess_5:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_2 == guess_1:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_2 == guess_3:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_2 == guess_4:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_2 == guess_5:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_3 == guess_1:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_3 == guess_2:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_3 == guess_4:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_3 == guess_5:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_4 == guess_1:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_4 == guess_2:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_4 == guess_3:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_4 == guess_5:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_5 == guess_1:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_5 == guess_2:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_5 == guess_3:
                print(" ")
                print("No duplication of a number is allowed")
            elif guess_5 == guess_4:
                print(" ")
                print("No duplication of a number is allowed")

            else:

                if (guess_1 == a) and \
                        (guess_2 == b) and \
                        (guess_3 == c) and \
                        (guess_4 == d) and \
                        (guess_5 == e):
                    print(" ")
                    print("You have won the gold prize, "
                          "\nyou got all 5 numbers correctly.")
                    print(" ")
                    print("The secret numbers in the "
                          "\nsealed envelope are: "
                          "\n", a, " ", b, " ", c, " ", d, " ", e, " ")
                else:
                    print(" ")
                    print("The secret numbers in the "
                          "\nsealed envelope were: "
                          "\n", a, " ", b, " ", c, " ", d, " ", e, " ")
                    print(" ")
                    print("Oops!! Almost got it. "
                          "\nDo you want to go again ?")
        elif answer == 'c':
            deck = list(range(1, 10))

            a = random.randrange(1, 3, 1)
            b = random.randrange(3, 5, 1)
            c = random.randrange(5, 7, 1)
            d = random.randrange(7, 9, 1)
            e = random.randrange(9, 10, 1)

            hand = random.sample(deck, k=5)
            print("The computer generated numbers are: "
                  "\n", hand)
            print(" ")

            if a == hand[0] and b == hand[1] and \
                    c == hand[2] and d == hand[3] and e == hand[4]:
                print("You have won the gold prize, "
                      "\nyou got all 5 numbers correctly.")
                print(" ")
                print("The secret numbers in the "
                      "\nsealed envelope are: "
                      "\n", a, " ", b, " ", c, " ", d, " ", e, " ")
            else:
                print("The secret numbers in the "
                      "\nsealed envelope were: "
                      "\n", a, " ", b, " ", c, " ", d, " ", e, " ")
                print(" ")
                print("Oops!! Almost got it. "
                      "\nDo you want to go again ?")

        else:
            if answer != 'g' or answer != 'c':
                print("Please input either "
                      "\ng to guess the 5 numbers yourself or "
                      "\nc to have the computer generated numbers.")

    prediction_of_numbers = input("\nDo you want to play again? "
                                  "\nPress yes for Yes, \nPress no for No: ")
    print(" ")
else:
    if prediction_of_numbers != 'yes' or 'no':
        print("Your input was:", prediction_of_numbers, ". "
              "\nPlease input either, "
              "\nyes for Yes or"
              "\nno for No.")
        print(" ")
    prediction_of_numbers = 'yes'

print("End of program.")
