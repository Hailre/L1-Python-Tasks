pin_number = int(input("Please enter your pin number: "))
i = 0
while i < pin_number:
    print(str(i).zfill(4))
    i += 1
pin = str(i).zfill(4)
print(f"Your pin is: {pin}")
