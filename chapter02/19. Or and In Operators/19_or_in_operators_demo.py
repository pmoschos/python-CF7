choice = 'q'

# or
if choice == 'q' or choice == "Q":
    print("OK")
else:
    print("Not OK")

# upper
if choice.upper() == 'Q':
    print("OK")
else:
    print("Not OK")

# in (Pythonian!)
if choice in ('q', 'Q'):
        print("OK")
else:
    print("Not OK")