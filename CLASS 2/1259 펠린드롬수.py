while True:
    word = input()
    if word == "0":
        break
    print("yes" if word == word[::-1] else "no")
