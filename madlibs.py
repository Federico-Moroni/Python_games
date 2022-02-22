def madlibs():

    print("Welcome to Madlibs! Get ready to play!", "\n")

    adj = input("Adjective: ")
    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous = input("Famous Person: ")

    madlib = f"Skydiving is so {adj}! I love trying new stuff everyday because I love to {verb1}. Sometimes, when I'm planning other activities to do, I {verb2} like if I were {famous}!"

    print("\n", madlib, "\n")

    play_again = (
        input("Do you want to play again? Please answer YES or NO: ")).lower()

    if play_again == "yes":
        print("Lets play another one!")
        madlibs()
    else:
        print("Thanks for playing")


madlibs()
