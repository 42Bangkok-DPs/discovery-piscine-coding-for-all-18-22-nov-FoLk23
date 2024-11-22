while True:
    user_input = input("What you gotta say? ('STOP' for end ): ")

    if user_input.upper() == "STOP":
        print("END.")
        break
    else:
        print(f"You say: {user_input}")
