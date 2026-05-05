def welcome_screen():
    print("""
Welcome to Fantasy Rush!

What is your name?
          """)

    name = input(": ")

    print("""
Great! And for nothing of importance, what is your favourite animal?
          """)

    animal = input(": ")

    print(
        f"""
OH NO! Your most favourite pet {animal} has fallen ill! The only cure is the reward for winning the kingdom's arena battle... So your only option is to fight!\n\nThe rules of the arena are simple... survive 20 rounds and defeat all of the enemies! Good luck."""
    )

    input("Press enter to begin...")
    return name
