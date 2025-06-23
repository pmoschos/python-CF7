# Python 2: returned a list which was not efficient
# There was the xrange() which was efficient

# Python 3
# range() function: returns a range-object
# generates a sequence of numbers on the fly (efficient)

# range(start, end, step)
# start: inclusive
# end: exclusive

# print odd numbers from 1 to 21
# Java style:
print("Java style")
for i in range(22):
    if i % 2 != 0:
        print(i, end=' ')
print()


# Python Style
print("Python style")
for i in range(1, 22, 2):
    print(i, end=' ')
print()
