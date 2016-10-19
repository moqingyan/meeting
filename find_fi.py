def find_fi(number, total):
    for ct in range(1, total):
        if (( number ** ct ) % total == 1):
            print("num is: " + str( number ** ct ))
            return ct
    return -1

numbers = [1,5,7,11,13,17]
for i in numbers:
    print(str(i) + " is " + str(find_fi(i,18)))