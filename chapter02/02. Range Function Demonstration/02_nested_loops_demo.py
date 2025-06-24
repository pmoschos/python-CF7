print("Nested loops in Python (multiplication example)")

for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end=" | ")
    print()
print()